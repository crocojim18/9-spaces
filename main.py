import sys, pygame
pygame.init()

WIDTH = 650
HEIGHT = 450

screen = pygame.display.set_mode((WIDTH,HEIGHT))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((110,198,211))
    pygame.display.flip()