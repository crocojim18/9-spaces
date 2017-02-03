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
		thing.updateRect()

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
		
class Character:

	def __init__(self, thix, thiy):
		self.x = thix
		self.y = thiy
		self.forwardSprite = pygame.image.load("pics/ned.png")
		self.backSprite = pygame.image.load("pics/ned back.png")
		self.backWSprite = pygame.image.load("pics/ned back.png")#ned_walk_backward.gif")
		self.forwardWSprite = pygame.image.load("pics/ned.png")#_walk_forward.png")
		self.rightWSprite = pygame.image.load("pics/ned1.png")
		self.leftWSprite = pygame.transform.flip(self.rightWSprite, True, False)
		self.sprite = self.forwardSprite
		self.facing = 0
		self.walking = 0
	
	def updateRect(self):
		self.x = self.x
		
	def exist(self):
		upd = pygame.key.get_pressed()
		if upd[pygame.K_w]:
			self.y -= 4
			self.facing = 1
			self.walking |= 2
		if upd[pygame.K_a]:
			self.x -= 4
			self.walking |= 8;
		if upd[pygame.K_s]:
			self.y += 4
			self.facing = 0
			self.walking |= 1
		if upd[pygame.K_d]:
			self.x += 4
			self.walking |= 4
		self.updateSprite()
		self.walking = 0
		
	def updateSprite(self):
		if(self.walking == 0 and self.facing == 0): self.sprite = self.forwardSprite
		elif(self.walking == 0 and self.facing == 1): self.sprite = self.backSprite
		elif(self.walking > 7): self.sprite = self.leftWSprite
		elif(self.walking >= 4 and self.walking <= 7): self.sprite = self.rightWSprite
		elif(self.walking == 2 or self.walking == 3): self.sprite = self.backWSprite
		else: self.sprite = self.forwardWSprite