from fastapi import FastAPI
from core.chakra_engine import process_input

app = FastAPI(title="KURAMA AI")

@app.post("/ask")
def ask_kurama(payload: dict):
    user_input = payload.get("message")

    if not user_input:
        return {"error": "Message is required"}

    response = process_input(user_input)
    return {"response": response}
