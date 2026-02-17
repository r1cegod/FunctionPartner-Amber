import sys, os, time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key or not "sk-proj" in api_key:
    print("yo there is something wrong with your api key dude")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def brain(user_text):
    try:
        completion = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": "you are a helpful assitant"},
                {"role": "user", "content": user_text}
            ]
        )
        content = completion.choices[0].message.content
        itoken = completion.usage.prompt_tokens
        utoken = completion.usage.completion_tokens
        return content, itoken, utoken
    except Exception as e:
        return f"{e}", 0, 0

def textani(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def main():
    print("Simple chat bot v1.1")
    print("type 'exit' to exit")
    total_input = 0
    total_output = 0
    total = 0
    while True:
        try:
            user_text = input("You: ")
            if user_text.lower() in ["exit"]:
                print(f"Input: {total_input}")
                print(f"Output: {total_output}")
                print(f"Completion token: {total}")
                break
            print("Amber: Thinking...", end="\r")
            try:
                respond, itoken, utoken = brain(user_text)
                total_input += itoken
                total_output += utoken
                total += itoken + utoken
            except Exception as e:
                return f"{e}", 0, 0
            sys.stdout.write("\033[K")
            sys.stdout.write("\r")
            sys.stdout.write("Amber: ")
            textani(respond)
        except KeyboardInterrupt:
            print(f"Input: {total_input}")
            print(f"Output: {total_output}")
            print(f"Completion token: {total}")
            break
if __name__ == "__main__":
    main()