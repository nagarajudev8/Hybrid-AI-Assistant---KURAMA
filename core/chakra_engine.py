from core.sharingan import classify_intent
from llm.ollama_client import generate_response
from commands.executor import execute_command

def process_input(user_input: str) -> str:
    intent = classify_intent(user_input)

    if intent == "system":
        return execute_command(user_input)

    return generate_response(user_input)
