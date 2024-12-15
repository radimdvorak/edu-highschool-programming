from sympy import symbols, Eq, solve

def solve_equation():
    print("Program na řešení rovnic")
    x = symbols('x')  # Definice proměnné
    expr = input("Zadejte levou část rovnice rovnu nule (např. x**2 + 2*x - 8): ")
    
    # Řešení
    equation = Eq(eval(expr), 0)
    solutions = solve(equation, x)
    
    print("\nRovnice:")
    print(equation.args[0], " = ", equation.args[1])
    print("\nŘešení:")
    print(solutions)

solve_equation()
