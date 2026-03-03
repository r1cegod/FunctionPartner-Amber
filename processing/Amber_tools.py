from langchain_core.tools import tool
from sympy import symbols, Eq, solve, Poly, fraction
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor
)
import re

trans = standard_transformations + (implicit_multiplication_application, convert_xor)

@tool
def graph_plot(equation_str: str) -> str:
    """Parse a math formula and return its type + coefficients for the frontend to render.
    Use this when the user wants to visualize a formula.
    Input: formula string e.g. 'x^3 - 3x + 2', 'x^2 - 4', 'x^4 - 4x^2 + 3', '(2x+1)/(x-1)'"""
    try:
        x, y = symbols("x y")

        # Solve for y if in equation form (e.g. "y = x^2 + 1")
        if "y" in equation_str.lower() and "=" in equation_str.lower():
            left, right = equation_str.split("=", 1)
            eq = Eq(parse_expr(left, transformations=trans), parse_expr(right, transformations=trans))
            expr = solve(eq, y)[0]
        else:
            expr = parse_expr(equation_str, transformations=trans)

        #DETECT phanthuoc: (ax+b)/(cx+d)
        numer, denom = fraction(expr)
        if denom != 1:
            p_n = Poly(numer, x)
            p_d = Poly(denom, x)
            if p_n.degree() == 1 and p_d.degree() == 1:
                a_val, b_val = [float(c) for c in p_n.all_coeffs()]
                c_val, d_val = [float(c) for c in p_d.all_coeffs()]
                return f"GRAPH:phanthuoc:{a_val},{b_val},{c_val},{d_val}"
            return "Error: Rational function must be linear/linear form (ax+b)/(cx+d)"

        # --- Polynomial types ---
        poly = Poly(expr, x)
        deg = poly.degree()
        # all_coeffs() returns [highest → lowest], zero-padded
        all_c = [float(c) for c in poly.all_coeffs()]

        if deg == 2:
            # bac2: y = ax² + bx + c → coefficients: [a, b, c]
            a_val, b_val, c_val = all_c
            return f"GRAPH:bac2:{a_val},{b_val},{c_val}"

        elif deg == 3:
            # bac3: y = ax³ + bx² + cx + d → coefficients: [a, b, c, d]
            a_val, b_val, c_val, d_val = all_c
            return f"GRAPH:bac3:{a_val},{b_val},{c_val},{d_val}"

        elif deg == 4:
            # bac4tp (trung phuong): y = ax⁴ + bx² + c (no odd powers)
            # all_coeffs for degree 4: [a, x3, b, x1, c]
            a_val, x3_val, b_val, x1_val, c_val = all_c
            if abs(x3_val) > 0.001 or abs(x1_val) > 0.001:
                return "Error: Degree-4 formula must have no odd powers (use ax\u2074 + bx\u00B2 + c form)"
            return f"GRAPH:bac4tp:{a_val},{b_val},{c_val}"

        else:
            return f"Error: Degree {deg} not supported. Use degree 2, 3, 4 (even only), or rational (ax+b)/(cx+d)."

    except Exception as e:
        return f"Error: {e}"

@tool
def calculate(expression: str) -> str:
    """Use this tool to calculate simple math, return steps, concise number answer (not 1234.12/13 or 1234.1212121212 but 1234.12)"""
    expression = expression.replace(" ", "")
    if not re.match(r'^[0-9+\-*/()**.]+$', expression):
        return "Unsafe characters detected."
    try:
        from sympy import sympify
        math_result = sympify(expression, convert_xor=True)
        return str(float(math_result))
    except Exception as e:
        return f"{e}"