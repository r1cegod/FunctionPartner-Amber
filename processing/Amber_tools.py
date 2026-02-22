from langchain_core.tools import tool
from sympy import *
from spb import *
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor
)
import re

trans = standard_transformations + (implicit_multiplication_application, convert_xor)

@tool
def graph_plot(equation_str: str)-> str:
    """This tool generate a visual graph for the formula you put in (str, only use 0-9 /*^.-+=) use this tool when the user tell you to 'visualize' a graph"""
    try:
        x, y, a, b, c, d = symbols("x, y, a, b, c, d")

        if "y" and "=" in equation_str.lower():
            left, right = equation_str.split('=')
            equation = Eq(parse_expr(left, transformations=trans), parse_expr(right, transformations=trans))
            y_answers = solve(equation, y)
            y_answers = y_answers[0]
            answer = Poly(y_answers)
        else:
            y_answers = parse_expr(equation_str, transformations=trans)
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

        clipped_formula = Piecewise((formula, And(formula >= -10, formula <= 10)), (nan, True))

        p = plot(
            clipped_formula, 
            (x, -10, 10),
            params=params,
            imodule='panel',
            backend=PB, 
            show=False,
            line_color='blue'
        )

        p.fig.update_xaxes(
            dtick=1,
            gridcolor='#333333', 
            zeroline=True,
            zerolinecolor='white',
            zerolinewidth=2
        )
        p.fig.update_yaxes(
            dtick=1,
            gridcolor='#333333',
            zeroline=True,
            zerolinecolor='white',
            zerolinewidth=2
        )
        p.fig.update_layout(
            dragmode='pan',
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white'
        )
        p.fig.update_traces(
            line=dict(
                color='#00aaff',
                width=3
            )
        )
        p.fig.layout.modebar={'remove': ['zoom', 'box', 'select', 'lasso', 'autoscale']}
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