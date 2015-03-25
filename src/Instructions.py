<<<<<<< HEAD
import pygame
=======
import pygame, sys
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
from pygame.locals import *

pygame.init()

<<<<<<< HEAD
screenSize = 1100, 700
=======
screenSize = 1280, 720
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
white = 255, 255, 255
black = 0, 0, 0

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
        

# a variable to control how long to run the game
def load ():
    global screen
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Instructions")
    game = 0
    
<<<<<<< HEAD
    backLoc = (50, 550)
    backSize = (128, 128)
    backButton = Image((black), "../resources/back.png", backLoc, backSize)
=======
    backLoc = (50, 600)
    backSize = (120, 75)
    backButton = Image("../resources/back.png", backLoc, backSize)
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
    
    while game == 0:

        screen.fill(white)
        
<<<<<<< HEAD
        instructions = Image((white),"../resources/instructionsScreen.png",(0,0), screenSize)
=======
        instructions = Image("../resources/instructionsScreen.png",(0,0), screenSize)
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
        
        # Put these images on the screen
        screen.blit(instructions.image, instructions)
        screen.blit(backButton.image, backButton)
        # update the game window
        pygame.display.update()
        
        # check if the user wants to quit, by pressing the X button on the window or the escape key
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
                        game = 1;
                        
                        
<<<<<<< HEAD
        pygame.display.update()

=======
        pygame.display.update()
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
