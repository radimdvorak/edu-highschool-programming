import pygame
import math

# Inicializace Pygame
pygame.init()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simulátor Sluneční soustavy")
clock = pygame.time.Clock()

# Barvy
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)  # Slunce
BLUE = (0, 0, 255)  # Země
RED = (255, 0, 0)  # Mars

# Gravitační konstanta (zjednodušená pro simulaci)
G = 6.67430e-11
scale = 1e9  # 1 pixel = 1 miliarda metrů
time_step = 3600 * 24  # Jeden simulovaný den (sekundy)

# Třída pro těleso
class Body:
    def __init__(self, x, y, vx, vy, mass, radius, color):
        self.x = x  # Pozice na ose x (m)
        self.y = y  # Pozice na ose y (m)
        self.vx = vx  # Rychlost ve směru x (m/s)
        self.vy = vy  # Rychlost ve směru y (m/s)
        self.mass = mass  # Hmotnost (kg)
        self.radius = radius  # Poloměr (pro vykreslení)
        self.color = color  # Barva
        self.path = []  # Trajektorie

    def update_position(self, bodies):
        # Výpočet gravitačních sil
        fx = 0
        fy = 0
        for body in bodies:
            if body == self:
                continue
            dx = body.x - self.x
            dy = body.y - self.y
            distance = math.sqrt(dx**2 + dy**2)
            if distance == 0:
                continue
            force = G * self.mass * body.mass / distance**2
            fx += force * dx / distance
            fy += force * dy / distance

        # Aktualizace rychlosti na základě síly
        ax = fx / self.mass
        ay = fy / self.mass
        self.vx += ax * time_step
        self.vy += ay * time_step

        # Aktualizace pozice na základě rychlosti
        self.x += self.vx * time_step
        self.y += self.vy * time_step

        # Uložení bodu trajektorie
        self.path.append((self.x, self.y))

    def draw(self, screen):
        # Přepočet pozice na obrazovku
        screen_x = int(self.x / scale + screen_width / 2)
        screen_y = int(self.y / scale + screen_height / 2)
        pygame.draw.circle(screen, self.color, (screen_x, screen_y), self.radius)

        # Vykreslení trajektorie
        if len(self.path) > 1:
            scaled_path = [(int(x / scale + screen_width / 2), int(y / scale + screen_height / 2)) for x, y in self.path]
            pygame.draw.lines(screen, self.color, False, scaled_path, 1)

# Inicializace těles
sun = Body(0, 0, 0, 0, 1.989e30, 20, YELLOW)  # Slunce
earth = Body(1.496e11, 0, 0, 29780, 5.972e24, 5, BLUE)  # Země
mars = Body(2.279e11, 0, 0, 24077, 6.417e23, 4, RED)  # Mars

bodies = [sun, earth, mars]

# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for body in bodies:
        body.update_position(bodies)
        body.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
