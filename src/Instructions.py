#Instructions menu
import pygame, sys
from pygame.locals import *

pygame.init()

screenSize = 1280, 720
white = 255, 255, 255
black = 0, 0, 0

class Image(pygame.sprite.Sprite):
    def __init__(self, filename, location, size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(filename).convert()
        #self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, (size))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
def load ():
    global screen
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Instructions")
    game = 0
    
    backLoc = (50, 600)
    backSize = (120, 75)
    backButton = Image("../resources/back.png", backLoc, backSize)
    
    while game == 0:
        #displays the splash instructions screen
        instructions = Image("../resources/instructionsScreen.png",(0,0), screenSize)
        
        # Put these images on the screen
        screen.blit(instructions.image, instructions)
        screen.blit(backButton.image, backButton)
        # update the game window
        pygame.display.update()
        
        # check if the user wants to quit, by pressing the X button on the window or the escape key
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game = 1
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseLoc = pygame.mouse.get_pos()
                if (mouseLoc[0] > backLoc[0] and mouseLoc[0] < (backLoc[0] + backSize[0])):
                    if (mouseLoc[1] > backLoc[1] and mouseLoc[1] < (backLoc[1] + backSize[1])):
                        game = 1;
                                
        pygame.display.update()