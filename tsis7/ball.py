import pygame

pygame.init()
SIZE = [800, 800]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Game")

radius = 50
clock = pygame.time.Clock()
velocity = 10
x, y = 100, 100
screenWidth, screenHeight = screen.get_width(), screen.get_height()

running = True

while running:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - 50 > 0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x + 50 < screenWidth:
        x += velocity
    if keys[pygame.K_UP] and y - 50 > 0:
        y -= velocity
    if keys[pygame.K_DOWN] and y + 50 < screenHeight:
        y += velocity

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pygame.display.flip()

pygame.quit()
