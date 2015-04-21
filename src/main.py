import pygame, Key, Gate, Level, sys, EndScreen
import enemy as enemyFile

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#background music
pygame.mixer.init()

#This song is was taken from the open source website www.tannerhelland.com
#and is credited to Tanner Helland.
pygame.mixer.music.load('../resources/Surreptitious.OGG')

#default colors for the players
p1Color="red"
p2Color="purple" 

#function to reset the level or move onto the next one
def resetLevel(playerOne, playerTwo, enemy, current_level_num, current_level, reset):
    #reset is true we keep the same level, false if we move onto the next level
    if not reset:
        current_level_num += 1
    
    #default locations for the players
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
        playerTwo.standUp(current_level.platform_list, playerOne)
    
    #enemy starts off the screen by default
    enemy.rect.x = -100
    enemy.rect.y = SCREEN_HEIGHT-20-80
    if enemy.crouching:
        enemy.standUp(current_level.platform_list)

    #special cases for certain levels
    #In level 4, the players start at a different location
    if current_level_num == 4:
        playerOne.rect.y = SCREEN_HEIGHT / 2 - 40
        playerTwo.rect.x = 20
        
    #levels 5 and 7 have the enemies on the screen
    elif current_level_num == 5:
        enemy.rect.x = 400;
    elif current_level_num == 7:
        enemy.rect.x = 640
        enemy.rect.y = 300
    
    #settings for animations    
    playerOne.rightIDX = 2
    playerTwo.rightIDX = 2
    enemy.rightIDX = 2
    playerOne.image = playerOne.rightImages[playerOne.rightIDX]
    playerOne.image = pygame.transform.scale(playerOne.image, (playerOne.width, playerOne.height))
    playerTwo.image = playerTwo.rightImages[playerTwo.rightIDX]
    playerTwo.image = pygame.transform.scale(playerTwo.image, (playerTwo.width, playerTwo.height))
    enemy.image = enemy.rightImages[enemy.rightIDX]
    enemy.image = pygame.transform.scale(enemy.image, (enemy.width, enemy.height))
    
    return current_level_num

