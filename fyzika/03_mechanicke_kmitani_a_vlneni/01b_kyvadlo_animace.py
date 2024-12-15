import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parametry kyvadla
L = 1         # Délka kyvadla (m)
g = 9.81      # Gravitační zrychlení (m/s^2)
theta0 = 0.4  # Počáteční úhlová výchylka (rad)
t = np.linspace(0, 10, 500)  # Časová osa (s)

# Výpočet úhlové frekvence
omega = np.sqrt(g / L)

# Výpočet úhlové výchylky v čase
theta = theta0 * np.cos(omega * t)

# Převod úhlové výchylky na souřadnice x, y koncového bodu kyvadla
x = L * np.sin(theta)
y = -L * np.cos(theta)

# Vytvoření grafu
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-L - 0.1, L + 0.1)
ax.set_ylim(-L - 0.1, L + 0.1)

# Vytvoření objektů pro animaci (tyč a hmotný bod na konci kyvadla)
line, = ax.plot([0, x[0]], [0, y[0]], lw=2, color='blue')
mass, = ax.plot([x[0]], [y[0]], 'o', color='red', markersize=10)

# Funkce pro aktualizaci pozice kyvadla v každém kroku animace
def update(i):
    line.set_data([0, x[i]], [0, y[i]])      # Aktualizace tyče
    mass.set_data([x[i]], [y[i]])            # Aktualizace polohy hmotného bodu
    return line, mass

# Nastavení animace
ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)

# Zobrazení animace
plt.title("Animace pohybu kyvadla")
plt.show()
