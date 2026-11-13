from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import status
from .core.config import settings
app = FastAPI(
        title=settings.app_name,
        version=settings.app_version
)
class HealthCheck(BaseModel):
    status :str
    

@app.get("/")
async def root():
    return {"message": "Hello ChatGPT"}


@app.get("/health", status_code=status.HTTP_200_OK,response_model=HealthCheck)
async def health( )->HealthCheck:
    return HealthCheck(status="OK")