from ..llm.client import client
from fastapi import HTTPException
from google.genai import errors
def generate_response(prompt:str) -> str:
    try:
        response = client.models.generate_content( model='gemini-3.8-flash',contents=prompt, streaming = True )
        if not response or not response.text:
            raise HTTPException(status_code=502, detail="AI returned an empty response.",)
        return response.text
    except errors.APIError as e:
        raise HTTPException(
            status_code=e.code or 502,
            detail=e.message or "AI API error.",
        )