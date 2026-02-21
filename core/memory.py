conversation_history = []

def store_message(role: str, message: str):
    conversation_history.append({"role": role, "message": message})

def get_history():
    return conversation_history
