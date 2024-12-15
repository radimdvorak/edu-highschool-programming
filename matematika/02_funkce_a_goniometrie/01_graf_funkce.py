import numpy as np
import matplotlib.pyplot as plt

#funkce = input("Napiste funkci: ")

# Definice funkce
def fx():
    return 'x**2 + 2*x - 4'

# Definiční obor
x = np.linspace(-10, 10, 400)
# rozsireni o eval
y = eval(fx())

# Vypočítáme obor hodnot
min_y = min(y)
max_y = max(y)

# Vykreslení grafu
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=fx(), color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')

# Zvýrazníme definiční obor a obor hodnot
plt.fill_between(x, min_y, max_y, color='lightblue', alpha=0.2, label='Obor hodnot')

plt.title('Graf funkce f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()
