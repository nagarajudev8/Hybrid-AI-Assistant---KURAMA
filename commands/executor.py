import subprocess
from commands.allowed_commands import ALLOWED_COMMANDS

def execute_command(user_input: str) -> str:
    for key, command in ALLOWED_COMMANDS.items():
        if key in user_input.lower():
            try:
                result = subprocess.check_output(
                    command, shell=True, text=True
                )
                return result
            except Exception as e:
                return f"Execution Error: {str(e)}"

    return "Command not allowed."
