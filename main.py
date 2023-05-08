import pygame
from sys import exit

pygame.init()

# display surface -> x, y
screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("Fireboy and Watergirl")
clock = pygame.time.Clock()


# added surface
background_surface = pygame.image.load("graphics/ground.png")

# timer
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = test_font.render('Time: ', True, 'Black')
text_rect = text_surface.get_rect(midtop = (400, 10))

watergirl = pygame.image.load("graphics/2.png").convert_alpha()
watergirl_rect = watergirl.get_rect(midbottom = (700, 700))

fireboy = pygame.image.load("graphics/1.png").convert_alpha()
fireboy_rect = fireboy.get_rect(midbottom = (90, 700))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255,255,255))
    screen.blit(background_surface, (0, 700))

    fireboy_rect.left += 2
    screen.blit(fireboy, fireboy_rect)

    watergirl_rect.left -= 2
    screen.blit(watergirl, watergirl_rect)

    pygame.draw.rect(screen, "Pink", text_rect)
    pygame.draw.rect(screen, "Pink", text_rect, 7)
    screen.blit(text_surface, text_rect)


    # if watergirl_rect.colliderect(fireboy_rect):
    #     screen.blit(text_surface, (250, 350))
    #


    pygame.display.update()
    clock.tick(60)
