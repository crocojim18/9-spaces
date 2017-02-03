import sys, pygame
from functions import *

pygame.init()


WIDTH = 650
HEIGHT = 450

screen = Screen(WIDTH, HEIGHT)
thisFont = pygame.font.SysFont("TimesNewRoman", 30)
str1 = getText(2)
str2 = getText(4)
str3 = getText(3)
gameClock = pygame.time.Clock()
buttonWidth = thisFont.size(str2)
button2Width = thisFont.size(str3)
butto = pygame.Rect(centerText(thisFont, str2, WIDTH)-5,295,buttonWidth[0]+10,buttonWidth[1]+10)
butto2 = pygame.Rect(centerText(thisFont, str3, WIDTH)-5,215,button2Width[0]+10,button2Width[1]+10)
title = thisFont.render(str1, 1, (30,30,30))
exitaisvou = thisFont.render(str2, 1, (30,30,30))
desc = thisFont.render(str3, 1, (30,30,30))
screen.interpretMap('maps/first.map')
isBlue = True
ned = Character(0,0)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if butto2.collidepoint(pygame.mouse.get_pos()):
				if isBlue: screen.interpretMap('maps/second.map')
				else: screen.interpretMap('maps/first.map')
				isBlue = not isBlue
			elif butto.collidepoint(pygame.mouse.get_pos()):
				sys.exit()
		
	screen.fill()
	screen.drawRect(butto, 109, 139, 188)
	screen.drawRect(butto2, 109, 139, 188)
	ned.exist()
	screen.place(ned)
	screen.placeText(title, centerText(thisFont, str1, WIDTH),100)
	screen.placeText(desc, centerText(thisFont, str3, WIDTH),220)
	screen.placeText(exitaisvou, centerText(thisFont, str2, WIDTH),300)
    
	gameClock.tick(40)
	pygame.display.flip()