#called by the Main Menu
def load(current_level_num, muted):
    global p1Color,p2Color
    pygame.init()
    
    #Initiate a font for messages
    pygame.font.init()
    font = pygame.font.SysFont("Courier New", 18)
    
    #setting the screen
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("Over Under")
    
    #background image was taken from http://pixgood.com/cartoon-grass-and-sky.html
    bg_image = pygame.image.load("../resources/background1.png").convert()
    bg_image = pygame.transform.scale(bg_image, [SCREEN_WIDTH, SCREEN_HEIGHT])

    #keeping track of total levels in the game
    TOTAL_LEVELS = 9
    
    #play background music
    pygame.mixer.music.play(-1, 0)
    
    #setting up sound effects
    gateSound = pygame.mixer.Sound('../resources/Unlock.ogg')
    hurtSound = pygame.mixer.Sound('../resources/Ow.ogg')
    
    #start with the music muted if the mute option is turned on
    if muted:
        pygame.mixer.music.pause()
 
    #creating the reset button
    resetLoc = (20, 20)
    resetSize = (45, 45)
    reset = Button("../resources/reset.png", resetLoc, resetSize)
    reset.image.set_colorkey([255, 255, 255])
    
    #creating the home button
    homeLoc = (77, 20)
    homeSize = (45, 45)
    home = Button("../resources/home.png", homeLoc, homeSize)
    home.image.set_colorkey([255, 216, 63])
    
    #creating the mute button
    muteLoc = (134, 20)
    muteSize = (45, 45)
    if not muted:
        mute = Button("../resources/sound.png", muteLoc, muteSize)
    else:
        mute = Button("../resources/soundMute.png", muteLoc, muteSize)
    mute.image.set_colorkey([255, 255, 255])
    
    #timer to help run at 60 fps
    timer = pygame.time.Clock()
    
    #Initializes the players and enemy
    playerOne = Player(20, SCREEN_HEIGHT - 20 - 80, 1,p1Color)
    playerTwo = Player(80, SCREEN_HEIGHT - 20 - 80, 2,p2Color)
    enemy = enemyFile.Enemy(-100,SCREEN_HEIGHT-20-80)

    if current_level_num == 0:
        current_level_num= 1
    #sets this to the current level
    current_level = Level.Level(current_level_num)
    
    #set up the level
    current_level_num = resetLevel(playerOne, playerTwo, enemy, current_level_num, current_level, True)
    
    #instantiate the level
    current_level = Level.Level(current_level_num)
    
    
    #main game loop
    while True:
        mouseClicked = False
        
        #if the player exits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
                
            #checks for various key presses
            if event.type == pygame.KEYDOWN:
                #cheat code - the ENTER key skips the level
                if event.key == pygame.K_RETURN:
                    if current_level_num == TOTAL_LEVELS:
                        pygame.mixer.music.fadeout(100)
                        EndScreen.load()
                        return [0, muted]
                    current_level_num = resetLevel(playerOne, playerTwo,enemy, current_level_num, current_level, False)
                    current_level = Level.Level(current_level_num)
                
                #controls for player one
                if event.key == pygame.K_w:
                    playerOne.jump()
                if event.key == pygame.K_a:
                    playerOne.go_left()
                if event.key == pygame.K_d:
                    playerOne.go_right()
                
                #controls for player two
                if event.key == pygame.K_LEFT:
                    playerTwo.go_left()
                if event.key == pygame.K_RIGHT:
                    playerTwo.go_right()
                if event.key == pygame.K_UP: 
                    if playerTwo.crouching:
                        playerTwo.standUp(current_level.platform_list, playerOne)
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
                mouseClicked = True
 
        #updates the players and sees if they have the conditions to finish the level
        [levelCompleteOne,dead1] = playerOne.update(current_level.platform_list, playerTwo, muted)
        [levelCompleteTwo,dead2] = playerTwo.update(current_level.platform_list, playerOne, muted)
        
        #updates the enemy
        [killed1,killed2] = enemy.update(current_level.platform_list,[playerOne,playerTwo])
        
        #updates the level, like the moving walls
        current_level.update(playerOne, playerTwo)
        
        #if either player was killed and the game is not muted, play a death sound
        if killed1 or killed2:
            if not muted:
                hurtSound.play()
        
        #if the level was completed
        if levelCompleteOne and levelCompleteTwo:
            #play a gate sound if not muted
            if not muted:
                gateSound.play()
                pygame.time.wait(100)

            #no levels left, go to the congratulations screen
            #then return to the main menu
            if current_level_num == TOTAL_LEVELS:
                pygame.mixer.music.fadeout(100)
                EndScreen.load()
                return [0, muted]
            #if there are still levels left
            else:
                #restarts the players and loads the next level
                current_level_num = resetLevel(playerOne, playerTwo,enemy, current_level_num, current_level, False)
                current_level = Level.Level(current_level_num)
        
        elif dead1 or dead2 or killed1 or killed2:
            current_level_num = resetLevel(playerOne, playerTwo,enemy, current_level_num, current_level, True)
            current_level = Level.Level(current_level_num)
        
        #draw the platforms
        current_level.draw(screen, bg_image)
        
        #draw the players
        playerOne.draw(screen)
        playerTwo.draw(screen)
        
        #draw the enemy
        enemy.draw(screen)
        
        #draw the message for the level at the top center of the screen
        messageText = current_level.message
        messageWrite = font.render(messageText, 1, [0, 0, 255])
        screen.blit(messageWrite, ((SCREEN_WIDTH - messageWrite.get_width())/2, 40))
        messageText = current_level.levelText
        messageWrite = font.render(messageText, 1, [0, 0, 255])
        screen.blit(messageWrite, ((SCREEN_WIDTH - messageWrite.get_width())/2, 20))
       
        #display the menu buttons in the upper left
        screen.blit(reset.image, reset)
        screen.blit(home.image, home)
        screen.blit(mute.image, mute)
        
        #determine if buttons were pressed
        homeClicked = False
        resetClicked = False
        if mouseClicked == True:
            resetClicked = Button.mouseClick(reset, resetSize, resetLoc, 1, muted)
            if resetClicked:
                current_level_num = resetLevel(playerOne, playerTwo,enemy, current_level_num, current_level, True)
                current_level = Level.Level(current_level_num)
            else:
                homeClicked = Button.mouseClick(home, homeSize, homeLoc, 2, muted)
                if homeClicked:
                    return [current_level_num, muted]
                else:
                    muted = Button.mouseClick(mute, muteSize, muteLoc, 3, muted)
        
        #for 60fps - doesn't work well on Macs
        timer.tick(60)
        
        pygame.display.update()
    
    return [0, muted]

