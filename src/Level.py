import pygame, Key, Gate

def generate(levnum):
    levelMap = 0
    if levnum == 1:
        levelMap = [
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                             K                                P",
    "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
    "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
    "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
    "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
    "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
    "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
    "P                                                              P",
    "P                                                              P",
    "P                              K                              GP",
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]
        
    elif levnum == 2:
        levelMap = [
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P             P                                                P",
    "P              PPP                         K                   P",
    "P                 P                                            P",
    "P                P                                             P",
    "P               P                                              P",
    "P              P                                               P",
    "P             P                             P                  P",
    "P            PPPPP                         P                   P",
    "P                                         P                    P",
    "P                                        PPPPP                 P",
    "P             K              P                         G       P",
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]
    
    #return levelMap
    if (levnum > 0):
        return Level(levelMap)

class Level(object):
    platform_list = None
    
    def __init__(self, levelMap):
        self.platform_list = pygame.sprite.Group()
        
        x = 0
        y = 0
        for row in levelMap:
            for col in row:
                if col == "P":
                    p = Platform(x, y)
                    self.platform_list.add(p)
                elif col =="K":
                    k = Key.key((x,y))
                    self.platform_list.add(k)
                elif col =="G":
                    g = Gate.gate((x,y))
                    self.platform_list.add(g)
                x += 20
            y += 20
            x = 0
        
    def draw(self, screen):
        screen.fill((255, 255, 255))
        self.platform_list.draw(screen)
        

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        
        self.image.fill((0, 0, 0))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y