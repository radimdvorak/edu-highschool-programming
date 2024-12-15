import pygame
import pymunk
import pymunk.pygame_util
import matplotlib.pyplot as plt

# Inicializace pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simulace vzájemného působení těles s třením a grafy")
clock = pygame.time.Clock()

# Inicializace Pymunk prostoru
space = pymunk.Space()
space.gravity = (0, 0)
damping = 0.999  # Koeficient tlumení (simuluje odpor prostředí)

# Funkce pro vytvoření kruhového tělesa
def create_circle(space, position, radius, mass, color):
    body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.9  # Mírná ztráta energie při nárazu
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
        line.elasticity = 0.9
    space.add(*static_lines)

create_walls(space, screen_width, screen_height)

# Vizualizační nástroj pro Pygame
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Data pro grafy
time_data = []
velocity1_data = []
velocity2_data = []
position1_data = []
position2_data = []

# Funkce pro měření sil během kolizí
collision_forces = []

def record_collision(arbiter, space, data):
    force = arbiter.total_impulse.length
    collision_forces.append(force)
    return True

space.add_default_collision_handler().post_solve = record_collision

# Hlavní smyčka simulace
running = True
t = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aktualizace simulace
    t += 1 / 60
    space.step(1 / 60.0)
    for body in space.bodies:
        body.velocity *= damping  # Aplikace odporu prostředí

    # Ukládání dat pro grafy
    time_data.append(t)
    velocity1_data.append(circle1.body.velocity.length)
    velocity2_data.append(circle2.body.velocity.length)
    position1_data.append(circle1.body.position[0])
    position2_data.append(circle2.body.position[0])

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
    force_text = font.render(
        f"Síla poslední kolize: {collision_forces[-1]:.2f} N" if collision_forces else "Síla poslední kolize: -- N",
        True,
        (0, 0, 0),
    )
    screen.blit(vel_text1, (10, 10))
    screen.blit(vel_text2, (10, 30))
    screen.blit(force_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# Grafy pohybu a rychlosti
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(time_data, velocity1_data, label="Těleso 1 (červené)", color='red')
plt.plot(time_data, velocity2_data, label="Těleso 2 (modré)", color="blue")
plt.title("Rychlost v čase")
plt.xlabel("Čas (s)")
plt.ylabel("Rychlost (m/s)")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(time_data, position1_data, label="Těleso 1 (červené)", color='red')
plt.plot(time_data, position2_data, label="Těleso 2 (modré)", color='blue')
plt.title("Poloha v čase")
plt.xlabel("Čas (s)")
plt.ylabel("Poloha na ose X (m)")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(range(len(collision_forces)), collision_forces, label="Síly při kolizích")
plt.title("Síla při kolizích")
plt.xlabel("Počet kolizí")
plt.ylabel("Síla (N)")
plt.legend()

plt.tight_layout()
plt.show()
