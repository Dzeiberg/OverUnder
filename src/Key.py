import pygame

class key(pygame.sprite.Sprite):
	def __init__(self,location):
		pygame.sprite.Sprite.__init__(self)
		# call parent class constructorpygame.sprite.Sprite.__init__(self)
		# load the image, converting the pixel format for optimization
		self.image = pygame.image.load("../resources/key.png").convert()
		# make 'color' transparent on the image
<<<<<<< HEAD
		self.image.set_colorkey((102,255,255)) 
		# resize image to 40x40 px
		self.image = pygame.transform.scale(self.image, (20,20))    
=======
		self.image.set_colorkey((0,0,0)) 
		# resize image to 40x40 px
		self.image = pygame.transform.scale(self.image, (40,20))    
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
		# set the rectangle defined for this image for collision detection
		self.rect = self.image.get_rect()
		# position the image
		self.rect.x = location[0]
		self.rect.y = location[1]
