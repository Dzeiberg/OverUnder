# Over Under Main Menu
import pygame, Options, Instructions, main, sys
from pygame.locals import * 

#initialize the screen
pygame.init()

screenSize= 1280, 720
white= 255,255, 255
blue = 102, 255, 255

#sets the size of the screen
screen = pygame.display.set_mode(screenSize)

#Image class to be used with menu buttons
class Image(pygame.sprite.Sprite):
    def __init__(self, color, filename, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
    
    #called when a button is clicked on
    def mouseClick(self, buttonSize, location, file, level_num, muted):
        #get the mouse location
        mouseLoc = pygame.mouse.get_pos()
        
        #if the location of the mouse click was on the button
        if (mouseLoc[0] > location[0] and mouseLoc[0] < (location[0] + buttonSize[0])):
            if (mouseLoc[1] > location[1] and mouseLoc[1] < (location[1] + buttonSize[1])):
                #for the Resume button
                if(file == 2):
                    #load the game starting from the stored level number
                    [level_num, muted] = main.load(level_num, muted)
                #for the Start button
                elif(file == 3):
                    #load the game starting from level one
                    [level_num, muted] = main.load(1, muted)
                else:
                    #load the respective screen
                    file.load()
                    
        return [level_num, muted]

def menu(level_num, muted):
    #Setting the caption
    pygame.display.set_caption("Main Menu")
 
    #Setting the current level number
    current_level_num = level_num
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
    
    bg = Image((white), "../resources/homeScreen5.png", bgLoc, bgSize)
    start = Image((white), "../resources/start.png", startLoc, startSize)
    options = Image((white), "../resources/options.png", optionsLoc, optionsSize)
    instructions = Image((white), "../resources/instructions.png", instructionsLoc, instructionsSize)
    resume = Image((white), "../resources/resumeButton.png", resumeLoc, resumeSize)
    
    #loop for the main menu, the "game" variables acts as the state of the menu
    game = 0
    while game == 0:
        #printing the images to the screen
        screen.blit(bg.image, bg)
        screen.blit(start.image, start)
        screen.blit(options.image, options)
        screen.blit(instructions.image, instructions)
        screen.blit(resume.image, resume)
        
        pygame.display.update()
        mouseClicked = False
        
        for event in pygame.event.get():
            #user quits the game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game = 1
                sys.exit()
            #if the mouse was clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked = True
               
        #used to go to other screens when the mouse is clicked
        if (mouseClicked == True):
            [current_level_num, muted] = Image.mouseClick(start, startSize, startLoc, 3, current_level_num, muted) 
            Image.mouseClick(options, optionsSize, optionsLoc, Options, current_level_num, muted) 
            Image.mouseClick(instructions, instructionsSize, instructionsLoc, Instructions, current_level_num, muted)
            [current_level_num, muted] = Image.mouseClick(resume, resumeSize, resumeLoc, 2, current_level_num, muted) 
            
            mouseClicked = False

#Start at the menu screen, with level number at 1 and with sound on        
menu(1, False)
