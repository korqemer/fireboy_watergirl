import pygame
from sys import exit

pygame.init()

# display surface -> x, y
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Fireboy and Watergirl")
clock = pygame.time.Clock()

# added surface
backgorund_surface = pygame.image.load("graphics/background.png")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(backgorund_surface, (0, 0))


    pygame.display.update()
    clock.tick(60)
