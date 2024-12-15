import pygame
import math
import sys

# Inicializace pygame
pygame.init()

# Nastavení velikosti okna
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometrické animace")

# Barvy
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Nastavení FPS
clock = pygame.time.Clock()
FPS = 60

# Koule
ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2  # Počáteční pozice
ball_dx, ball_dy = 3, 4  # Počáteční rychlost (ve směrech x a y)

# Rotující trojúhelník
triangle_vertices = [(0, -50), (50, 50), (-50, 50)]  # Lokální souřadnice trojúhelníku
triangle_center = (WIDTH // 4, HEIGHT // 2)  # Střed rotace
rotation_angle = 0  # Počáteční úhel rotace

# Funkce pro rotaci bodu kolem středu
def rotate_point(point, center, angle):
    px, py = point
    cx, cy = center
    rad = math.radians(angle)
    x_new = math.cos(rad) * (px - cx) - math.sin(rad) * (py - cy) + cx
    y_new = math.sin(rad) * (px - cx) + math.cos(rad) * (py - cy) + cy
    return (x_new, y_new)

# Hlavní smyčka programu
running = True
while running:
    screen.fill(WHITE)  # Vyčištění obrazovky

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Pohyb koule
    ball_x += ball_dx
    ball_y += ball_dy

    # Kontrola odrazů od stěn
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_dx *= -1  # Invertujeme směr v ose x
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_dy *= -1  # Invertujeme směr v ose y

    # Kreslení koule
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_radius)

    # 2. Rotace trojúhelníku
    rotation_angle += 1  # Zvyšujeme úhel rotace
    rotated_vertices = [rotate_point(v, triangle_center, rotation_angle) for v in triangle_vertices]

    # Kreslení trojúhelníku
    pygame.draw.polygon(screen, RED, rotated_vertices)

    # Aktualizace obrazovky
    pygame.display.flip()
    clock.tick(FPS)

# Ukončení programu
pygame.quit()
sys.exit()
