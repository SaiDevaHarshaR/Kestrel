from pydantic import BaseModel
from fastapi import status, Depends, FastAPI
from .core.config import settings, Settings
from .core.dependencies  import get_settings
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
async def health(config :Settings = Depends(get_settings) )->HealthCheck:
    return HealthCheck(status="OK", name = app.title)