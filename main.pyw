import sys, pygame
from functions import *

pygame.init()

WIDTH = 650
HEIGHT = 450

screen = pygame.display.set_mode((WIDTH,HEIGHT))
thisFont = pygame.font.SysFont("TimesNewRoman", 30)
str1 = getText(2)
title = thisFont.render(str1, 1, (30,30,30))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
			sys.exit()
		
	screen.fill((110,198,211))
	screen.blit(title, (centerText(thisFont, str1, WIDTH),100))
		
    
    pygame.display.flip()