#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, playerNum,color):
        #setting up the player sprite
        pygame.sprite.Sprite.__init__(self)
        self.color=color
        self.image = pygame.image.load("../resources/"+self.color+"/player.png").convert()
        self.image.set_colorkey(pygame.Color("white"))
        
        #animations
        self.leftImages = []
        self.rightImages = []
        self.leftCrouchImages = []
        self.rightCrouchImages = []
        self.leftIDX = 0
        self.rightIDX = 0
        self.leftCrouchIDX = 0
        self.rightCrouchIDX = 0
        self.leftImages.append(pygame.image.load("../resources/"+color+"/knightLeft1.png").convert())
        self.leftImages.append(pygame.image.load("../resources/"+color+"/knightLeft3.png").convert())
        self.leftImages.append(pygame.image.load("../resources/"+color+"/knightLeft2.png").convert())
        self.rightImages.append(pygame.image.load("../resources/"+color+"/knightRight1.png").convert())
        self.rightImages.append(pygame.image.load("../resources/"+color+"/knightRight3.png").convert())
        self.rightImages.append(pygame.image.load("../resources/"+color+"/knightRight2.png").convert())
        self.leftCrouchImages.append(pygame.image.load("../resources/"+color+"/knightLeft1Crouch.png").convert())
        self.leftCrouchImages.append(pygame.image.load("../resources/"+color+"/knightLeft3Crouch.png").convert())
        self.leftCrouchImages.append(pygame.image.load("../resources/"+color+"/knightLeft2Crouch.png").convert())
        self.rightCrouchImages.append(pygame.image.load("../resources/"+color+"/knightRight1Crouch.png").convert())
        self.rightCrouchImages.append(pygame.image.load("../resources/"+color+"/knightRight3Crouch.png").convert())
        self.rightCrouchImages.append(pygame.image.load("../resources/"+color+"/knightRight2Crouch.png").convert())
        
        #some sounds for player actions
        self.painSound = pygame.mixer.Sound('../resources/Spikes.ogg')
        self.keySound = pygame.mixer.Sound('../resources/Ding.ogg')
        
        #variables for the player
        self.width = 40
        self.height = 80
        self.ticker = 0
        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        
        #creating the rectangle for the player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        #speed
        self.speedX = 0
        self.speedY = 0
        
        self.onGround = True
        self.crouching = False
        self.playerNum = playerNum #1 for jumping player, 2 for crouching player
        self.hasKey = False
        
        self.disabled = True
    
    #function that returns true if the player is on top of a platform, wall, or another player that is on the ground
    def isOnGround(self, platform_list, otherPlayer):
        #move the player down slightly and check if it collides with anything
        self.rect.y = self.rect.y + 1
        collision_list = pygame.sprite.spritecollide(self, platform_list, False)
        
        for block in collision_list:
            if block.rect.y > self.rect.y:
                self.rect.y = self.rect.y - 1
                return True
        if pygame.sprite.collide_rect(self, otherPlayer) and otherPlayer.rect.y > self.rect.y and otherPlayer.onGround:
            self.rect.y = self.rect.y - 1
            return True
        
        #didn't collide with anything at the bottom
        self.rect.y = self.rect.y - 1
        return False
        
    #updates the player's location and checks for collisions
    def update(self, platform_list, otherPlayer, noSound):
        levelComplete = False
        dead = False
        self.image.set_colorkey(pygame.Color("white"))
        
        #calculates new y speed
        self.calcGrav()
        
        #if a player is diabled, AKA stuck underneath a wall, they cannot move
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
            
            #if it's a spike
            if isinstance(block,Level.Spike):
                if self.speedX > 0:
                    self.rect.right = block.rect.left
                #if moving right, place the player to the left of the platform
                elif self.speedX < 0:
                    self.rect.left = block.rect.right 
                if not noSound:
                    self.painSound.play()
                #player dies
                dead = True
            #if it's a platform
            elif isinstance(block, Level.Platform):
                if not((isinstance(block, Level.Wall)) and (block.rect.bottom - 10) < self.rect.y):
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
                if not noSound:
                    self.keySound.play()
                #removes the key from the screen
                block.rect.x=-50
            #if it's a gate
            elif isinstance(block, Gate.gate) and self.hasKey:
                #if they have a key, levelComplete is true and is returned later
                levelComplete = True
                
        #checks for collision with the other player, similar to a platform
        if pygame.sprite.collide_rect(self, otherPlayer):
            if self.speedX > 0:
                self.rect.right = otherPlayer.rect.left
            elif self.speedX < 0:
                self.rect.left = otherPlayer.rect.right
         
        #moves in y direction    
        self.rect.y += self.speedY
 
        #check if the player is currently on the ground
        self.onGround = self.isOnGround(platform_list, otherPlayer)
 
        #checks for collisions
        collision_list = pygame.sprite.spritecollide(self, platform_list, False)
        for block in collision_list:
            
            #if the player is on top of a button, activate the button
            if isinstance(block, Level.Button) and self.rect.y < block.rect.y:
                block.activate()
            
            #just like collisions with x direction
            if isinstance(block, Level.Platform):
                
                #If the player is under a wall, stop the player's and the wall's movement
                if isinstance(block, Level.Wall) and self.rect.y > block.rect.y:
                    if self.onGround:
                        block.rect.bottom = self.rect.top + 1
                        if block.rect.y > block.bottomY:
                            block.rect.y = block.bottomY
                    else:
                        self.rect.top = block.rect.bottom + 1
                    block.disabled = True
                    #if the player is stuck between the ground and the wall, the player becomes disabled
                    if self.onGround:
                        self.disabled = True
                #if the player touched a spike
                elif isinstance(block,Level.Spike):
                    if self.speedY > 0:
                        self.rect.bottom = block.rect.top
                    #if moving right, place the player to the left of the platform
                    elif self.speedX < 0:
                        self.rect.bottom = block.rect.top 
                    if not noSound:
                        self.painSound.play()
                    dead = True   
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
                if not noSound:
                    self.keySound.play()
                block.rect.x=-50
            elif isinstance(block,Gate.gate) and self.hasKey:
                levelComplete = True
        
        #check for collisions with the other player    
        if pygame.sprite.collide_rect(self, otherPlayer):
            if self.speedY > 0:
                self.rect.bottom = otherPlayer.rect.top
                if otherPlayer.onGround:
                    self.onGround = True
            elif self.speedY < 0:
                self.rect.top = otherPlayer.rect.bottom
            self.speedY = 0
        
        #prevent the player from leaving the borders of the screen
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width
        if self.rect.y <= 0:
            self.rect.y = 0
            self.speedY = 0
        
        #call the animate function
        self.animate()      
         
        return [levelComplete,dead]   
    
    #calculates the speed of the y-direction for the player        
    def calcGrav(self):
        #make the player start falling
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

    #function for just player Two
    def standUp(self, platform_list, otherPlayer):
        #create new sprite for standing up
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../resources/"+self.color+"/player.png").convert()
        self.image.set_colorkey(pygame.Color("white"))

        #new height for the player
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
        
        #if standing up causes a collision, crouch back down
        if pygame.sprite.collide_rect(self, otherPlayer):
            self.crouch()
        else:
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
        self.image = pygame.image.load("../resources/"+self.color+"/playerCrouch.png").convert()
        self.image.set_colorkey(pygame.Color("white"))

        #new height of player
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

    #changes the y-direction speed for the player
    def jump(self):
        self.image.set_colorkey(pygame.Color("white"))
        if self.onGround and not self.disabled:
            self.speedY = -12 + (4.5 * (self.playerNum - 1)) #different values for different players
            self.onGround = False
 
    #draws the players when called onto screen
    def draw(self, screen):
        self.image.set_colorkey(pygame.Color("white"))
        screen.blit(self.image, (self.rect.x, self.rect.y))

    #functions for the x-direction movement
    def go_left(self):
        self.image.set_colorkey(pygame.Color("white"))
        self.speedX = -6
    def go_right(self):
        self.image.set_colorkey(pygame.Color("white"))
        self.speedX = 6
    def stop(self):
        self.image.set_colorkey(pygame.Color("white"))
        self.speedX = 0        
    
    #animates the players
    def animate(self):
        #updates only every other frame
        if self.ticker%2 ==0:
            self.image.set_colorkey(pygame.Color("white"))
            #if moving left on the ground
            if self.speedX < 0 and self.speedY == 0:
                #standing up
                if not self.crouching:
                    self.leftIDX = (self.leftIDX+1)%3
                    self.image = self.leftImages[self.leftIDX]
                    self.image = pygame.transform.scale(self.image, (self.width, self.height))
                    self.image.set_colorkey(pygame.Color("white"))

                #crouching
                else:
                    self.leftCrouchIDX = (self.leftCrouchIDX+1)%3
                    self.image = self.leftCrouchImages[self.leftCrouchIDX]
                    self.image = pygame.transform.scale(self.image, (self.width, self.height))
                    self.image.set_colorkey(pygame.Color("white"))\
                    
            #if moving right and on the ground
            elif self.speedX > 0 and self.speedY == 0:
                #standing up
                if not self.crouching:
                    self.rightIDX = (self.rightIDX+1)%3
                    self.image = self.rightImages[self.rightIDX]
                    self.image = pygame.transform.scale(self.image, (self.width, self.height))
                    self.image.set_colorkey(pygame.Color("white"))
                    
                #crouching
                else:
                    self.rightCrouchIDX = (self.rightCrouchIDX+1)%3
                    self.image = self.rightCrouchImages[self.rightCrouchIDX]
                    self.image = pygame.transform.scale(self.image, (self.width, self.height))
                    self.image.set_colorkey(pygame.Color("white"))
                    
            #in the air moving left
            elif self.speedX < 0 and self.speedY != 0:
                if not self.crouching:
                    self.leftIDX = 0
                    self.image = self.leftImages[self.leftIDX]
                    self.image = pygame.transform.scale(self.image, (self.width, self.height))
                    self.image.set_colorkey(pygame.Color("white"))
                elif self.crouching:
                    self.leftCrouchIDX = 0
                    self.image = self.leftCrouchImages[self.leftCrouchIDX]
                    self.image = pygame.transform.scale(self.image, (self.width, self.height))
                    self.image.set_colorkey(pygame.Color("white"))
            #in the air moving right
            elif self.speedX > 0 and self.speedY != 0:
                if not self.crouching:
                    self.rightIDX = 0
                    self.image = self.rightImages[self.rightIDX]
                    self.image = pygame.transform.scale(self.image, (self.width, self.height))
                    self.image.set_colorkey(pygame.Color("white"))
                elif self.crouching:
                    self.rightCrouchIDX = 0
                    self.image = self.rightCrouchImages[self.rightCrouchIDX]
                    self.image = pygame.transform.scale(self.image, (self.width, self.height))
                    self.image.set_colorkey(pygame.Color("white"))
        self.ticker += 1

