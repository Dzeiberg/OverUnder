#Options Menu
import pygame,sys,main
from pygame.locals import *


pygame.init()

class Image(pygame.sprite.Sprite):
    def __init__(self, filename, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        #self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, (size))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        self.location = location
        self.size = size
    def mouseClick(self):
        mouseLoc = pygame.mouse.get_pos()
        
        if (mouseLoc[0] > self.location[0] and mouseLoc[0] < (self.location[0] + self.size[0])):
            if (mouseLoc[1] > self.location[1] and mouseLoc[1] < (self.location[1] + self.size[1])):
                return True
        return False

def load():
    
    pygame.display.set_caption('Options')

    screenSize = 1280, 720
    white = 255, 255, 255
    black = 0, 0, 0

    screen = pygame.display.set_mode(screenSize)

    titleLoc = (0, 0)
    title = Image("../resources/optionsScreen.png", titleLoc, screenSize)
    
    backLoc = (50, 600)
    backSize = (120, 75)
    backButton = Image("../resources/back.png", backLoc, backSize)

    squareSize = (75,75)
    redLoc = (350,290)
    orangeLoc = (440,290)
    yellowLoc = (525,290)
    greenLoc = (610,290)
    blueLoc = (695,290)
    purpleLoc = (780,290)
    redLoc2 = (350,460)
    orangeLoc2 = (440,460)
    yellowLoc2 = (525,460)
    greenLoc2 = (610,460)
    blueLoc2 = (695,460)
    purpleLoc2 = (780,460)
    red1 = Image("../resources/redSquare.png",redLoc,squareSize)
    orange1 = Image("../resources/orangeSquare.png",orangeLoc,squareSize)
    yellow1 = Image("../resources/yellowSquare.png",yellowLoc,squareSize)
    green1 = Image("../resources/greenSquare.png",greenLoc,squareSize)
    blue1 = Image("../resources/blueSquare.png",blueLoc,squareSize)
    purple1 = Image("../resources/purpleSquare.png",purpleLoc,squareSize)
    red2 = Image("../resources/redSquare.png",redLoc2,squareSize)
    orange2 = Image("../resources/orangeSquare.png",orangeLoc2,squareSize)
    yellow2 = Image("../resources/yellowSquare.png",yellowLoc2,squareSize)
    green2 = Image("../resources/greenSquare.png",greenLoc2,squareSize)
    blue2 = Image("../resources/blueSquare.png",blueLoc2,squareSize)
    purple2 = Image("../resources/purpleSquare.png",purpleLoc2,squareSize)

    
    global game
    game = 0
    while game == 0 :
        
        screen.fill(white)
        
        screen.blit(title.image, title)
        screen.blit(backButton.image, backButton)
        screen.blit(red1.image,red1)
        screen.blit(orange1.image,orange1)
        screen.blit(yellow1.image,yellow1)
        screen.blit(green1.image,green1)
        screen.blit(blue1.image,blue1)
        screen.blit(purple1.image,purple1)
        screen.blit(red2.image,red2)
        screen.blit(orange2.image,orange2)
        screen.blit(yellow2.image,yellow2)
        screen.blit(green2.image,green2)
        screen.blit(blue2.image,blue2)
        screen.blit(purple2.image,purple2)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game = 1
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseLoc = pygame.mouse.get_pos()
                if (mouseLoc[0] > backLoc[0] and mouseLoc[0] < (backLoc[0] + backSize[0])):
                    if (mouseLoc[1] > backLoc[1] and mouseLoc[1] < (backLoc[1] + backSize[1])):
                        game = 1
                if red1.mouseClick():
                    main.p1Color="red"
                elif orange1.mouseClick():
                    main.p1Color="orange"
                elif yellow1.mouseClick():
                    main.p1Color="yellow"
                elif green1.mouseClick():
                    main.p1Color="green"
                elif blue1.mouseClick():
                    main.p1Color="blue"
                elif purple1.mouseClick():
                    main.p1Color="purple"
                elif red2.mouseClick():
                    main.p2Color="red"
                elif orange2.mouseClick():
                    main.p2Color="orange"
                elif yellow2.mouseClick():
                    main.p2Color="yellow"
                elif green2.mouseClick():
                    main.p2Color="green"
                elif blue2.mouseClick():
                    main.p2Color="blue"
                elif purple2.mouseClick():
                    main.p2Color="purple" 
                        
        
        pygame.display.update()     
