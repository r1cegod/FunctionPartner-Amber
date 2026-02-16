import sys
import sys, os, time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

if not key or "sk-proj" not in key:
    print("Yo you forgot the api key")
    sys.exit(1)

def text_ani(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

client = OpenAI(api_key=key)

def brain(mytext):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "you are a helpful assitant"},
                {"role": "user", "content": mytext}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"{e}"

def main():
    while True:
        try:
            mytext = input("You: ")
            if mytext.lower() in ["exit", "quit"]:
                print("Amber: Goodbye!")
                break
            print("Amber: Thinking... ", end="\r")
            try:
                response = brain(mytext)
            except Exception as e:
                return f"{e}"
            sys.stdout.write("\033[K")
            sys.stdout.write("\r")
            sys.stdout.write("Amber: ")
            text_ani(response)
        except KeyboardInterrupt:
            print("\nAmber: goodbye")
            break

if __name__ == "__main__":
    main()