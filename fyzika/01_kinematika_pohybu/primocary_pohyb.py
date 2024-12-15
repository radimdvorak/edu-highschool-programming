import pygame
import pymunk

# snimku za vterinu
FPS = 60
# zakladni jednotka casu (v sekundach)
dt = 1.0 / FPS # (s)

# ---------------------
# nastaveni pygame
pygame.init()
# ---------------------
# # hodiny v pygame
clock = pygame.time.Clock()
# obrazovka - 1 pixel odpovida 1 m
velikost_obrazovky = pymunk.Vec2d(600, 600)
screen = pygame.display.set_mode(velikost_obrazovky)
pocatek = velikost_obrazovky / 2

# ---------------------
# nastaveni pymunk
# dvourozmerny prostor 
space = pymunk.Space()

# aplikovane zrychleni - vektor
zrychleni = pymunk.Vec2d(1, -1)

# pridani telesa do prostoru
teleso = pymunk.Body()
# pocatecni rychlost - vektor
teleso.velocity = pymunk.Vec2d(1, -1)
hmotny_bod = pymunk.Circle(teleso, 3)
hmotny_bod.mass = 1 # dulezite pro simulator pymunk (kg)
space.add(teleso, hmotny_bod)

# nekonecny cyklus
while True:
    for event in pygame.event.get():
        if (
            event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE
        ):
            exit()

    # vektor rychlosti zvetsime
    teleso.velocity += zrychleni * dt

    # nechame vypocitat dalsi krok simulace za jednotku casu - dt
    space.step(dt)

    # nejdrive vyplnime obrazovku cernou barvou
    screen.fill(pygame.Color("black"))

    # nakreslime objekty (telesa) vzhledem od pocatku (scitani vektoru)
    pygame.draw.circle(screen, "white", pocatek + teleso.position, hmotny_bod.radius)

    # nakreslime vektor rychlosti od pocatku
    pygame.draw.line(screen, "white", pocatek, pocatek + teleso.velocity)

    # po vykresleni zobrazime
    pygame.display.flip()
    clock.tick(FPS)

    # aktualizujeme udaj na okne
    pygame.display.set_caption(f"FPS: {clock.get_fps():.2f} {teleso.velocity.length:.2f}")
