#.py file for the level class

import pygame, Key, Gate

class Level(object):
    platform_list = None
            
    def __init__(self, levelNum):
        self.platform_list = pygame.sprite.Group()
        self.button_list = []
        x = 0
        y = 0
        
        #level maps for each level
        #D = dirt
        #P = dirt with grass on top
        #G = gate
        #K = key
        #S = spike
        
        if levelNum == 1:
            levelMap = [
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                              K                                 ",
                "                   PPPPPPPPPPPPPPPPPPPPPPPPP                    ",
                "                   DDDDDDDDDDDDDDDDDDDDDDDDD                    ",
                "                   DDDDDDDDDDDDDDDDDDDDDDDDD                    ",
                "                   DDDDDDDDDDDDDDDDDDDDDDDDD                    ",
                "                   DDDDDDDDDDDDDDDDDDDDDDDDD                    ",
                "                   DDDDDDDDDDDDDDDDDDDDDDDDD                    ",
                "                                                                ",
                "                                                                ",
                "                              K                               G ",
                "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]
        
        elif levelNum == 2:
            levelMap = [
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                    K                        K                G ",
                "PPPPPPPPPPPPPPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPP PPPPPPPPPPPPPPPPPP"]
        
        elif levelNum == 3:
            levelMap = [
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                              K                 ",
                "                                         PPPPP PPPPP            ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "          PPPP                                                  ",
                "          DDDD       PPPPP                                      ",
                "          DDDD                                                  ",
                "          DDDD                                                  ",
                "          DDDD         K                                      G ",
                "PPPPPPPPPPDDDDPPPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]        
                
        
        elif levelNum == 4:
            levelMap = [
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                        K                       ",
                "PPPPPPPPPPPPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP         ",
                "                                                      D         ",
                "                                                      D         ",
                "                                                      D         ",
                "                                                      D         ",
                "                                                      D         ",
                "                                                      D         ",
                "                                                      D         ",
                "                                                      D         ",
                "                                                      D         ",
                "                                                      D         ",
                "                                                      D         ",
                "                                                                ",
                "                                                                ",
                "                                        K                     G ",
                "PPPPPPPPPPPPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]
            
        elif levelNum == 5:
            levelMap = [
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                   K                            ",
                "                          PPPPPPPPPPPPPPPPPP                    ",
                "                          DDDDDDDDDDDDDDDDDD                    ",
                "                          DDDDDDDDDDDDDDDDDD  SS                ",
                "                                              DD                ",
                "                                              DD                ",
                "                                              DD                ",
                "                                   K          DD              G ",
                "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPDDPPPPPPPPPPPPPPPP"]

        elif levelNum == 6:
            levelMap = [
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                K                               ",
                "                           PPPPP PPPP                           ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "              PPPPPPPP                                          ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "          PPPPPPPP PPP                                          ",
                "          DDDDDDDDDDDD                                          ",
                "          DDDD                                                  ",
                "          DDDD                                                  ",
                "          DDDD   K                                            G ",
                "PPPPPPPPP DDDDPPP PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]
            
        elif levelNum == 7:
            levelMap = [
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "            PPPP                                                ",
                "            DDDD                                                ",
                "            DDDD                                                ",
                "                                                    PPPP        ",
                "                                                    DDDD        ",
                "                                                    DDDD        ",
                "        PPPPPPPPPPPPPPPPPPPPPP     PPPPPPPPPPPPPPPPPDDDD        ",
                "                             D     D                            ",
                "                             D     D                            ",
                "                             D   G D                            ",
                "PPPP                         DPPPPPD                        PPPP",
                "                                                                ",
                "                                                                ",
                "                     P   K           K    P                     ",
                "PPPPPPPP             DPPPPPPPPPPPPPPPPPPPPD                     ",
                "                        D              D                        ",
                "                        D              D                        ",
                "PPPPPPPPPPPP            D              D                  PPPPPP",
                "          DD            D              D                        ",
                "          DD       PPPPPD              DPP                      ",
                "          DD       D                     D                      ",
                "          DD       D                     D                      ",
                "          DD       D                     D                      ",
                "          DD  PPPPPD                     DPPPPPPPP              ",
                "              D                                  D              ",
                "              D                                  D              ",
                "              D                                  D              ",
                "        PPPPPPD                                  D              ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                        SSSSSSSSSSSSSSSS                        ",
                "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]
                
            
        elif levelNum == 8:
            levelMap = [
                "                                                   D            ",
                "                                                   D            ",
                "                                                   D            ",
                "                               D                   D            ",
                "                               D                   D            ",
                "                               D       PPPPPP      D            ",
                "                               D            D      D            ",
                "                               D            D      D            ",
                "                               D            D      D            ",
                "                               D            D      D            ",
                "                               D            D      D K          ",
                "              PPPPPPPPPPP      D            D      DPPPP        ",
                "                        D      D            DPP                 ",
                "                        D      D            DDD                 ",
                "                        D      D            DDD                 ",
                "                        D      D            DDD                 ",
                "             PPPPPPPPPP D      DPPPP        DDDPPPPPPPPPPPPPPPPP",
                "                        D                   D                   ",
                "                        D                   D                   ",
                "                        D                   D                   ",
                "                        D                   D                   ",
                "       PPPPPPPPPPPP     DPPPPPPPPPPPPPPPPPPPD                   ",
                "       DDDDDDDDDDDD                                        PP PP",
                "       D                                                        ",
                "       D                                                        ",
                "       D                                                        ",
                "       D                                                        ",
                "       D                                                        ",
                "       D                                                        ",
                "       DPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                     ",
                "       DDDDDDDD      DDDDDDDDDDDDDDDDDDDDDDPPPP                 ",
                "       DDDDDDDD                              DDPPPP             ",
                "                                                                ",
                "                                                                ",
                "                   PPPPPPPPP      K                     PP    G ",
                "PPPPPPPPPPPPPPPPPPPDDDDDDDDDPPPPPPP PPPPP PPPPPPPPPPPPPPDDPPPPPP"]
            
        elif levelNum == 9:
            levelMap = [
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                                                ",
                "                                         K                      ",
                "                  PPPPPPPPPPP PP PP PPPPPPPPPPP                 ",
                "                  D                           D                 ",
                "                  D                           D                 ",
                "                  D                           D                 ",
                "                  D                           D                 ",
                "                  D                           D                 ",
                "                  D                           D                 ",
                "                  D                           D                 ",
                "                  D                           D                 ",
                "                  D                           D                 ",
                "              PPPPD                           DPPPP             ",
                "              D                                   D             ",
                "              D                                   D             ",
                "              D                                   D             ",
                "              D                                   D             ",
                "              D                                   D             ",
                "              D                                   D             ",
                "              D                                   D             ",
                "              D                                   D             ",
                "              D        S SSSSSSS SSSSSSS S        D             ",
                "          PPPPDPPPP    D DDDDDDD DDDDDDD D    PPPPDPPPP         ",
                "                       D DDDDDDD DDDDDDD D                      ",
                "                       D DDDDDDD DDDDDDD D                      ",
                "                       DDDDDDDDDDDDDDDDDDD        K           G ",
                "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]

        
        #code that runs through the level map
        for row in levelMap:
                for col in row:
                    #create a platform
                    if col == "P":
                        p = Platform(x, y)
                        self.platform_list.add(p)
                    #create a key
                    elif col =="K":
                        k = Key.key((x,y))
                        self.platform_list.add(k)
                    #create a platform with a different image
                    elif col =="D":
                        d = Dirt(x, y)
                        self.platform_list.add(d)
                    #create a gate
                    elif col =="G":
                        g = Gate.gate((x,y))
                        self.platform_list.add(g)
                    #create a spike
                    elif col =="S":
                        s=Spike(x,y,20,20)
                        self.platform_list.add(s)
                    x += 20
                y += 20
                x = 0
        
        #create buttons and walls at certain locations
        #specific to levels
        if levelNum == 2:
            self.wall = Wall(200, 200, 630, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(400, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(600, 500, 700, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(900, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
        elif levelNum == 3:
            self.wall = Wall(700, 500, 700, 200, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(460, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(660, 660, 700, 160, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(920, 180, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            
        elif levelNum == 4:
            self.wall = Wall(580, 180, 400, 120, 1)
            self.platform_list.add(self.wall)
            
            self.button = Button(360, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(580, 560, 700, 140, 1)
            self.platform_list.add(self.wall)
            
            self.button = Button(360, 400, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
        elif levelNum == 6:
            self.wall = Wall(200, 400, 600, 300, 2)
            self.platform_list.add(self.wall)
            
            self.button = Button(180, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(540, 200, 420, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(360, 600, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(440, 450, 700, 220, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(640, 420, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(720, 220, 420, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(340, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
        elif levelNum == 8:
            self.wall = Wall(1140, 200, 280, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(700, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(740, 300, 360, 40, 10)#fix
            self.platform_list.add(self.wall)
            
            self.button = Button(820, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(1020, 600, 680, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(460, 320, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(220, 300, 420, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(1220, 440, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
        elif levelNum == 9:
            self.wall = Wall(480, 660, 680, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(580, 220, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(640, 660, 680, 100, 10)#fix
            self.platform_list.add(self.wall)
            
            self.button = Button(640, 220, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(800, 660, 680, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(700, 220, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)  
        
        #create messages for every level
        self.message = ""
        if levelNum == 1:
            self.message = "Each player can grab one key. Collect them both to unlock the gate!"
        elif levelNum == 2:
            self.message = "You're both doing great! In this level, stand on the buttons to move the walls!"
        elif levelNum == 3:
            self.message = "Nice! Click the refresh button in the corner if you want to restart the level."
        elif levelNum == 4:
            self.message = "Keep up the good work! Make sure to talk to your partner too!"
        elif levelNum == 5:
            self.message = "Great cooperation! Be careful of the spikes and the monster in this level!"
        elif levelNum == 6:
            self.message = "That was amazing! For this level, make sure to think before doing!"
        elif levelNum == 7:
            self.message = "Good job! Here's a hint for this level: the monster chases the closest player!"
        elif levelNum == 8:
            self.message = "Amazing teamwork! You're almost done with the game!"
        elif levelNum == 9:
            self.message = "It's the final level! Timing is everything, so make sure to talk to each other!"
        
        #text signaling the current level
        self.levelText = "Level " + str(levelNum)
        
    #updates every button and wall in the level
    def update(self, playerOne, playerTwo):
        for button in self.button_list:
            button.updateColor()            
            button.wall.update(button.activated, playerOne, playerTwo)
            button.deactivate()
    
    #draws the background image and platforms on the screen
    def draw(self, screen, bg_image):
        screen.blit(bg_image, (0, 0))
        self.platform_list.draw(screen)

#the basic platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        #makes Platform an image
        #colors are off on Macs for some reason
        self.image = pygame.image.load("../resources/grass.png").convert() 
        self.image = pygame.transform.scale(self.image, (20, 20))
    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#inherits from platform, just uses a different image
class Dirt(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        
        #makes dirt an image
        #colors are off on Macs for some reason
        self.image = pygame.image.load("../resources/ground.png").convert() 
        self.image = pygame.transform.scale(self.image, (20, 20))
    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#class for the moving walls
class Wall(Platform):
    def __init__(self, x, y, bottom, maxIncrease, speedY):
        #x, y are the initial location for the wall (upper left corner)
        #bottom is the y-position that the wall can be at lowest, equal to where it starts at
        #maxIncrease is the total vertical change that the wall can have
        #speedY is how fast the wall is allowed to move
        
        Platform.__init__(self, x, y)
        self.image = pygame.Surface([20, bottom - y])
        self.image.fill((0, 0, 255))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.bottomY = y
        self.topY = y - maxIncrease
        self.speedY = speedY
        
        self.disabled = False
    
    #updates the wall
    def update(self, activated, playerOne, playerTwo):
        #if the button is activated, move the wall up
        if(activated):
            self.rect.y = self.rect.y - self.speedY
            #stop moving if it is past the maximum it can go
            if self.rect.y < self.topY:
                self.rect.y = self.topY
                
            #checking for certain collisions with the players as it moves up
            if pygame.sprite.collide_rect(self, playerOne) and self.rect.y < playerOne.rect.bottom:
                playerOne.rect.bottom = self.rect.y - 1
            if pygame.sprite.collide_rect(self, playerTwo) and self.rect.y < playerTwo.rect.bottom:
                playerTwo.rect.bottom = self.rect.y - 1
            
        
        #if the wall is disabled, do nothing (wall cannot be disabled and activated at the same time)        
        elif self.disabled:
            self.disabled = False
        
        #wall is moving downwards
        else:
            self.rect.y = self.rect.y + self.speedY
            #stop moving if it is past the lowest it can go
            if self.rect.y > self.bottomY:
                self.rect.y = self.bottomY
                
            #checking for certain collisions with the players as it moves down
            else:
                if pygame.sprite.collide_rect(self, playerOne) and self.rect.bottom > playerOne.rect.y:
                    self.rect.bottom = playerOne.rect.y + 1
                    if playerOne.onGround:
                        playerOne.disabled = True
                    self.disabled = True
                    
                if pygame.sprite.collide_rect(self, playerTwo) and self.rect.bottom > playerTwo.rect.y:
                    self.rect.bottom = playerTwo.rect.y + 1
                    if playerTwo.onGround:
                        playerTwo.disabled = True
                    self.disabled = True
    
                if self.rect.y > self.bottomY:
                    self.rect.y = self.bottomY
           
#class definition for the button        
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, wall):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("../resources/redButton.png").convert() 
        self.image = pygame.transform.scale(self.image, (20, 20))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.wall = wall
        self.activated = False
        
    def activate(self):
        self.activated = True
        
    def deactivate(self):
        self.activated = False
    
    #if it is stepped on or off of, change the sprite for the button
    def updateColor(self):
        if (self.activated):
            self.image = pygame.image.load("../resources/greenButton.png").convert() 
            self.image = pygame.transform.scale(self.image, (20, 20))
        else:
            self.image = pygame.image.load("../resources/redButton.png").convert() 
            self.image = pygame.transform.scale(self.image, (20, 20))

#class for the spike, which inherits from platform            
class Spike(Platform):
    def __init__(self,x,y,width,height):
        Platform.__init__(self,x,y)
        self.width=width
        self.height=height
        self.image = pygame.image.load("../resources/spike.png").convert()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image.set_colorkey(pygame.Color("white"))
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
