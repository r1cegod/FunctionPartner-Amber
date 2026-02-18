import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

if not key or "sk-proj" not in key:
    print("yo something is wrong with the apikey dude")
    sys.exit()

client = OpenAI(api_key=key)

def brain(user_text):
    try:
        completion = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": "you are a helpful assitant"},
                {"role": "user", "content": user_text}
            ]
        )
        respond = completion.choices[0].message.content
        itoken = completion.usage.prompt_tokens
        utoken = completion.usage.completion_tokens
        return respond, itoken, utoken
    except Exception as e:
        return f"{e}", 0, 0