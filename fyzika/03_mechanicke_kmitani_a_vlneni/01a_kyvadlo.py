import numpy as np
import matplotlib.pyplot as plt

# Parametry kyvadla
L = 1         # Délka kyvadla (m)
g = 9.81      # Gravitační zrychlení (m/s^2)
theta0 = 0.2  # Počáteční úhlová výchylka (rad)
omega0 = 0    # Počáteční úhlová rychlost (rad/s)
t = np.linspace(0, 10, 1000)  # Časová osa (s)

# Výpočet úhlové frekvence
omega = np.sqrt(g / L)

# Výpočet úhlové výchylky v čase pomocí analytického řešení
theta = theta0 * np.cos(omega * t) + (omega0 / omega) * np.sin(omega * t)

# Vizualizace pohybu kyvadla
plt.figure(figsize=(10, 6))
plt.plot(t, theta, label="Úhlová výchylka (θ)", color="green")
plt.xlabel("Čas (s)")
plt.ylabel("Úhlová výchylka (rad)")
plt.title("Pohyb jednoduchého kyvadla")
plt.legend()
plt.grid()
plt.show()
