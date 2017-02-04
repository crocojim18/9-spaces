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
		pygame.display.set_caption(getText(2))
		size = self.width, self.height
		self.screen = pygame.display.set_mode(size)
		self.fillColor = (0,0,0)
		self.loadedTiles = []
		self.tileList = []

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

	def interpretColor(self, file):
		f = open(file, 'rb')
		hey = struct.unpack('3B', f.read(3))
		f.close()
		self.fillColor = hey
		
	def drawMap(self):
		for i in len(tileList):
			self.screen.blit(loadedTiles[tileList[i][0]], tileList[i][1])
			#such that loadedTiles consists of cells that have a sprite index, and (x,y)

	def interpretMap(self,file=1):
		inp = open('maps/'+str(file)+'.map', 'rb')
		tempStr = "l"
		while len(tempStr) > 0:
			tempStr = inp.read(1)
			if tempStr != "":
				stri = str(struct.unpack('B', tempStr)[0])
				print "pics/"+stri+".png"
				#pygame.image.load("pics/"+stri+".png")
		inp.close()

class Character:

	def __init__(self, thix, thiy):
		self.x = thix
		self.y = thiy
		self.forwardSprite = pygame.image.load("pics/ned.png")
		self.backSprite = pygame.image.load("pics/ned back.png")
		self.backWSprite = [pygame.image.load("pics/nedWB1.png"), pygame.image.load("pics/nedWB2.png")]
		self.forwardWSprite = [pygame.image.load("pics/nedWF1.png"), pygame.image.load("pics/nedWF2.png")]
		self.rightWSprite = [pygame.image.load("pics/ned1.png"),pygame.image.load("pics/ned2.png"),pygame.image.load("pics/ned3.png")]
		self.leftWSprite = [pygame.transform.flip(self.rightWSprite[0], True, False),
							pygame.transform.flip(self.rightWSprite[1], True, False),
							pygame.transform.flip(self.rightWSprite[2], True, False)]
		self.sprite = self.forwardSprite
		self.facing = 0
		self.walking = 0
		self.speed = 4
		self.frame = 0
		self.toFrom = True
		self.frameTime = pygame.time.get_ticks();
	
	def updateRect(self):
		self.x = self.x
		
	def exist(self):
		upd = pygame.key.get_pressed()
		if upd[pygame.K_w]:
			self.y -= self.speed
			self.facing = 1
			self.walking |= 2
		if upd[pygame.K_a]:
			self.x -= self.speed
			self.walking |= 8;
		if upd[pygame.K_s]:
			self.y += self.speed
			self.facing = 0
			self.walking |= 1
		if upd[pygame.K_d]:
			self.x += self.speed
			self.walking |= 4
		self.updateSprite()
		self.walking = 0
		
	def twoWayFrame(self):
		if(pygame.time.get_ticks()-self.frameTime>250):
			if(self.frame==0): self.frame = 1
			else: self.frame = 0
			self.frameTime = pygame.time.get_ticks()

	def threeWayFrame(self):
		if(pygame.time.get_ticks()-self.frameTime>250):
			if(self.frame==0): self.frame = 1
			elif(self.frame==1 and self.toFrom): self.frame = 2
			elif(self.frame==1 and not self.toFrom):
				self.frame = 0
				self.toFrom = True
			else:
				self.frame = 1
				self.toFrom = False
			self.frameTime = pygame.time.get_ticks()

	def updateSprite(self):
		if(self.walking == 0 and self.facing == 0):
			self.sprite = self.forwardSprite
		elif(self.walking == 0 and self.facing == 1):
			self.sprite = self.backSprite
		elif(self.walking > 7):
			self.threeWayFrame()
			self.sprite = self.leftWSprite[self.frame]
		elif(self.walking >= 4 and self.walking <= 7):
			self.threeWayFrame()
			self.sprite = self.rightWSprite[self.frame]
		elif(self.walking == 2 or self.walking == 3):
			self.twoWayFrame()
			if(self.frame>1): self.frame = 0
			self.sprite = self.backWSprite[self.frame]
		else:
			self.twoWayFrame()
			if(self.frame>1): self.frame = 0
			self.sprite = self.forwardWSprite[self.frame]