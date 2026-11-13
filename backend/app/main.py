from pydantic import BaseModel
from fastapi import status, Depends, FastAPI
from .core.config import settings, Settings
from .core.dependencies  import get_settings
app = FastAPI(
        title=settings.app_name,
        version=settings.app_version
)
