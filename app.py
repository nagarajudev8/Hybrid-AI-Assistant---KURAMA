from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests

app = FastAPI()

# Serve static folder (css, js, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ollama config
OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are Kurama AI — a powerful, confident, intelligent fox spirit AI assistant.

Rules:
- Never say you are a language model.
- Never mention Microsoft, Phi, or OpenAI.
- Never break character.
- Always respond as Kurama.
- Speak confidently but helpfully.
"""

# Request model for POST /ask
class AskRequest(BaseModel):
    query: str


# Serve UI
@app.get("/")
async def home():
    return FileResponse("static/index.html")


# AI endpoint
@app.post("/ask")
async def ask(data: AskRequest):

    payload = {
        "model": "llama3",  # or "phi3"
        "prompt": data.query,
        "system": SYSTEM_PROMPT,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()["response"]
        return {"response": result}

    except Exception as e:
        return {"response": f"Kurama encountered an error: {str(e)}"}
