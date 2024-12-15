import pygame
import sys

# Inicializace pygame
pygame.init()

# Nastavení velikosti okna
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tangram - Skládání tvarů")

# Barvy
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Třída pro tvary
class Shape:
    def __init__(self, points, color):
        self.points = points  # Body tvaru (seznam souřadnic)
        self.color = color
        self.is_dragging = False  # Indikace, zda se tvar přesouvá

    def draw(self, surface):
        """Nakreslení tvaru."""
        pygame.draw.polygon(surface, self.color, self.points)

    def move(self, dx, dy):
        """Posun tvaru o dx, dy."""
        self.points = [(x + dx, y + dy) for x, y in self.points]

    def is_point_inside(self, pos):
        """Zjištění, zda je bod uvnitř tvaru."""
        polygon_rect = pygame.Rect(min(x for x, _ in self.points),
                                   min(y for _, y in self.points),
                                   max(x for x, _ in self.points) - min(x for x, _ in self.points),
                                   max(y for _, y in self.points) - min(y for _, y in self.points))
        return polygon_rect.collidepoint(pos)

# Vytvoření tvarů
shapes = [
    Shape([(100, 100), (150, 50), (200, 100)], BLUE),  # Trojúhelník
    Shape([(300, 300), (400, 300), (400, 400), (300, 400)], GREEN),  # Čtverec
    Shape([(500, 100), (550, 50), (600, 100), (550, 150)], RED)  # Kosočtverec
]

# Hlavní smyčka programu
running = True
selected_shape = None

while running:
    screen.fill(WHITE)  # Vyčištění obrazovky

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detekce kliknutí myší
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Levé tlačítko myši
                for shape in shapes:
                    if shape.is_point_inside(event.pos):  # Kontrola, zda je klik uvnitř tvaru
                        shape.is_dragging = True
                        selected_shape = shape
                        break

        # Uvolnění tlačítka myši
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Levé tlačítko myši
                if selected_shape:
                    selected_shape.is_dragging = False
                    selected_shape = None

        # Pohyb myší
        elif event.type == pygame.MOUSEMOTION:
            if selected_shape and selected_shape.is_dragging:
                dx, dy = event.rel  # Posun myši
                selected_shape.move(dx, dy)

    # Kreslení tvarů
    for shape in shapes:
        shape.draw(screen)

    pygame.display.flip()  # Aktualizace obrazovky

# Ukončení programu
pygame.quit()
sys.exit()
