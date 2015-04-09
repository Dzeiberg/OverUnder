import pygame, Key, Gate

class Level(object):
    platform_list = None
            
    def __init__(self, levelNum):
        self.platform_list = pygame.sprite.Group()
        self.button_list = []
        x = 0
        y = 0
        
        if levelNum == 1:
            levelMap = [
                "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                             K                                D",
                "D                  PPPPPPPPPPPPPPPPPPPPPPPPP                   D",
                "D                  DDDDDDDDDDDDDDDDDDDDDDDDD                   D",
                "D                  DDDDDDDDDDDDDDDDDDDDDDDDD                   D",
                "D                  DDDDDDDDDDDDDDDDDDDDDDDDD                   D",
                "D                  DDDDDDDDDDDDDDDDDDDDDDDDD                   D",
                "D                  DDDDDDDDDDDDDDDDDDDDDDDDD                   D",
                "D                                                              D",
                "D                                                              D",
                "D                              K                             G D",
                "DPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPD"]
        
        elif levelNum == 2:
            levelMap = [
                "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                   K                        K                GD",
                "DPPPPPPPPPPPPPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPP PPPPPPPPPPPPPPPPPD"]
        
        elif levelNum == 3:
            levelMap = [
                "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                               K                              D",
                "D                          PPPPP PPPP                          D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D             PPPPPPPP                                         D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D         PPPPPPPP PPP                                         D",
                "D         DDDDDDDDDDDD                                         D",
                "D         DDDD                                                 D",
                "D         DDDD                                                 D",
                "D         DDDD   K                                            GD",
                "DPPPPPPPP DDDDPPP PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPD"]
        
        elif levelNum == 4:
            levelMap = [
                "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                       K                      D",
                "DPPPPPPPPPPPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP        D",
                "D                                                     D        D",
                "D                                                     D        D",
                "D                                                     D        D",
                "D                                                     D        D",
                "D                                                     D        D",
                "D                                                     D        D",
                "D                                                     D        D",
                "D                                                     D        D",
                "D                                                     D        D",
                "D                                                     D        D",
                "D                                                     D        D",
                "D                                                     D        D",
                "D                                                     D        D",
                "D                                                              D",
                "D                                                              D",
                "D                                       K                     GD",
                "DPPPPPPPPPPPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPD"]
            
        elif levelNum == 5:
            levelMap = [
                "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                  K                           D",
                "D                         PPPPPPPPPPPPPPPPPP                   D",
                "D                         DDDDDDDDDDDDDDDDDD                   D",
                "D                         DDDDDDDDDDDDDDDDDD  SS               D",
                "D                                             PP               D",
                "D                                             DD               D",
                "D                                             DD               D",
                "D                                  K          DD              GD",
                "DPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPDDPPPPPPPPPPPPPPPD"]
        
        elif levelNum == 6:
            levelMap = [
                "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                             K                D",
                "D                                        PPPPP PPPPP           D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D                                                              D",
                "D         SSSS                                                 D",
                "D         DDDD       PPPPP                                     D",
                "D         DDDD                                                 D",
                "D         DDDD                                                 D",
                "D         DDDD         K                                      GD",
                "DPPPPPPPPPDDDDPPPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPD"]
            
        elif levelNum == 7:
            levelMap = [
                "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
                "D                              D                   D           D",
                "D                              D                   D           D",
                "D                              D                   D           D",
                "D                              D                   D           D",
                "D                              D       PPPPPP      D           D",
                "D                              D            D      D           D",
                "D                              D            D      D           D",
                "D                              D            D      D           D",
                "D                              D            D      D           D",
                "D                              D            D      D K         D",
                "D             PPPPPPPPPPP      D            D      DPPPP       D",
                "D                       D      D            DPP                D",
                "D                       D      D            DDD                D",
                "D                       D      D            DDD                D",
                "D                       D      D            DDD                D",
                "D            PPPPPPPPPP D      DPPPP        DDDPPPPPPPPPPPPPPPPD",
                "D                       D                   D                  D",
                "D                       D                   D                  D",
                "D                       D                   D                  D",
                "D                       D                   D                  D",
                "D      PPPP PPPPPPP     DPPPPPPPPPPPPPPPPPPPD                  D",
                "D      D                                                   PP PD",
                "D      D                                                       D",
                "D      D                                                       D",
                "D      D                                                       D",
                "D      D                                                       D",
                "D      D                                                       D",
                "D      D                                                       D",
                "D      DPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP            D",
                "D      DDDDDD        DDDDD  DDDDDDDDDDDDDDDDDDDDDDD            D",
                "D      DDDDDD                                                  D",
                "D                                                              D",
                "D                                                              D",
                "D                  PPPPPPPPP      K                           GD",
                "DPPPPPPPPPPPPPPPPPPDDDDDDDDDPPPPPPP PPPPP PPPPPPPPPPPPPPPPPPPPPP"]

        
        for row in levelMap:
                for col in row:
                    if col == "P":
                        p = Platform(x, y)
                        self.platform_list.add(p)
                    elif col =="K":
                        k = Key.key((x,y))
                        self.platform_list.add(k)
                    elif col =="D":
                        d = Dirt(x, y)
                        self.platform_list.add(d)
                    elif col =="G":
                        g = Gate.gate((x,y))
                        self.platform_list.add(g)
                    elif col =="S":
                        s=Spike(x,y,20,20)
                        self.platform_list.add(s)
                    x += 20
                y += 20
                x = 0
        
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
            
            
        elif levelNum == 4:
            self.wall = Wall(600, 140, 360, 120, 1)
            self.platform_list.add(self.wall)
            
            self.button = Button(360, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(600, 520, 700, 140, 1)
            self.platform_list.add(self.wall)
            
            self.button = Button(360, 360, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
        elif levelNum == 6:
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
            
        elif levelNum == 7:
            self.wall = Wall(1140, 200, 280, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(700, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(740, 320, 380, 40, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(820, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(1020, 620, 700, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(460, 320, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(220, 300, 440, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(1220, 440, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
        self.message = ""
        if levelNum == 1:
            self.message = "Each player can grab one key. Collect them both to unlock the gate!"
        elif levelNum == 2:
            self.message = "Stand on the buttons to move the walls!"
        elif levelNum == 3:
            self.message = "Click the refresh button in the corner if you want to restart the level"
        elif levelNum == 5:
            self.message = "Careful of the spikes and the monster!"
            
    def update(self, playerOne, playerTwo):
        for button in self.button_list:
            button.updateColor()            
            button.wall.update(button.activated, playerOne, playerTwo)
            button.deactivate()
        
    def draw(self, screen):
        screen.fill((255, 255, 255))
        self.platform_list.draw(screen)
        

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        #makes platform a black box
        #self.image = pygame.Surface([20, 20])
        #self.image.fill((0, 0, 0))
        
        #makes Platform an image
        self.image = pygame.image.load("../resources/grass.png").convert() 
        self.image = pygame.transform.scale(self.image, (20, 20))
    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Dirt(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        #makes dirt a black box
        self.image = pygame.Surface([20, 20])
        self.image.fill((178,126,68))
    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Wall(Platform):
    def __init__(self, x, y, bottom, maxIncrease, speedY):
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
        
    def update(self, activated, playerOne, playerTwo):
        if(activated):
            self.rect.y = self.rect.y - self.speedY
            
            if self.rect.y < self.topY:
                self.rect.y = self.topY
                
        elif self.disabled:
            self.disabled = False
            
        else:
            self.rect.y = self.rect.y + self.speedY
            
            if pygame.sprite.collide_rect(self, playerOne) and self.rect.bottom > playerOne.rect.y:
                self.rect.bottom = playerOne.rect.y + 1
                playerOne.disabled = True
                self.disabled = True
                
            elif pygame.sprite.collide_rect(self, playerTwo) and self.rect.bottom > playerTwo.rect.y:
                self.rect.bottom = playerTwo.rect.y + 1
                playerTwo.disabled = True
                self.disabled = True
            
            elif self.rect.y > self.bottomY:
                self.rect.y = self.bottomY
           
        
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, wall):
        pygame.sprite.Sprite.__init__(self)
        
        #self.image = pygame.Surface([20,20])
        #self.image.fill((255, 0, 0))
        
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
    
    def updateColor(self):
        if (self.activated):
            #self.image.fill((0, 255, 0))
            self.image = pygame.image.load("../resources/greenButton.png").convert() 
            self.image = pygame.transform.scale(self.image, (20, 20))
        else:
            #self.image.fill((255, 0, 0))
            self.image = pygame.image.load("../resources/redButton.png").convert() 
            self.image = pygame.transform.scale(self.image, (20, 20))
            
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
