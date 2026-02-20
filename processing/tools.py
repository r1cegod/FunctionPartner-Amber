from langchain_core.tools import tool

@tool
def calculate(expression: str) -> str:
    """Calculate a math expression (important: '2^3'='2**3'), always return a short approximate numbers (e.g. '21,323,424.32' not 21,323,424.32423143124)."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"{e}"
