import pygame
import pymunk
import pymunk.pygame_util

# Inicializace pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simulace vzájemného působení těles")
clock = pygame.time.Clock()

# Inicializace Pymunk prostoru
space = pymunk.Space()
space.gravity = (0, 0)

# Funkce pro vytvoření kruhového tělesa
def create_circle(space, position, radius, mass, color):
    body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 1.0  # Perfektně pružná kolize
    shape.friction = 0.5
    shape.color = color
    space.add(body, shape)
    return shape

# Vytvoření dvou těles
circle1 = create_circle(space, (200, 300), 30, 1, (255, 0, 0, 255))  # Těleso 1 (červené)
circle2 = create_circle(space, (600, 300), 50, 3, (0, 0, 255, 255))  # Těleso 2 (modré)

# Přidání počátečních rychlostí
circle1.body.velocity = (200, 0)  # Rychlost červeného tělesa
circle2.body.velocity = (-100, 0)  # Rychlost modrého tělesa

# Přidání stěn kolem scény
def create_walls(space, screen_width, screen_height):
    static_lines = [
        pymunk.Segment(space.static_body, (0, 0), (screen_width, 0), 1),  # Horní stěna
        pymunk.Segment(space.static_body, (0, 0), (0, screen_height), 1),  # Levá stěna
        pymunk.Segment(space.static_body, (0, screen_height), (screen_width, screen_height), 1),  # Spodní stěna
        pymunk.Segment(space.static_body, (screen_width, 0), (screen_width, screen_height), 1),  # Pravá stěna
    ]
    for line in static_lines:
        line.elasticity = 1.0
    space.add(*static_lines)

create_walls(space, screen_width, screen_height)

# Vizualizační nástroj pro Pygame
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Hlavní smyčka simulace
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aktualizace simulace
    space.step(1 / 60.0)

    # Vykreslení scény
    screen.fill((255, 255, 255))  # Bílý podklad
    space.debug_draw(draw_options)  # Kreslí tělesa pomocí pymunku

    # Vykreslení informací o rychlostech
    font = pygame.font.SysFont("Arial", 16)
    vel_text1 = font.render(
        f"Těleso 1 - rychlost: {circle1.body.velocity.length:.2f} m/s", True, (0, 0, 0)
    )
    vel_text2 = font.render(
        f"Těleso 2 - rychlost: {circle2.body.velocity.length:.2f} m/s", True, (0, 0, 0)
    )
    screen.blit(vel_text1, (10, 10))
    screen.blit(vel_text2, (10, 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
