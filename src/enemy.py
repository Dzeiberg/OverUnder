
import pygame,main,Key, Gate, Level, math
class Enemy(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("../resources/enemy/player.png").convert()
		self.image.set_colorkey(pygame.Color("white"))
		self.leftImages = []
		self.rightImages = []
		self.leftCrouchImages = []
		self.rightCrouchImages = []
		self.leftCrouchIDX = 0
		self.rightCrouchIDX = 0
		self.leftIDX = 0
		self.rightIDX = 0
		self.leftImages.append(pygame.image.load("../resources/enemy/knightLeft1.png").convert())
		self.leftImages.append(pygame.image.load("../resources/enemy/knightLeft3.png").convert())
		self.leftImages.append(pygame.image.load("../resources/enemy/knightLeft2.png").convert())
		self.rightImages.append(pygame.image.load("../resources/enemy/knightRight1.png").convert())
		self.rightImages.append(pygame.image.load("../resources/enemy/knightRight3.png").convert())
		self.rightImages.append(pygame.image.load("../resources/enemy/knightRight2.png").convert())
		self.leftCrouchImages.append(pygame.image.load("../resources/enemy/knightLeft1Crouch.png").convert())
		self.leftCrouchImages.append(pygame.image.load("../resources/enemy/knightLeft3Crouch.png").convert())
		self.leftCrouchImages.append(pygame.image.load("../resources/enemy/knightLeft2Crouch.png").convert())
		self.rightCrouchImages.append(pygame.image.load("../resources/enemy/knightRight1Crouch.png").convert())
		self.rightCrouchImages.append(pygame.image.load("../resources/enemy/knightRight3Crouch.png").convert())
		self.rightCrouchImages.append(pygame.image.load("../resources/enemy/knightRight2Crouch.png").convert())
		self.width = 40
		self.height = 80
		self.image = pygame.transform.scale(self.image, (self.width, self.height))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speedX = 0
		self.speedY = 0 
		self.onGround = True
		self.disabled = True
		self.crouching = False

	def update(self, platform_list, players):
		levelComplete = False
		dead1 = False
		dead2 = False
		self.image.set_colorkey(pygame.Color("white"))
		#calculates new y speed
		self.calcGrav()
		self.getSpeed(players[0],players[1])
		if self.disabled:
			self.speedX = 0
			if self.onGround == True:
				self.speedY = 0
			self.disabled = False
		#moves in x direction
		self.rect.x += self.speedX
 
		#checks if the player collides with anything
		collision_list = pygame.sprite.spritecollide(self, platform_list, False)
		if self.crouching:
			self.standUp(platform_list)
		for block in collision_list:
			if isinstance(block,Level.Spike):
				if self.speedX > 0:
					self.rect.right = block.rect.left
				#if moving right, place the player to the left of the platform
				elif self.speedX < 0:
					self.rect.left = block.rect.right 
				#if not noSound:
				 #   self.painSound.play()
			#if it's a platform
			elif isinstance(block, Level.Platform):
				#if moving left, place the player to the right of the platform
				if self.speedX > 0:
					self.rect.right = block.rect.left
				#if moving right, place the player to the left of the platform
				elif self.speedX < 0:
					self.rect.left = block.rect.right
				self.crouch()
			#if it's a gate
			elif isinstance(block, Gate.gate):
				self.speedX *= -1 
		#checks for collision with the other player, similar to a platform
		if pygame.sprite.collide_rect(self, players[0]):
			dead1=True
			'''
			if self.speedX > 0:
				self.rect.right = players[0].rect.left
			elif self.speedX < 0:
				self.rect.left = players[0].rect.right
			'''
		if pygame.sprite.collide_rect(self, players[1]):
			dead2 = True
			'''
			if self.speedX > 0:
				self.rect.right = players[1].rect.left
			elif self.speedX < 0:
				self.rect.left = players[1].rect.right
			'''
		#moves in y direction    
		self.rect.y += self.speedY
 
		self.onGround = False
 
		#checks for collisions
		collision_list = pygame.sprite.spritecollide(self, platform_list, False)
		for block in collision_list:        
			#just like collisions with x direction
			if isinstance(block, Level.Platform):
				#If the player is under a wall, stop the player's and the wall's movement

				if isinstance(block, Level.Wall) and self.rect.y > block.rect.y:
					block.rect.bottom = self.rect.top + 1
					block.disabled = True
					self.disabled = True
				elif isinstance(block,Level.Spike):
					if self.speedY > 0:
						self.rect.bottom = block.rect.top
					#if moving right, place the player to the left of the platform
					elif self.speedX < 0:
						self.rect.bottom = block.rect.top 
					dead = True   
				else:
					if self.speedY > 0:
						self.rect.bottom = block.rect.top
						self.onGround = True
					elif self.speedY < 0:
						self.rect.top = block.rect.bottom
				
				# Stop moving vertically if we hit a platform
				self.speedY = 0
					
			#if isinstance(block,Gate.gate):
				#not sure what to do if the enemy jumps into the gate
		if pygame.sprite.collide_rect(self, players[0]):
			dead1 = True
			'''
			if self.speedY > 0:
				self.rect.bottom = players[0].rect.top
				if players[0].onGround:
					self.onGround = True
			elif self.speedY < 0:
				self.rect.top = players[0].rect.bottom
			self.speedY = 0
			'''
		elif pygame.sprite.collide_rect(self, players[0]):
			dead2 = True
			'''
			if self.speedY > 0:
				self.rect.bottom = players[1].rect.top
				if players[1].onGround:
					self.onGround = True
			elif self.speedY < 0:
				self.rect.top = players[1].rect.bottom
			self.speedY = 0
			'''
		self.animate()
		#returns True if the player has a key and is at the gate, false otherwise
		return [dead1,dead2]   		
	def calcGrav(self):
		#if they're not on the ground
		if self.speedY == 0:
			self.speedY = 1
		#acceleration for gravity
		else:
			self.speedY += .35
 
		#checks if they are past the bottom of the screen
		#not really needed since platforms will cover the bottom of the screen
		if self.rect.y >= main.SCREEN_HEIGHT - self.rect.height and self.speedY >= 0:
			self.speedY = 0
			self.rect.y = main.SCREEN_HEIGHT - self.rect.height
			self.onGround = True
	
	def crouch(self):
		#create new sprite for crouching player
		if not self.crouching:
			pygame.sprite.Sprite.__init__(self)
			if self.speedX > 0:
				self.image=pygame.image.load("../resources/enemy/knightRight1Crouch.png").convert()
			elif self.speedX < 0:
				self.image=pygame.image.load("../resources/enemy/knightLeft1Crouch.png").convert()
			else:
				self.image = pygame.image.load("../resources/enemy/playerCrouch.png").convert()
			self.image.set_colorkey(pygame.Color("white"))
			self.height = 60  
			#stores previous location
			x = self.rect.x
			y = self.rect.y   
			self.image = pygame.transform.scale(self.image, (self.width, self.height))
			#new location
			self.rect = self.image.get_rect()
			self.rect.x = x
			self.rect.y = y + 20
			self.crouching = True       

	def standUp(self, platform_list):
		#create new sprite for standing up
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("../resources/enemy/player.png").convert()
		self.image.set_colorkey(pygame.Color("white"))


		self.height = 80
		
		#storing old location
		x = self.rect.x
		y = self.rect.y
		
		self.image = pygame.transform.scale(self.image, (self.width, self.height))

		#updating new location
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y - 20
		
		self.crouching = False
		
		#if standing up makes you collide with another platform, go back to crouching
		collision_list = pygame.sprite.spritecollide(self, platform_list, False)
		
		for block in collision_list:
			if isinstance(block, Level.Platform):
				self.crouch()
				break
		
	def jump(self):
		self.image.set_colorkey(pygame.Color("white"))
		if self.onGround:
			self.speedY = -12 #+ (4.5 * (self.playerNum - 1)) #different values for different players
			self.onGround = False
			#PLAYSOUND
			#self.jumpSound.play()
 
	def draw(self, screen):
		self.image.set_colorkey(pygame.Color("white"))
		screen.blit(self.image, (self.rect.x, self.rect.y))

	def go_left(self):
		self.image.set_colorkey(pygame.Color("white"))
		self.speedX = -6
 
	def go_right(self):
		self.image.set_colorkey(pygame.Color("white"))
		self.speedX = 6
 
	def stop(self):
		self.image.set_colorkey(pygame.Color("white"))
		self.speedX = 0        
	
	def animate(self):
		self.image.set_colorkey(pygame.Color("white"))
		if self.speedX < 0 and self.speedY == 0:
			#moving left
			if not self.crouching:
				self.leftIDX = (self.leftIDX+1)%3
				self.image = self.leftImages[self.leftIDX]
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				self.image.set_colorkey(pygame.Color("white"))

				#self.rect = self.image.get_rect()
			else:
				self.leftCrouchIDX = (self.leftCrouchIDX+1)%3
				self.image = self.leftCrouchImages[self.leftCrouchIDX]
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				self.image.set_colorkey(pygame.Color("white"))
				#self.rect = self.image.get_rect()
		elif self.speedX > 0 and self.speedY == 0:
			#moving right
			if not self.crouching:
				self.rightIDX = (self.rightIDX+1)%3
				self.image = self.rightImages[self.rightIDX]
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				self.image.set_colorkey(pygame.Color("white"))
				#self.rect = self.image.get_rect()
			else:
				self.rightCrouchIDX = (self.rightCrouchIDX+1)%3
				self.image = self.rightCrouchImages[self.rightCrouchIDX]
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				self.image.set_colorkey(pygame.Color("white"))
				#self.rect = self.image.get_rect()
		elif self.speedX < 0 and self.speedY != 0:
			if not self.crouching:
				self.leftIDX = 0
				self.image = self.leftImages[self.leftIDX]
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				self.image.set_colorkey(pygame.Color("white"))
			elif self.crouching:
				self.leftCrouchIDX = 0
				self.image = self.leftCrouchImages[self.leftCrouchIDX]
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				self.image.set_colorkey(pygame.Color("white"))
		elif self.speedX > 0 and self.speedY != 0:
			if not self.crouching:
				self.rightIDX = 0
				self.image = self.rightImages[self.rightIDX]
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				self.image.set_colorkey(pygame.Color("white"))
			elif self.crouching:
				self.rightCrouchIDX = 0
				self.image = self.rightCrouchImages[self.rightCrouchIDX]
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				self.image.set_colorkey(pygame.Color("white"))
	def getSpeed(self,playerOne,playerTwo):
		d1 = math.sqrt(math.pow(self.rect.x-playerOne.rect.x,2)+math.pow(self.rect.y-playerOne.rect.y,2))
		d2 = math.sqrt(math.pow(self.rect.x-playerTwo.rect.x,2)+math.pow(self.rect.y-playerTwo.rect.y,2))
		if abs(d1) < abs(d2):
			#print "P1"
			#go towards playerOne
			if self.rect.x-playerOne.rect.x < 0:
				self.speedX = 1
			else:
				self.speedX = -1
			
		elif abs(d1) > abs(d2):
			#print "P2"
			#go towards playerTwo
			if self.rect.x-playerTwo.rect.x < 0:
				self.speedX = 1
			else:
				self.speedX = -1
		else:
			#print "IDK"
			#otherwise just go forward
			self.speedX = 1

		
