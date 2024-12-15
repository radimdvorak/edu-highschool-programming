import pygame
import math

# Inicializace Pygame
pygame.init()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simulátor Sluneční soustavy s Měsícem")
clock = pygame.time.Clock()

# Barvy
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)  # Slunce
BLUE = (0, 0, 255)  # Země
GRAY = (200, 200, 200)  # Měsíc
RED = (255, 0, 0)  # Mars

# Gravitační konstanta (zjednodušená pro simulaci)
G = 6.67430e-11
scale = 1e9  # 1 pixel = 1 miliarda metrů
time_step = 3600 * 24 / 6  # Jedna šestina simulovaného dne (sekundy)

# Faktor vizuálního oddálení Měsíce od Země
moon_visual_offset = 30  # Zvětšení vzdálenosti Měsíce při kreslení (násobek skutečné vzdálenosti)

# Třída pro těleso
class Body:
    def __init__(self, x, y, vx, vy, mass, radius, color, center_body = None):
        self.x = x  # Pozice na ose x (m)
        self.y = y  # Pozice na ose y (m)
        self.vx = vx  # Rychlost ve směru x (m/s)
        self.vy = vy  # Rychlost ve směru y (m/s)
        self.mass = mass  # Hmotnost (kg)
        self.radius = radius  # Poloměr (pro vykreslení)
        self.color = color  # Barva
        self.center_body = center_body # teleso, kolem ktereho obiha
        self.path = []  # Trajektorie
        self.visual_path = [] # Vizuální trajektorie - souřadnice na obrazovce

    def update_position(self, bodies, time_step):
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

    def draw(self, screen, reference_body=None, visual_offset = 0):
        # Přepočet pozice na obrazovku
        screen_x = self.x / scale + screen_width / 2
        screen_y = self.y / scale + screen_height / 2

        # Pokud je těleso Měsíc, vizuálně ho oddálíme od Země
        if reference_body:
            dx = screen_x - (reference_body.x / scale + screen_width / 2)
            dy = screen_y - (reference_body.y / scale + screen_height / 2)
            screen_x += dx * visual_offset
            screen_y += dy * visual_offset

        pygame.draw.circle(screen, self.color, (screen_x, screen_y), self.radius)

        # Uložení bodu trajektorie
        self.visual_path.append((screen_x, screen_y))
        self.path.append((self.x, self.y))

        while len(self.path) > 1e4:
            self.path = self.path[1:]
        while len(self.visual_path) > 1e4:
            self.path = self.visual_path[1:]

        # Vykreslení trajektorie
        if reference_body and len(self.visual_path) > 1:
            scaled_path = [(x, y) for x, y in self.visual_path]
            pygame.draw.lines(screen, self.color, False, scaled_path, 1)
        elif len(self.path) > 1:
            scaled_path = [(int(x / scale + screen_width / 2), int(y / scale + screen_height / 2)) for x, y in self.path]
            pygame.draw.lines(screen, self.color, False, scaled_path, 1)

# Inicializace těles
sun = Body(0, 0, 0, 0, 1.989e30, 20, YELLOW)  # Slunce
earth = Body(1.496e11, 0, 0, 29780, 5.972e24, 5, BLUE)  # Země
moon = Body(1.496e11 + 3.844e8, 0, 0, 29780 + 1022, 7.348e22, 2, GRAY)  # Měsíc
mars = Body(2.279e11, 0, 0, 24077, 6.417e23, 4, RED)  # Mars

bodies = [sun, earth, moon, mars]
# bodies = [sun, earth, mars]

# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    N = 24
    for i in range(N):
        dt = time_step / N
        for body in bodies:
            body.update_position(bodies, dt)

    for body in bodies:
        if body == moon:
            # Měsíc kreslíme s ohledem na vizuální oddálení od Země
            body.draw(screen, reference_body=earth, visual_offset=moon_visual_offset)
        else:
            body.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
