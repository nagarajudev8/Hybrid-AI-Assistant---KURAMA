def classify_intent(user_input: str) -> str:
    system_keywords = ["disk", "process", "cpu", "memory", "uptime"]

    for keyword in system_keywords:
        if keyword in user_input.lower():
            return "system"

    return "chat"
