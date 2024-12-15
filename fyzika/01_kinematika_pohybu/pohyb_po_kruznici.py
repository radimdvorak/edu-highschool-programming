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

# uhlova rychlost [rad / s]
phi = 3.1415 / 4

# pridani telesa do prostoru
teleso = pymunk.Body()
# pocatecni rychlost - vektor
teleso.velocity = pymunk.Vec2d(200, 0)
teleso.position = pymunk.Vec2d(0, -200)
hmotny_bod = pymunk.Circle(teleso, 5)
hmotny_bod.mass = 1 # dulezite pro simulator pymunk (kg)
space.add(teleso, hmotny_bod)

font = pygame.font.Font(None, 20)

# nekonecny cyklus
while True:
    for event in pygame.event.get():
        if (
            event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE
        ):
            exit()

    steps = int(teleso.velocity.length)
    for i in range(steps):
        # ad = v^2 / r
        velikost_ad = teleso.velocity.length * teleso.velocity.length / teleso.position.length

        # vypocet vektoru dostrediveho zrychleni
        relativni_pozice = pymunk.Vec2d(0, 0) - teleso.position
        ad = relativni_pozice.normalized() * velikost_ad

        # vektor rychlosti doplnime o pusobeni dostrediveho zrychleni
        teleso.velocity += ad * (dt / steps)

        # nechame vypocitat dalsi krok simulace za jednotku casu - dt
        space.step(dt / steps)

    # nejdrive vyplnime obrazovku cernou barvou
    screen.fill(pygame.Color("black"))

    pygame.draw.circle(screen, "white", pocatek, 3)
    
    pygame.draw.circle(screen, "white", pocatek, teleso.position.length, 1)

    # nakreslime objekty (telesa) vzhledem od pocatku (scitani vektoru)
    pygame.draw.circle(screen, "white", pocatek + teleso.position, hmotny_bod.radius)

    # nakreslime vektor rychlosti od pocatku
    pygame.draw.line(screen, "white", pocatek + teleso.position, pocatek + teleso.position + teleso.velocity)

    pygame.draw.line(screen, "orange", pocatek + teleso.position, pocatek + teleso.position + ad)

    screen.blit(font.render(f"dostredive zrychleni: {ad.x:.3f},{ad.y:.3f}, velikost: {velikost_ad:.3f}", True, pygame.Color("orange")), (5, 5))
    screen.blit(font.render(f"rychlost: {teleso.velocity.x:.3f},{teleso.velocity.y:.3f}, velikost: {teleso.velocity.length:.3f}", True, pygame.Color("white")), (5, 20))

    # po vykresleni zobrazime
    pygame.display.flip()
    clock.tick(FPS)

    # aktualizujeme udaj na okne
    pygame.display.set_caption(f"FPS: {clock.get_fps():.2f} {teleso.velocity.length:.2f}")
