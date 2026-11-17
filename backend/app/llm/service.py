from ..llm.client import client
from fastapi import HTTPException
from google import genai
from google.genai import errors
from typing import Iterator
def generate_response_stream(prompt: str) -> Iterator[str]:
    try:
        stream = client.models.generate_content_stream(
            model="gemini-3.8-flash",
            contents=prompt
        )
        for chunk in stream:
            if chunk.text:
                yield chunk.text
    except errors.APIError as e:
        raise HTTPException(
            status_code=502,
            detail=e.message or "AI streaming error."
        )
def generate_response(prompt:str) -> str:
    try:
        response = client.models.generate_content( model='gemini-3.8-flash',contents=prompt )
        if not response or not response.text:
            raise HTTPException(status_code=502, detail="AI returned an empty response.",)
        return response.text
    except errors.APIError as e:
        raise HTTPException(
            status_code=e.code or 502,
            detail=e.message or "AI API error.",
        )