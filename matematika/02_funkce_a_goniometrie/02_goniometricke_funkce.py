import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definice goniometrických funkcí
x = np.linspace(-2 * np.pi, 2 * np.pi, 500)

y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

# Nastavení grafu
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-2 * np.pi, 2 * np.pi)
ax.set_ylim(-2, 2)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')

sin_line, = ax.plot([], [], label='sin(x)', color='blue')
cos_line, = ax.plot([], [], label='cos(x)', color='red')
tan_line, = ax.plot([], [], label='tan(x)', color='green', alpha=0.5)

def update(frame):
    sin_line.set_data(x[:frame], y_sin[:frame])
    cos_line.set_data(x[:frame], y_cos[:frame])
    tan_line.set_data(x[:frame], y_tan[:frame])
    return sin_line, cos_line, tan_line

ani = FuncAnimation(fig, update, frames=len(x), interval=30, blit=True)

ax.legend()
ax.grid()
plt.title('Goniometrické funkce')
plt.show()
