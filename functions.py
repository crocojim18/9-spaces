import linecache, pygame, struct

def centerText(font, text, screenWidth):
	newsc = screenWidth / 2
	newsc -= (font.size(text)[0])/2
	return newsc
	
def getText(line, filename="text.txt"):
	ret = linecache.getline(filename, line)
	ret = ret[:-1]
	return ret
	
class Screen:

	def __init__(self, x, y):
		self.width = x
		self.height = y
		icon = pygame.image.load("pics/icon.png")
		pygame.display.set_icon(icon)
		pygame.display.set_caption("9 Spaces")
		size = self.width, self.height
		self.screen = pygame.display.set_mode(size)
		self.fillColor = (0,0,0)

	def place(self, thing):
		self.screen.blit(thing.sprite, (thing.x, thing.y))
		thing.update_rect()

	def placeText(self, text_object, x, y):
		self.screen.blit(text_object, (x, y))

	def setFill(self, rgb):
		self.fillColor = rgb

	def fill(self):
		self.screen.fill(self.fillColor)
	
	def drawRect(self, rect, r, g, b):
		pygame.draw.rect(self.screen, (r, g, b), rect)

	def interpretMap(self, file):
		f = open(file, 'rb')
		hey = struct.unpack('3B', f.read(3))
		f.close()
		self.fillColor = hey