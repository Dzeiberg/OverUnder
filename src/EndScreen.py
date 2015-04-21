#Runs when the player reaches the congratulations screen

import pygame
from pygame.locals import *
import sys 

pygame.init()

screenSize = 1280, 720
white = 255, 255, 255
black = 0, 0, 0

class Image(pygame.sprite.Sprite):
    def __init__(self, color, filename, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, (size))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
def load():
    global screen
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Congratulations!")
    game = 0
    
    #initialize a button to take the player back to the main menu
    homeLoc = (30, 620)
    homeSize = (100, 100)
    homeButton = Image((255,216,63),"../resources/home.png", homeLoc, homeSize)
    
    while game == 0:
        
        EndScreen = Image((black), "../resources/EndScreen.png",(0,0), screenSize)
        
        # Put these images on the screen
        screen.blit(EndScreen.image, EndScreen)
        screen.blit(homeButton.image, homeButton)
        
        # check if the user wants to quit, by pressing the X button on the window or the escape key
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game = 1
                sys.exit()
            
            #if the home button is pressed, exit the EndScreen
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseLoc = pygame.mouse.get_pos()
                if (mouseLoc[0] > homeLoc[0] and mouseLoc[0] < (homeLoc[0] + homeSize[0])):
                    if (mouseLoc[1] > homeLoc[1] and mouseLoc[1] < (homeLoc[1] + homeSize[1])):
                        game = 1
                        
        pygame.display.update()