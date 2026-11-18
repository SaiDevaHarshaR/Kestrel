from ..core.config import settings
from google import genai
from .vector_store import results
def joining():
    a1 = results["documents"]
    re = " ".join(a1)
    return re
client = genai.Client(api_key = settings.gemini_api_key.get_secret_value())


