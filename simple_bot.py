"""
Amber Tier 1: The Chatter (OpenAI Integration)
Target: Single file, uses .env for security, connects to Real Brain.
"""
import sys, time, os
from dotenv import load_dotenv
from openai import OpenAI

# 1. SETUP (The 'Configuration' Block)
load_dotenv() # Load environment variables from .env
api_key = os.getenv("OPENAI_API_KEY")

if not api_key or "Paste" in api_key:
    print("ERROR: OPENAI_API_KEY not found in .env file.")
    print("Please open .env and paste your key.")
    sys.exit(1)

# Configure OpenAI
client = OpenAI(api_key=api_key)

def slow_print(text):
    """Simulates typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def ask_openai(user_text):
    """The 'Brain' of the agent (Real LLM Call)."""
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini", # Using cheaper model for testing
            messages=[
                {"role": "system", "content": "You are Amber, a helpful AI assistant."},
                {"role": "user", "content": user_text}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Brain Freeze: {e}"

def main():
    print("--- AMBER (Tier 1 - OpenAI Connected) ---")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            # 1. INPUT
            user_text = input("You: ")
            if user_text.lower() in ["exit", "quit"]:
                print("Amber: Goodbye.")
                break
            
            # 2. PROCESSING
            print("Amber: Thinking...", end="\r")
            try:
                response = ask_openai(user_text)
            except Exception as e:
                response = f"Error: {e}"

            # 3. OUTPUT
            # Clear "Thinking..." line (works in most terminals)
            sys.stdout.write("\033[K") 
            sys.stdout.write("\r") # Return to start of line
            sys.stdout.write("Amber: ")
            slow_print(response)
            
        except KeyboardInterrupt:
            print("\nAmber: Goodbye.")
            break

if __name__ == "__main__":
    main()
