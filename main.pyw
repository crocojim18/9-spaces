import sys, pygame
from functions import *

pygame.init()

WIDTH = 650
HEIGHT = 450

screen = pygame.display.set_mode((WIDTH,HEIGHT))
thisFont = pygame.font.SysFont("TimesNewRoman", 30)
str1 = getText(2)
str2 = getText(4)
str3 = "A game I'm slowly working on"
buttonWidth = thisFont.size("Exit")
butto = pygame.Rect(295,centerText(thisFont, str2, WIDTH)-5,buttonWidth[0]+10,buttonWidth[1]+10)
title = thisFont.render(str1, 1, (30,30,30))
exitaisvou = thisFont.render(str2, 1, (30,30,30))
desc = thisFont.render(str3, 1, (30,30,30))


while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if butto.collidepoint(pygame.mouse.get_pos()):
				sys.exit()
		
	screen.fill((110,198,211))
	pygame.draw.rect(screen, (109, 139, 188), butto)
	screen.blit(title, (centerText(thisFont, str1, WIDTH),100))
	screen.blit(desc, (centerText(thisFont, str3, WIDTH),150))
	screen.blit(exitaisvou, (centerText(thisFont, str2, WIDTH),300))
    
	pygame.display.flip()