#class for the menu buttons on the screen
class Button(pygame.sprite.Sprite):
    def __init__(self, filename, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)
        #self.image.set_colorkey(color) 
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
    #called when the mouse is clicked
    def mouseClick(self, buttonSize, location, file, muted):
        #get the position of the mouse click
        mouseLoc = pygame.mouse.get_pos()

        #file 1 is to reset the level
        if file == 1:
            if (mouseLoc[0] > location[0] and mouseLoc[0] < (location[0] + buttonSize[0])):
                if (mouseLoc[1] > location[1] and mouseLoc[1] < (location[1] + buttonSize[1])):
                    return True

        #file 2 is to return to main menu
        elif file == 2:
            if (mouseLoc[0] > location[0] and mouseLoc[0] < (location[0] + buttonSize[0])):
                if (mouseLoc[1] > location[1] and mouseLoc[1] < (location[1] + buttonSize[1])):
                    #backgroundMusic.fadeout(100)
                    if not muted:
                        pygame.mixer.music.fadeout(100)
                    return True
        
        #file 3 is to mute/play sounds
        elif file == 3:
            if (mouseLoc[0] > location[0] and mouseLoc[0] < (location[0] + buttonSize[0])) and (mouseLoc[1] > location[1] and mouseLoc[1] < (location[1] + buttonSize[1])):
                    if muted:
                        pygame.mixer.music.unpause()
                        self.image = pygame.image.load("../resources/sound.png").convert()
                        self.image = pygame.transform.scale(self.image, self.size)
                        self.image.set_colorkey([255, 255, 255])
                        return False
                    else:
                        pygame.mixer.music.pause()
                        self.image = pygame.image.load("../resources/soundMute.png").convert()
                        self.image = pygame.transform.scale(self.image, self.size)
                        self.image.set_colorkey([255, 255, 255])
                        return True
            else:
                return muted
            
#this code exists so that main.py can be run to start immediately into the game
#however, this means that you cannot go back to the main menu afterwards
if(__name__ == "__main__"):
    load(1, False)
