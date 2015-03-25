import pygame, Key, Gate, Level, sys, EndScreen

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#background music
pygame.mixer.init()
backgroundMusic = pygame.mixer.music
backgroundMusic.load('../resources/bgmusic.mp3')
    
def resetLevel(playerOne, playerTwo, current_level_num, current_level, reset):
    if not reset:
        current_level_num += 1
    
    playerOne.rect.x = 20
    playerOne.rect.y = SCREEN_HEIGHT - 20 - 80
    playerTwo.rect.x = 80
    playerTwo.rect.y = SCREEN_HEIGHT - 20 - 80
    playerOne.speedX = 0
    playerOne.speedY = 0
    playerTwo.speedX = 0
    playerTwo.speedY = 0
    playerOne.hasKey = False
    playerTwo.hasKey = False
    
    if playerTwo.crouching:
        playerTwo.standUp(current_level.platform_list)
        
    if current_level_num == 3:
        playerOne.rect.y = SCREEN_HEIGHT / 2 - 80
        playerTwo.rect.x = 20
    
    return current_level_num

#called by the Main Menu
def load(current_level_num):
    pygame.init()
    
    pygame.font.init()
    font = pygame.font.SysFont("Courier New", 18)
    
    tutorialText = ""
    tutorialWrite = font.render(tutorialText, 1, [0, 0, 255])
    
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    
    pygame.display.set_caption("Over Under")
    
    #play background music
    backgroundMusic.play(-1, 0)
    
    #creating the reset button
    resetLoc = (30, 30)
    resetSize = (45, 45)
    reset = Button("../resources/reset.png", resetLoc, resetSize)
    
    #creating the home button
    homeLoc = (87, 30)
    homeSize = (45, 45)
    home = Button("../resources/home.png", homeLoc, homeSize)
    
    #Does not work properly on Macs
    timer = pygame.time.Clock()
    
    #Initializes the starting locations of player
    #TODO: initialize them in a different location depending on the level number
    playerOne = Player(20, SCREEN_HEIGHT - 20 - 80, 1)
    playerTwo = Player(80, SCREEN_HEIGHT - 20 - 80, 2)
    
    #sets this to the current level
    TOTAL_LEVELS = 5

    current_level = Level.Level(current_level_num)
    
    
    #main game loop
    while True:
        game = 1
        
        #if the player exits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
                
            #checks for various key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if current_level_num == TOTAL_LEVELS:
                        EndScreen.load()
                        return current_level_num
                    current_level_num = resetLevel(playerOne, playerTwo, current_level_num, current_level, False)
                    current_level = Level.Level(current_level_num)
                    
                if event.key == pygame.K_w:
                    playerOne.jump()
                if event.key == pygame.K_a:
                    playerOne.go_left()
                if event.key == pygame.K_d:
                    playerOne.go_right()
                
                if event.key == pygame.K_LEFT:
                    playerTwo.go_left()
                if event.key == pygame.K_RIGHT:
                    playerTwo.go_right()
                if event.key == pygame.K_UP: 
                    if playerTwo.crouching:
                        playerTwo.standUp(current_level.platform_list)
                    else:
                        playerTwo.jump()  
                elif event.key == pygame.K_DOWN and playerTwo.onGround and (playerTwo.crouching == False):
                    playerTwo.crouch()   
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and playerOne.speedX < 0:
                    playerOne.stop()
                if event.key == pygame.K_d and playerOne.speedX > 0:
                    playerOne.stop()
                
                if event.key == pygame.K_LEFT and playerTwo.speedX < 0:
                    playerTwo.stop()
                if event.key == pygame.K_RIGHT and playerTwo.speedX > 0:
                    playerTwo.stop()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                game = 2
 
        #updates the players and sees if they have the conditions to finish the level
        levelCompleteOne = playerOne.update(current_level.platform_list, playerTwo)
        levelCompleteTwo = playerTwo.update(current_level.platform_list, playerOne)
        
        current_level.update(playerOne, playerTwo)
        
        if levelCompleteOne and levelCompleteTwo:
            #if there are still levels remaining
            
            #no levels left, return and exit back to the main menu
            if current_level_num == TOTAL_LEVELS:
                EndScreen.load()
                return 0
            else:
                #restarts the players and loads the next level
                current_level_num = resetLevel(playerOne, playerTwo, current_level_num, current_level, False)
                current_level = Level.Level(current_level_num)
        
        #draw the platforms
        current_level.draw(screen)
        
        #draw the players
        playerOne.draw(screen)
        playerTwo.draw(screen)
        tutorialText = current_level.message
        tutorialWrite = font.render(tutorialText, 1, [0, 0, 255])
        screen.blit(tutorialWrite, ((SCREEN_WIDTH - tutorialWrite.get_width())/2, 20))
       
        #to determine what button was pressed
        screen.blit(reset.image, reset)
        screen.blit(home.image, home)
        
        resetClicked = False
        if (game == 2):
            resetClicked = Button.mouseClick(reset, resetSize, resetLoc, 1, current_level_num)
            Button.mouseClick(home, homeSize, homeLoc, 2, current_level_num)
        
        if resetClicked:
            current_level_num = resetLevel(playerOne, playerTwo, current_level_num, current_level, True)
            current_level = Level.Level(current_level_num)
        
        #for 60fps
        #DOESN'T WORK ON MACS
        timer.tick(60)
        
        pygame.display.update()
    
    return 0

