from ..core.config import settings
from google import genai

client = genai.Client(api_key = settings.gemini_api_key.get_secret_value())