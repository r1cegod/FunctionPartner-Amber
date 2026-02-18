def user_input():
    try:
        return input("You: ").strip()
    except (EOFError, KeyboardInterrupt):
        return "exit"