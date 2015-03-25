#Options Menu
import pygame
from pygame.locals import *
<<<<<<< HEAD
=======
import sys
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e

pygame.init()

class Image(pygame.sprite.Sprite):
<<<<<<< HEAD
    def __init__(self, color, filename, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(color) 
=======
    def __init__(self, filename, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        #self.image.set_colorkey(color) 
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
        self.image = pygame.transform.scale(self.image, (size))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

def load():
    
    pygame.display.set_caption('Options')

<<<<<<< HEAD
    screenSize = 1100, 700
=======
    screenSize = 1280, 720
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
    white = 255, 255, 255
    black = 0, 0, 0

    screen = pygame.display.set_mode(screenSize)
    
    titleLoc = (0, 0)
<<<<<<< HEAD
    title = Image((white), "../resources/optionsScreen.png", titleLoc, screenSize)
    
    backLoc = (50, 550)
    backSize = (128, 128)
    backButton = Image((black), "../resources/back.png", backLoc, backSize)
=======
    title = Image("../resources/optionsScreen.png", titleLoc, screenSize)
    
    backLoc = (50, 600)
    backSize = (120, 75)
    backButton = Image("../resources/back.png", backLoc, backSize)
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
    
    global game
    game = 0
    while game == 0 :
        
        screen.fill(white)
        
        screen.blit(title.image, title)
        screen.blit(backButton.image, backButton)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game = 1
<<<<<<< HEAD
=======
                sys.exit()
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseLoc = pygame.mouse.get_pos()
                if (mouseLoc[0] > backLoc[0] and mouseLoc[0] < (backLoc[0] + backSize[0])):
                    if (mouseLoc[1] > backLoc[1] and mouseLoc[1] < (backLoc[1] + backSize[1])):
                        game = 1
                        
        
        pygame.display.update()     
