from google import generate_content
from google import genai
from ..llm.client import client
client = genai.client(client)
response = client.models.generate_content( model='gemini-3.8-flash',contents="Explain Agentic AI in simple words"  )

print(response.text)