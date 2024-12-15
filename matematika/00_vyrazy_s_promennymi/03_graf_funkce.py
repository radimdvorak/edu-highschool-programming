import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify

def plot_function():
    print("Program na vizualizaci grafu funkce")
    x = symbols('x')  # Definice proměnné
    expression = input("Zadejte výraz funkce (např. x**2 - 3*x + 2): ")
    
    # Převod na Python funkci
    f = lambdify(x, expression, "numpy")
    
    # Vytvoření hodnot x a y
    # lze nahradit cyklem
    x_vals = np.linspace(-10, 10, 500)
    y_vals = f(x_vals)
    
    # Vykreslení grafu
    plt.plot(x_vals, y_vals, label=f"f(x) = {expression}")
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.title("Graf funkce")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()

plot_function()
