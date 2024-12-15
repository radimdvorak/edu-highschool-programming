import pygame
import math
import sys

# Inicializace pygame
pygame.init()

# Nastavení velikosti okna
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulace pohybu v rovině")

# Barvy
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Nastavení FPS
clock = pygame.time.Clock()
FPS = 60

# Proměnné pro pohyb
t = 0  # Časová proměnná
speed = 2  # Rychlost pohybu

previous_pos_circle = ()
previous_pos_line = ()
previous_screen = pygame.Surface((WIDTH, HEIGHT))
previous_screen.fill(WHITE)

# Hlavní smyčka programu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(previous_screen, (0, 0))

    # 1. Pohyb po přímce
    x_line = 50 + t * speed  # Horizontální pohyb
    y_line = 300
    if previous_pos_line:
        pygame.draw.line(screen, BLUE, previous_pos_line, (x_line, y_line))

    # 2. Kruhový pohyb
    r = 100  # Poloměr kružnice
    x_circle = WIDTH // 2 + r * math.cos(t / 30)  # x = r * cos(t)
    y_circle = HEIGHT // 2 + r * math.sin(t / 30)  # y = r * sin(t)
    if previous_pos_circle:
        pygame.draw.line(screen, RED, previous_pos_circle, (x_circle, y_circle))

    # Uložíme si obrazovku na příští smyčku
    previous_screen.blit(screen, (0, 0))

    pygame.draw.circle(screen, BLUE, (int(x_line), int(y_line)), 10)
    previous_pos_line = (x_line, y_line)
    pygame.draw.circle(screen, RED, (int(x_circle), int(y_circle)), 10)
    previous_pos_circle = (x_circle, y_circle)

    # Aktualizace času a obrazovky
    t += 1
    pygame.display.flip()
    clock.tick(FPS)

# Ukončení programu
pygame.quit()
sys.exit()
