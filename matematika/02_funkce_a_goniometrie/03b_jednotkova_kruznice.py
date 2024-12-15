import pygame
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Inicializace pygame
pygame.init()

# Nastavení okna pygame
width, height = 600, 800
win = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
pygame.display.set_caption("Goniometrie na kružnici a grafy funkcí")

# Barvy
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Parametry kružnice
radius = 150
center = (width // 2, height // 4)
da = 0.025

# Nastavení grafu s matplotlib
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(0, 2 * math.pi)
ax.set_ylim(-1.5, 1.5)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
sin_line, = ax.plot([], [], label='sin(x)', color='blue')
cos_line, = ax.plot([], [], label='cos(x)', color='red')

# Funkce pro vykreslování grafu
def update_graph(angle):
    x_vals = np.linspace(0, 2 * math.pi, int(2 * math.pi / da))
    y_vals_sin = np.sin(x_vals)
    y_vals_cos = np.cos(x_vals)
    
    sin_line.set_data(x_vals[:angle], y_vals_sin[:angle])
    cos_line.set_data(x_vals[:angle], y_vals_cos[:angle])
    ax.legend()

# Funkce pro vykreslení grafu do Pygame okna
def draw_graph_to_pygame():
    canvas = FigureCanvas(fig)
    canvas.draw()
    size = canvas.get_width_height()
    data = canvas.tostring_rgb()
    surface = pygame.image.fromstring(data, size, "RGB")
    win.blit(surface, ((width - size[0]) // 2, center[1] + radius))

# Pohybující se bod
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aktualizace okna
    win.fill(white)
    
    # Kružnice
    pygame.draw.circle(win, black, center, radius, 1)
    
    # Pohybující se bod na jednotkové kružnici
    x = center[0] + radius * math.cos(angle)
    y = center[1] - radius * math.sin(angle)
    pygame.draw.line(win, red, center, (x, center[1]), 1)  # Cosine
    pygame.draw.line(win, blue, center, (center[0], y), 1)  # Sine
    pygame.draw.circle(win, black, (int(x), int(y)), 5)
    
    # Vykreslení grafu pomocí matplotlib
    update_graph(int(angle / da))  # Aktualizace grafu v matplotlib
    draw_graph_to_pygame()  # Vykreslení grafu do pygame okna
    
    # Aktualizace úhlu
    angle += da
    if angle > 2 * math.pi:
        angle = 0

    pygame.display.update()
    pygame.time.delay(50)

pygame.quit()
