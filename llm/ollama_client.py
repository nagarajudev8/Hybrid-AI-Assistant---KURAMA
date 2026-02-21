import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

def generate_response(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"]

    return "Kurama encountered an error."
