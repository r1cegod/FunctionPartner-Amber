import os, re
from dotenv import load_dotenv
from openai import OpenAI

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculate a math expression (important: '**' = power = '^'), always return a short approximate numbers (e.g. '21,323,424.32' not 21,323,424.32423143124).",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The math formula to solve."
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

if not key or "sk-proj" not in key:
    print("yo something is wrong with the apikey dude")
    sys.exit()

client = OpenAI(api_key=key)

def brain(history):
    try:
        completion = client.chat.completions.create(
            model="gpt-5-mini",
            messages=history,
            tools=tools,
            tool_choice="auto"
        )
        respond_obj = completion.choices[0].message
        itoken = completion.usage.prompt_tokens
        utoken = completion.usage.completion_tokens
        return respond_obj, itoken, utoken
    except Exception as e:
        print(f"BRAIN ERROR: {e}")
        return f"{e}", 0, 0

def calculate(expression):
    expression = expression.replace(" ", "")
    if not re.match(r'^[0-9+\-*/().]+$', expression):
        return "Unsafe characters detected."
    try:
        return str(eval(expression))
    except Exception as e:
        return f"{e}"