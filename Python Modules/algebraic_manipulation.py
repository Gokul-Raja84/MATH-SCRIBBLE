import sympy as sp

def algebraic_manipulation_example():
    x, y = sp.symbols('x y')
    expression1 = x**2 + 2*x + 1
    expression2 = x**2 - 4*x + 4

    simplified_expression = sp.simplify(expression1 * expression2)
    expanded_expression = sp.expand((x + 1)**3)
    factored_expression = sp.factor(x**2 - 1)

    print(f"Expression 1: {expression1}")
    print(f"Expression 2: {expression2}")
    print(f"Simplified Expression: {simplified_expression}")
    print(f"Expanded Expression: {expanded_expression}")
    print(f"Factored Expression: {factored_expression}")

if __name__ == "__main__":
    algebraic_manipulation_example()
