from pydantic import BaseModel
from fastapi import status, Depends, FastAPI
from .core.config import settings, Settings
from .core.dependencies  import get_settings
from .llm.service import generate_response_stream
from fastapi.responses import StreamingResponse

app = FastAPI(
        title=settings.app_name,
        version=settings.app_version
)
class HealthCheck(BaseModel):
    status: str
    app_name: str


class ChatRequest(BaseModel):
    query: str



@app.post("/chat/stream")
async def prompt(request: ChatRequest):
    prompt = request.query
    ans = generate_response_stream(prompt)
    return StreamingResponse(content=ans, media_type="text/plain")




@app.get(
    "/health",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck
)
async def health(
    config: Settings = Depends(get_settings)
) -> HealthCheck:
    return HealthCheck(
        status="OK",
        app_name=config.app_name
    )