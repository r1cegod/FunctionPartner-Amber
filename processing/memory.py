import json

def save_memory(history, filename="memory.json"):
    with open(filename, "w") as f:
        json.dump(history, f)

def load_memory(filename="memory.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []