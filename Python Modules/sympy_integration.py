import sympy as sp

def symbolic_integration_example():
    x = sp.symbols('x')
    expression = x**2 + 2*x + 1

    integrated_expression = sp.integrate(expression, x)
    print(f"Original Expression: {expression}")
    print(f"Integrated Expression: {integrated_expression}")

if __name__ == "__main__":
    symbolic_integration_example()
