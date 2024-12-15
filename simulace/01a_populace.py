import numpy as np
import matplotlib.pyplot as plt

# Parametry
P0 = 1000       # Počáteční populace
r = 0.03        # Rychlost růstu
K = 5000        # Nosná kapacita prostředí (pro logistický růst)
time = np.linspace(0, 100, 100)  # Časová osa

# Exponenciální růst
def exponential_growth(P0, r, t):
    return P0 * np.exp(r * t)

# Logistický růst
def logistic_growth(P0, r, K, t):
    return (K * P0 * np.exp(r * t)) / (K + P0 * (np.exp(r * t) - 1))

# Výpočty pro exponenciální a logistický růst
exp_growth = exponential_growth(P0, r, time)
log_growth = logistic_growth(P0, r, K, time)

# Vizualizace
plt.figure(figsize=(10, 6))
plt.plot(time, exp_growth, label="Exponenciální růst", color="blue")
plt.plot(time, log_growth, label="Logistický růst", color="green")
plt.axhline(K, color='red', linestyle=':', label="Kapacita prostředí")
plt.xlabel("Čas")
plt.ylabel("Populace")
plt.title("Simulace exponenciálního a logistického růstu populace")
plt.legend()
plt.grid()
plt.show()
