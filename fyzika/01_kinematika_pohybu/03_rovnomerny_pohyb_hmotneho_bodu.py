import pygame
import sys

# Inicializace pygame
pygame.init()

# Parametry okna
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rovnoměrný pohyb hmotného bodu")

# Barvy
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Parametry pohybu
x = 50 # počátek polohy x na obrazovce
y = HEIGHT // 2 # poloha uprostřed obrazovky
v = float(input("Zadejte rychlost pohybu (px/s): ")) # 1 pixel odpovídá 1 metru 

clock = pygame.time.Clock()

# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Výpočet nové polohy
    x += v * clock.get_time() / 1000  # převod na sekundy
    if x > WIDTH:
        x = 0  # restart na druhou stranu
    
    # Vykreslení - každý snímek je třeba vykresilt celý
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (int(x), y), 20)
    pygame.display.flip()
    
    # FPS
    clock.tick(60)

pygame.quit()
sys.exit()
