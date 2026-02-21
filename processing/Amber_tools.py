from langchain_core.tools import tool
from sympy import symbols, sympify, Eq, solve
from spb import plot, PB
import re

@tool
def graph_plot(equation_str: str)-> str:
    """This tool generate a visual graph for the formula you put in (str, only use 0-9 /*^.-+=) use this tool when the user tell you to 'visualize' a graph"""
    try:
        x,y = symbols('x y')

        left, right = equation_str.split('=')
        equation = Eq(sympify(left, convert_xor=True), sympify(right, convert_xor=True))

        y_answers = solve(equation, y)

        p = plot(y_answers, (x, -10, 10), backend=PB, show=False)
        p.save("graph.html")
        return "Graph created sucessfully, tell the user that"
    except Exception as e:
        return f"Error: {e}"
@tool
def calculate(expression: str)-> str:
    """Use this tool to calculate simple math, return steps, conside number answer (not 1234.12/13 or 1234.1212121212 but 1234.12)"""
    expression = expression.replace(" ", "")
    if not re.match(r'^[0-9+\-*/()**.]+$', expression):
        return "Unsafe characters detected."
    try:
        math_result = sympify(expression, convert_xor=True)
        return str(float(math_result))
    except Exception as e:
        return f"{e}"