#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, playerNum):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../resources/player.png").convert()
        self.image.set_colorkey(pygame.Color("white"))
        self.leftImages = []
        self.rightImages = []
        self.leftCrouchImages = []
        self.rightCrouchImages = []
        self.leftIDX = 0
        self.rightIDX = 0
        self.leftCrouchIDX = 0
        self.rightCrouchIDX = 0
        self.leftImages.append(pygame.image.load("../resources/knightLeft1.png").convert())
        self.leftImages.append(pygame.image.load("../resources/knightLeft3.png").convert())
        self.leftImages.append(pygame.image.load("../resources/knightLeft2.png").convert())
        self.rightImages.append(pygame.image.load("../resources/knightRight1.png").convert())
        self.rightImages.append(pygame.image.load("../resources/knightRight3.png").convert())
        self.rightImages.append(pygame.image.load("../resources/knightRight2.png").convert())
        self.leftCrouchImages.append(pygame.image.load("../resources/knightLeft1Crouch.png").convert())
        self.leftCrouchImages.append(pygame.image.load("../resources/knightLeft3Crouch.png").convert())
        self.leftCrouchImages.append(pygame.image.load("../resources/knightLeft2Crouch.png").convert())
        self.rightCrouchImages.append(pygame.image.load("../resources/knightRight1Crouch.png").convert())
        self.rightCrouchImages.append(pygame.image.load("../resources/knightRight3Crouch.png").convert())
        self.rightCrouchImages.append(pygame.image.load("../resources/knightRight2Crouch.png").convert())
        self.width = 40
        self.height = 80
        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speedX = 0
        self.speedY = 0
        
        self.onGround = True
        self.crouching = False
        self.playerNum = playerNum #1 for jumping player, 2 for crouching player
        self.hasKey = False
        
        self.disabled = True
        
    def update(self, platform_list, otherPlayer):
        levelComplete = False
        self.image.set_colorkey(pygame.Color("white"))
        #calculates new y speed
        self.calcGrav()
 
        if self.disabled:
            self.speedX = 0
            if self.onGround == True:
                self.speedY = 0
            self.disabled = False
 
        #moves in x direction
        self.rect.x += self.speedX
 
        #checks if the player collides with anything
        collision_list = pygame.sprite.spritecollide(self, platform_list, False)
        for block in collision_list:
            #if it's a platform
            if isinstance(block, Level.Platform):
                #if moving left, place the player to the right of the platform
                if self.speedX > 0:
                    self.rect.right = block.rect.left
                #if moving right, place the player to the left of the platform
                elif self.speedX < 0:
                    self.rect.left = block.rect.right
            #if it's a key
            elif isinstance(block,Key.key) and not self.hasKey:
                #player now has a key
                self.hasKey = True
                #removes the key from the screen
                block.rect.x=-50
            #if it's a gate
            elif isinstance(block, Gate.gate) and self.hasKey:
                #if they have a key, levelComplete is true and is return later
                levelComplete = True
                
        #checks for collision with the other player, similar to a platform
        if pygame.sprite.collide_rect(self, otherPlayer):
            if self.speedX > 0:
                self.rect.right = otherPlayer.rect.left
            elif self.speedX < 0:
                self.rect.left = otherPlayer.rect.right
         
        #moves in y direction    
        self.rect.y += self.speedY
 
        self.onGround = False
 
        #checks for collisions
        collision_list = pygame.sprite.spritecollide(self, platform_list, False)
        for block in collision_list:
            
            #if the player is on top of a button, activate the button
            if isinstance(block, Level.Button):
                block.activate()
            
            #just like collisions with x direction
            if isinstance(block, Level.Platform):
                #If the player is under a wall, stop the player's and the wall's movement
                if isinstance(block, Level.Wall) and self.rect.y > block.rect.y:
                    block.rect.bottom = self.rect.top + 1
                    block.disabled = True
                    self.disabled = True
                    
                else:
                    if self.speedY > 0:
                        self.rect.bottom = block.rect.top
                        self.onGround = True
                    elif self.speedY < 0:
                        self.rect.top = block.rect.bottom
                
                # Stop moving vertically if we hit a platform
                self.speedY = 0
                    
            if isinstance(block,Key.key) and not self.hasKey:
                self.hasKey = True
                block.rect.x=-50
            elif isinstance(block,Gate.gate) and self.hasKey:
                levelComplete = True
            
        if pygame.sprite.collide_rect(self, otherPlayer):
            if self.speedY > 0:
                self.rect.bottom = otherPlayer.rect.top
                if otherPlayer.onGround:
                    self.onGround = True
            elif self.speedY < 0:
                self.rect.top = otherPlayer.rect.bottom
            self.speedY = 0
        self.animate()
                
         
        #returns True if the player has a key and is at the gate, false otherwise
        return levelComplete   
            
    def calcGrav(self):
        #if they're not on the ground
        if self.speedY == 0:
            self.speedY = 1
        #acceleration for gravity
        else:
            self.speedY += .35
 
        #checks if they are past the bottom of the screen
        #not really needed since platforms will cover the bottom of the screen
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.speedY >= 0:
            self.speedY = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.onGround = True

    #function for player Two
    #TODO: perhaps make a new class for PlayerTwo that inherits from Player
    def standUp(self, platform_list):
        #create new sprite for standing up
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../resources/player.png").convert()
        self.image.set_colorkey(pygame.Color("white"))


        self.height = 80
        
        #storing old location
        x = self.rect.x
        y = self.rect.y
        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        #updating new location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 20
        
        self.crouching = False
        
        #if standing up makes you collide with another platform, go back to crouching
        collision_list = pygame.sprite.spritecollide(self, platform_list, False)
        
        for block in collision_list:
            if isinstance(block, Level.Platform):
                self.crouch()
                break
        
    #only for player Two       
    def crouch(self):
        #create new sprite for crouching player
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../resources/playerCrouch.png").convert()
        self.image.set_colorkey(pygame.Color("white"))


        self.height = 60
        
        #stores previous location
        x = self.rect.x
        y = self.rect.y
        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        #new location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 20

        self.crouching = True       

    def jump(self):
        self.image.set_colorkey(pygame.Color("white"))
        if self.onGround:
            self.speedY = -12 + (4.5 * (self.playerNum - 1)) #different values for different players
            self.onGround = False
 
    def draw(self, screen):
        self.image.set_colorkey(pygame.Color("white"))
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def go_left(self):
        self.image.set_colorkey(pygame.Color("white"))
        self.speedX = -6
 
    def go_right(self):
        self.image.set_colorkey(pygame.Color("white"))
        self.speedX = 6
 
    def stop(self):
        self.image.set_colorkey(pygame.Color("white"))
        self.speedX = 0        
    
    def animate(self):
        self.image.set_colorkey(pygame.Color("white"))
        if self.speedX < 0 and self.speedY == 0:
            #moving left
            if not self.crouching:
                self.leftIDX = (self.leftIDX+1)%3
                self.image = self.leftImages[self.leftIDX]
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                #self.rect = self.image.get_rect()
            else:
                self.leftCrouchIDX = (self.leftCrouchIDX+1)%3
                self.image = self.leftCrouchImages[self.leftCrouchIDX]
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                #self.rect = self.image.get_rect()
        elif self.speedX > 0 and self.speedY == 0:
            #moving right
            if not self.crouching:
                self.rightIDX = (self.rightIDX+1)%3
                self.image = self.rightImages[self.rightIDX]
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                #self.rect = self.image.get_rect()
            else:
                self.rightCrouchIDX = (self.rightCrouchIDX+1)%3
                self.image = self.rightCrouchImages[self.rightCrouchIDX]
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                #self.rect = self.image.get_rect()
        elif self.speedX < 0 and self.speedY != 0:
            self.leftIDX = 0
            self.image = self.leftImages[self.leftIDX]
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        elif self.speedX > 0 and self.speedY != 0:
            self.rightIDX = 0
            self.image = self.rightImages[self.rightIDX]
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            
class Button(pygame.sprite.Sprite):
    def __init__(self, filename, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

        
    def mouseClick(self, buttonSize, location, file, current_level_num):
        mouseLoc = pygame.mouse.get_pos()

        #file 1 is to reset the level
        if file == 1:
            if (mouseLoc[0] > location[0] and mouseLoc[0] < (location[0] + buttonSize[0])):
                if (mouseLoc[1] > location[1] and mouseLoc[1] < (location[1] + buttonSize[1])):
                    return True

        #file 2 is to return to main menu
        if file == 2:
            if (mouseLoc[0] > location[0] and mouseLoc[0] < (location[0] + buttonSize[0])):
                if (mouseLoc[1] > location[1] and mouseLoc[1] < (location[1] + buttonSize[1])):
                    backgroundMusic.fadeout(100)
                    import MainMenu
                    MainMenu.menu(current_level_num)
        
        
if(__name__ == "__main__"):
    load(1)
