import pygame
import math
import random

# Inicializace Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kanónová hra")
clock = pygame.time.Clock()

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Konstanty
g = 9.81  # Gravitační zrychlení (m/s^2)
ground_level = screen_height - 50  # Hladina země

# Třída pro projektil
class Projectile:
    def __init__(self, x, y, angle, velocity, mass):
        self.x = x
        self.y = y
        self.angle = math.radians(angle)  # Převod na radiány
        self.vx = velocity * math.cos(self.angle)  # Počáteční rychlost ve směru x
        self.vy = -velocity * math.sin(self.angle)  # Počáteční rychlost ve směru y (negativní kvůli osám)
        self.mass = mass
        self.path = []  # Sledování trajektorie

    def update(self, dt):
        # Pohyb projektilu podle fyzikálních zákonů
        self.vy += g * dt  # Vliv gravitace na rychlost
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Ukládání bodů trajektorie
        self.path.append((self.x, self.y))

    def draw(self, screen):
        # Vykreslení projektilu
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 5)
        # Vykreslení trajektorie
        if len(self.path) > 1:
            pygame.draw.lines(screen, BLUE, False, self.path, 2)

# Třída pro překážky
class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

    def check_collision(self, projectile):
        if (
            self.x <= projectile.x <= self.x + self.width
            and self.y <= projectile.y <= self.y + self.height
        ):
            return True
        return False

# Funkce pro vykreslení kanónu
def draw_cannon(screen, angle):
    base_x, base_y = 50, ground_level
    barrel_length = 50
    end_x = base_x + barrel_length * math.cos(math.radians(angle))
    end_y = base_y - barrel_length * math.sin(math.radians(angle))
    pygame.draw.line(screen, BLACK, (base_x, base_y), (end_x, end_y), 5)
    pygame.draw.circle(screen, BLACK, (base_x, base_y), 10)

# Inicializace hry
def main():
    running = True
    angle = 45  # Výchozí úhel
    velocity = 50  # Výchozí rychlost
    mass = 1.0  # Výchozí hmotnost projektilu
    projectile = None
    obstacles = [Obstacle(random.randint(300, 700), ground_level - 100, 50, 100)]  # Náhodná překážka

    while running:
        screen.fill(WHITE)

        # Vykreslení země
        pygame.draw.rect(screen, BLACK, (0, ground_level, screen_width, 50))

        # Vykreslení kanónu
        draw_cannon(screen, angle)

        # Vykreslení překážek
        for obstacle in obstacles:
            obstacle.draw(screen)

        # Vykreslení projektilu
        if projectile:
            projectile.update(1 / 60)  # Aktualizace každých 1/60 sekundy
            projectile.draw(screen)

            # Kontrola kolize s překážkami
            for obstacle in obstacles:
                if obstacle.check_collision(projectile):
                    print("Kolize s překážkou!")
                    projectile = None
                    break

            # Kontrola dopadu na zem
            if projectile and projectile.y > ground_level:
                print("Projektil dopadl na zem.")
                projectile = None

        # Zpracování událostí
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Vystřelení projektilu
                    projectile = Projectile(50, ground_level, angle, velocity, mass)
                elif event.key == pygame.K_UP:
                    angle = min(angle + 5, 90)  # Zvýšení úhlu
                elif event.key == pygame.K_DOWN:
                    angle = max(angle - 5, 0)  # Snížení úhlu
                elif event.key == pygame.K_RIGHT:
                    velocity += 5  # Zvýšení rychlosti
                elif event.key == pygame.K_LEFT:
                    velocity = max(velocity - 5, 5)  # Snížení rychlosti
                elif event.key == pygame.K_w:
                    mass += 0.1  # Zvýšení hmotnosti
                elif event.key == pygame.K_s:
                    mass = max(mass - 0.1, 0.1)  # Snížení hmotnosti

        # Vykreslení informací
        font = pygame.font.SysFont("Arial", 16)
        angle_text = font.render(f"Úhel: {angle}°", True, BLACK)
        velocity_text = font.render(f"Rychlost: {velocity} m/s", True, BLACK)
        mass_text = font.render(f"Hmotnost: {mass:.1f} kg", True, BLACK)
        screen.blit(angle_text, (10, 10))
        screen.blit(velocity_text, (10, 30))
        screen.blit(mass_text, (10, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
