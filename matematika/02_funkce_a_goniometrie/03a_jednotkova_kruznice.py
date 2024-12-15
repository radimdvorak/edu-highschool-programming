import pygame
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Nastavení pygame
pygame.init()

# Parametry okna
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Goniometrie na kružnici s grafem")

# Barvy
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Parametry kružnice
radius = 200
center = (width // 2, height // 2)

# Úhel a ukládání hodnot
angle = 0
angles = []
sin_values = []
cos_values = []

# Nastavení matplotlib
plt.ion()
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 2 * math.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Průběh funkcí sin(x) a cos(x)")
ax.grid()
line_sin, = ax.plot([], [], label="sin(x)", color="red")
line_cos, = ax.plot([], [], label="cos(x)", color="blue")
ax.legend()

# Funkce pro aktualizaci grafu
def update_plot():
    line_sin.set_data(angles, sin_values)
    line_cos.set_data(angles, cos_values)
    plt.draw()
    plt.pause(0.001)

# Hlavní smyčka pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Výpočet souřadnic bodu
    x = center[0] + radius * math.cos(angle)
    y = center[1] - radius * math.sin(angle)

    # Ukládání hodnot pro graf
    angles.append(angle)
    sin_values.append(math.sin(angle))
    cos_values.append(math.cos(angle))

    # Zajištění, že graf nezobrazuje příliš mnoho hodnot
    if len(angles) > 200:
        angles.pop(0)
        sin_values.pop(0)
        cos_values.pop(0)

    # Aktualizace grafu
    update_plot()

    # Vykreslení v pygame
    win.fill(white)
    pygame.draw.circle(win, black, center, radius, 1)
    pygame.draw.line(win, blue, center, (x, center[1]), 1)  # Cosine
    pygame.draw.line(win, red, center, (center[0], y), 1)  # Sine
    pygame.draw.circle(win, black, (int(x), int(y)), 5)

    # Posun úhlu
    angle += 0.05
    if angle > 2 * math.pi:
        angle = 0
        angles.clear()
        sin_values.clear()
        cos_values.clear()

    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()
plt.close()
