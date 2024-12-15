from sympy import symbols, simplify, expand, factor

def simplify_expression():
    print("Program na zjednodušování matematických výrazů")
    # Vstup od uživatele
    expression = input("Zadejte matematický výraz (např. x*(x + 2) + 1): ")
    x = symbols('x')  # Definice proměnné
    expr = simplify(expression)

    # Výpočty
    print("\nPůvodní výraz:")
    print(expression)

    print("\nZjednodušený výraz:")
    print(expr)

    extended_expression = expand(expression)
    print("\nRozvinutý výraz:")
    print(extended_expression)

    factored_expression = factor(expression)
    print("\nZjednodušený výraz (faktorizovaný):")
    print(factored_expression)

simplify_expression()
