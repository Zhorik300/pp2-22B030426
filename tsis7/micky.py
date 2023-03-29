import pygame
import os
from datetime import datetime

pygame.init()

SIZE = [500, 500]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Clock")

clock = pygame.image.load(os.path.abspath("images/clock.png")).convert_alpha()
long_arrow = pygame.image.load(os.path.abspath("images/arrow.png")).convert_alpha()
long_arrow = pygame.transform.rotate(long_arrow, 0)
secondsAngle = 0
minutesAngle = 0
hoursAngle = 0
running = True
dt = datetime.now()


def getSecondsArrow(angle, clock_rect, surface):
    m = pygame.transform.scale(long_arrow, (30, 180))
    arrRect = m.get_rect()
    surface.blit(m, (surface.get_rect().width / 2 - arrRect.width / 2, 0))

    surface = pygame.transform.rotate(surface, -angle)
    backRec = surface.get_rect()

    backRec.center = clock_rect.center

    screen.blit(surface, backRec)


def getMinutesArrow(angle, clock_rect, surface):
    m = pygame.transform.scale(long_arrow, (30, 150))
    arrRect = m.get_rect()
    surface.blit(m, (surface.get_rect().width / 2 - arrRect.width / 2, 25))

    surface = pygame.transform.rotate(surface, -angle)
    backRec = surface.get_rect()

    backRec.center = clock_rect.center

    screen.blit(surface, backRec)


while running:
    pygame.time.Clock().tick(1)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    dt = datetime.now()

    secondsAngle = dt.second * 6
    minutesAngle = dt.minute * 6
    hoursAngle = dt.hour * 10

    # Draw an image
    # clock
    clock = pygame.transform.scale(clock, (400, 400))
    clock_rec = clock.get_rect()
    clock_rec.center = screen.get_rect().center
    screen.blit(clock, clock_rec)

    # seconds
    secSurface = pygame.Surface((60, 320), pygame.SRCALPHA)

    getSecondsArrow(secondsAngle, clock_rec, secSurface)

    # minutes
    minSurface = pygame.Surface((60, 320), pygame.SRCALPHA)
    getMinutesArrow(minutesAngle, clock_rec, minSurface)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()