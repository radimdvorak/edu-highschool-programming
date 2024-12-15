import pymunk
import pymunk.pygame_util
import pygame
import sys

# Inicializace pygame a nastavení okna
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulace srážky dvou těles")
clock = pygame.time.Clock()

# Inicializace pymunk prostoru
space = pymunk.Space()
space.gravity = (0, 0)  # Žádná gravitace (pohyb po přímce)

# Funkce pro vytvoření tělesa
def create_ball(space, position, velocity, mass=1, radius=15):
    body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
    body.position = position
    body.velocity = velocity
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 1.0  # Dokonale pružná srážka
    space.add(body, shape)
    return shape

# Vytvoření dvou těles
ball1 = create_ball(space, position=(200, HEIGHT // 2), velocity=(100, 0))  # Těleso 1
ball2 = create_ball(space, position=(600, HEIGHT // 2), velocity=(-100, 0))  # Těleso 2

# Vykreslovací nástroj pro pymunk
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Hlavní smyčka programu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aktualizace pymunk simulace
    space.step(1 / 60)  # Simulace 60 FPS

    # Vyčištění obrazovky
    screen.fill((255, 255, 255))

    # Vykreslení těles
    space.debug_draw(draw_options)

    # Aktualizace obrazovky
    pygame.display.flip()

    # Nastavení FPS
    clock.tick(60)

# Ukončení programu
pygame.quit()
sys.exit()
