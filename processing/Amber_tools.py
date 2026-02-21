from langchain_core.tools import tool
from sympy import *
from spb import *
import re

@tool
def graph_plot(equation_str: str)-> str:
    """This tool generate a visual graph for the formula you put in (str, only use 0-9 /*^.-+=) use this tool when the user tell you to 'visualize' a graph"""
    try:
        x, y, a, b, c, d = symbols("x, y, a, b, c, d")

        left, right = equation_str.split('=')
        equation = Eq(sympify(left, convert_xor=True), sympify(right, convert_xor=True))
        y_answers = solve(equation, y)
        y_answers = y_answers[0]
        answer = Poly(y_answers)

        deg = answer.degree()
        coeffs = answer.all_coeffs()
        if deg == 3:
            a_val, b_val, c_val, d_val = coeffs
            formula = a*x**3 + b*x**2 + c*x + d
        if deg == 2:
            a_val, b_val, c_val = coeffs
            d_val = 0
            formula = a*x**2 + b*x + c
        params = {
            a: (a_val, 0, 20),
            b: (b_val, 0, 20),
            c: (c_val, 0, 20),
            d: (d_val, 0, 20)
        }

        p = plot(formula, (x, -10, 10), params=params, imodule='panel', backend=PB, show=False)
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