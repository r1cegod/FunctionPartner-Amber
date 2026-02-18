def prompt_user():
    try:
        return input("You: ").strip()
    except (EOFError, KeyboardInterrupt):
        return "exit"