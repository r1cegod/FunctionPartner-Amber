import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

if not key or "sk-proj" not in key:
    print("Error: OPENAI_API_KEY not found or invalid.")

client = OpenAI(api_key=key)

def brain(mytext):
    """
    Sends text to OpenAI and returns content + token usage.
    Returns: (content, prompt_tokens, completion_tokens)
    """
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": mytext}
            ]
        )
        content = completion.choices[0].message.content
        itoken = completion.usage.prompt_tokens
        utoken = completion.usage.completion_tokens
        return content, itoken, utoken
    except Exception as e:
        # Return error message and 0 tokens on failure
        return f"Error: {e}", 0, 0
