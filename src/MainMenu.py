# Over Under Main Menu

<<<<<<< HEAD
import pygame
from pygame.locals import * 
import Options, Instructions, main, EndScreen

pygame.init()

#Setting the caption
pygame.display.set_caption("Main Menu")

screenSize= 1100, 700
=======
import pygame, os, Options, Instructions, main, sys
from pygame.locals import * 


pygame.init()

screenSize= 1280, 720
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
white= 255,255, 255
blue = 102, 255, 255

#sets the size of the screen
screen = pygame.display.set_mode(screenSize)

class Image(pygame.sprite.Sprite):
    def __init__(self, color, filename, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
<<<<<<< HEAD
    def mouseClick(self, buttonSize, location, file):
=======
    def mouseClick(self, buttonSize, location, file, level_num):
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
        
        mouseLoc = pygame.mouse.get_pos()
        
        if (mouseLoc[0] > location[0] and mouseLoc[0] < (location[0] + buttonSize[0])):
            if (mouseLoc[1] > location[1] and mouseLoc[1] < (location[1] + buttonSize[1])):
<<<<<<< HEAD
                level = file.load()
                
                if (level == 2 and file == main):
                    EndScreen.load()
                    
#bg_music = pygame.mixer.music
#bg_music.load("bgmusic.mp3")
                
def menu():
 
    #setting variables for buttons
    startLoc = (50, 50)
    startSize = (200, 75)
    bgLoc = (-5,-5)
    bgSize = (1294, 788)
    optionsLoc = (50, 175)
    optionsSize = (316, 80)
    instructionsLoc = (50, 300)
    instructionsSize = (512, 80)
=======
                #for the resume button
                if(file == 2):
                    #do something to resume to whatever level
                    main.load(level_num)
                elif(file == 3):
                    main.load(1)
                else:
                    file.load()
                
                    

#bg_music = pygame.mixer.music
#bg_music.load('FuelShip.wav')
#bg_music.play(-1, 0.0)

def menu(level_num):
    #Setting the caption
    pygame.display.set_caption("Main Menu")
 
    current_level_num = level_num
    #Setting the current level number
    if level_num == 0:
        current_level_num = 1
    else:
        current_level_num = level_num
 
    #setting variables for buttons
    startLoc = (50, 50)
    startSize = (200, 80)
    bgLoc = (-5,-5)
    bgSize = (1294, 788)
    optionsLoc = (50, 300)
    optionsSize = (316, 80)
    instructionsLoc = (50, 425)
    instructionsSize = (512, 80)
    resumeLoc = (50, 175)
    resumeSize = (355, 80)
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
    
    bg = Image((white), "../resources/homeScreen5.png", bgLoc, bgSize)
    start = Image((white), "../resources/start.png", startLoc, startSize)
    options = Image((white), "../resources/options.png", optionsLoc, optionsSize)
    instructions = Image((white), "../resources/instructions.png", instructionsLoc, instructionsSize)
<<<<<<< HEAD
=======
    resume = Image((white), "../resources/resumeButton.png", resumeLoc, resumeSize)
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
    
    game = 0
    
    while game == 0:
        screen.fill(blue) 
        
        #printing the images to the screen
        screen.blit(bg.image, bg)
        screen.blit(start.image, start)
        screen.blit(options.image, options)
        screen.blit(instructions.image, instructions)
<<<<<<< HEAD
=======
        screen.blit(resume.image, resume)
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game = 1
<<<<<<< HEAD
=======
                sys.exit()
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
            if event.type == pygame.MOUSEBUTTONDOWN:
                game = 2
               
    #used to go to other screens
    if (game == 2):
<<<<<<< HEAD
        Image.mouseClick(start, startSize, startLoc, main) 
        Image.mouseClick(options, optionsSize, optionsLoc, Options) 
        Image.mouseClick(instructions, instructionsSize, instructionsLoc, Instructions)
        menu()
        
menu()
=======
        Image.mouseClick(start, startSize, startLoc, 3, current_level_num) 
        Image.mouseClick(options, optionsSize, optionsLoc, Options, current_level_num) 
        Image.mouseClick(instructions, instructionsSize, instructionsLoc, Instructions, current_level_num)
        Image.mouseClick(resume, resumeSize, resumeLoc, 2 ,current_level_num) 
        menu(current_level_num)
        
menu(1)
>>>>>>> 631219a937320816d42fb5903b27e2c45a050a7e
