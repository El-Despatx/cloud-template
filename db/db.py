import os
from typing import Annotated

from fastapi import Depends
from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine

IS_PROD = ["true", "1"]

def get_engine() -> Engine:
    return get_prod_engine() if is_production() else get_dev_engine()


def get_prod_engine() -> Engine:
    raise NotImplementedError("Production database not implemented yet")

def get_dev_engine() -> Engine:
    sqlite_file = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file}"
    connect_args = {"check_same_thread": False}
    return create_engine(sqlite_url, echo=True, connect_args=connect_args)

def is_production() -> bool:
    prod: str |None = os.getenv("PROD", "false")
    prod = prod.lower()
    return prod in IS_PROD

def create_db_and_tables():
    engine = get_engine()
    SQLModel.metadata.create_all(engine)

def get_session():
    engine = get_engine()
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]