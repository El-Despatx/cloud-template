from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="Sample user API",
    description="API for managing user data",
    version="0.1.0",
)

@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")