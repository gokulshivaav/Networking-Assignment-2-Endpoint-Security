import subprocess

ALLOWED_ACTIONS = {
    "kill_notepad": "taskkill /F /IM notepad.exe",
    "disable_testuser": "net user testuser123 /active:no"
}

def execute_action(action):
    if action not in ALLOWED_ACTIONS:
        print(f"[DENIED] Action '{action}' is not allowlisted")
        return

    command = ALLOWED_ACTIONS[action]

    print(f"[ACTION] Executing: {action}")
    print(f"[COMMAND] {command}")

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    print("\n--- OUTPUT ---")
    print(result.stdout)

    if result.stderr:
        print("\n--- ERRORS ---")
        print(result.stderr)

if __name__ == "__main__":
    execute_action("disable_testuser")