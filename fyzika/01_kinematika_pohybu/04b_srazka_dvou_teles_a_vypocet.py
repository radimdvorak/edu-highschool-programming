import time
import pymunk
import pymunk.pygame_util
import pygame
import sys

init_time = time.time()

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
def create_ball(space, position, velocity, collision_type, mass=1, radius=15):
    body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
    body.position = position
    body.velocity = velocity
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 1.0  # Dokonale pružná srážka
    shape.collision_type = collision_type  # Nastavení typu kolize
    space.add(body, shape)
    return shape

# Výpočet teoretického místa a času srážky
def calculate_collision(ball1, ball2):
    pos1, vel1 = ball1.body.position.x, ball1.body.velocity.x
    pos2, vel2 = ball2.body.position.x, ball2.body.velocity.x
    if vel1 == vel2:  # Tělesa mají stejnou rychlost, nikdy se nesrazí
        return None, None
    t_collision = (pos2 - pos1) / (vel1 - vel2)
    if t_collision < 0:  # Srážka se stala v minulosti, není relevantní
        return None, None
    x_collision = pos1 + vel1 * t_collision
    return t_collision, x_collision

# Proměnné pro uchování výsledků kolize
collision_data = {"detected": False, "time": None, "position": None}

# Funkce pro zpracování kolize
def handle_collision(arbiter: pymunk.Arbiter, space, data):
    # Zpracujeme kolizi pouze jednou
    if not collision_data["detected"]:
        collision_data["detected"] = True
        collision_data["time"] = time.time() - init_time
        collision_data["position"] = arbiter.contact_point_set.points[0].point_a[0]
        print("Srážka detekována! ", collision_data["time"], collision_data["position"])
    return True  # Vrací True, aby simulace pokračovala normálně

# Vytvoření dvou těles
ball1 = create_ball(space, position=(200, HEIGHT // 2), velocity=(100, 0), collision_type=1)  # Těleso 1
ball2 = create_ball(space, position=(600, HEIGHT // 2), velocity=(-100, 0), collision_type=2)  # Těleso 2

# Výpočet teoretického času a místa srážky
t_collision, x_collision = calculate_collision(ball1, ball2)
# if t_collision is not None and x_collision is not None:
#     collision_data["time"] = t_collision
#     collision_data["position"] = x_collision

# Nastavení kolizního handleru
collision_handler = space.add_collision_handler(1, 2)  # Typy kolizí těles
collision_handler.begin = handle_collision  # Připojení zpracovávací funkce

# Vykreslovací nástroj pro pymunk
draw_options = pymunk.pygame_util.DrawOptions(screen)

init_time = time.time()

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

    # Zobrazení informace o teoretickém čase a místě srážky
    if t_collision is not None and x_collision is not None:
        font = pygame.font.Font(None, 24)  # Větší font
        text = font.render(
            f"Srážka: t={t_collision:.2f}s, x={x_collision:.2f}px",
            True,
            (0, 0, 0) # černý text
        )
        screen.blit(text, (10, 10))
        # Vykreslení čáry na místě srážky
        pygame.draw.line(screen, (0, 0, 0), (x_collision, 0), (x_collision, HEIGHT), 2)

    # Zobrazení informace o detekovan0m čase a místě srážky
    if collision_data["time"] is not None and collision_data["position"] is not None:
        font = pygame.font.Font(None, 24)  # Větší font
        text = font.render(
            f"Detekovaná srážka: t={collision_data["time"]:.2f}s, x={collision_data["position"]:.2f}px",
            True,
            (255, 0, 0)  # Červený text
        )
        screen.blit(text, (10, 30))

    # Aktualizace obrazovky
    pygame.display.flip()

    # Nastavení FPS
    clock.tick(60)

# Ukončení programu
pygame.quit()
sys.exit()
