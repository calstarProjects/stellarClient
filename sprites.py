import pygame
import math
import time
import keyboard
import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import pyautogui

# Putting tkinter in front
root = tkinter.Tk()
root.withdraw()
root.attributes('-topmost', True)
root.update

pygame.init()

# Set up the window dimentions
if tkinter.messagebox.askyesno('Screen Setup', 'Would you like a custom window size? (Alt is fullscreen)'):
    screenWidth = tkinter.simpledialog.askinteger('Screen Dimentions', 'What is your desired width?')
    screenHeight = tkinter.simpledialog.askinteger('Screen Dimentions', 'What is your desired height?')
else:
    screenWidth, screenHeight = pyautogui.size()

# print (screenWidth, screenHeight)
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Sprite list for ticking
spriteList = pygame.sprite.Group()

# Sprite setup
class sprite(pygame.sprite.Sprite):
    def __init__(self, image_file: str, x: int, y: int, width: int, height: int,name: str, hp:  int = None):
        super().__init__()

        self.name = name

        self.faded = False

        # self.image = pygame.image.load(image_file).convert_alpha()
        # self.image = pygame.transform.scale(self.image, (width, height))

        # # Save the clean version
        # self.base_image = self.image.copy()

        self.image = pygame.image.load(image_file).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, 
            (
                (width), 
                (height)
            )
        )
        self.baseImg = self.image.copy()
        self.inverted = pygame.transform.flip(self.image, True, False)
        self.fadedImage = pygame.transform.grayscale(self.image)
        self.fadedInversion = pygame.transform.grayscale(self.inverted)

        self.xVel = 0
        self.yVel = 0
        
        pygame.draw.rect(self.image, (20, 20, 20), pygame.rect.Rect(x, y, 0, 0))

        self.rect = self.image.get_rect()
        # self.rect.width = width
        # self.rect.height = height
        old_center = self.rect.center  # save before changing image
        self.rect = self.image.get_rect()
        self.rect.center = old_center  # restore after


        self.rect.centerx = x
        self.rect.centery = y

        spriteList.add(self)
        if hp:
            self.hp = hp
            self.maxHp = hp
    # Velocity Edits
    def applyForce(self, xForce: int, yForce: int):
        self.xVel += xForce
        self.yVel += yForce
    def setPos(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y
    # Updating pos
    def tick(self):
        # Flip image based on screen position
        if self.rect.centerx < screen.get_width() // 2:
            self.image = self.fadedInversion if self.faded else self.inverted
        else:
            if self.faded:
                self.image = self.fadedImage
            else:
                self.image = pygame.transform.flip(self.inverted, True, False)

        # Apply velocity
        self.rect.centerx += self.xVel
        self.rect.centery += self.yVel
        self.xVel *= 0.9
        self.yVel *= 0.9

        # Screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
            if self.xVel < 0:
                self.xVel = 0
        if self.rect.top < 0:
            self.rect.top = 0
            if self.yVel < 0:
                self.yVel = 0
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
            if self.xVel > 0:
                self.xVel = 0
        if self.rect.bottom > screen.get_height():
            self.rect.bottom = screen.get_height()
            if self.yVel > 0:
                self.yVel = 0
    
    # Collision detection
    def hitsSprite(self, other):
        return (
            self.rect.left < other.rect.right and
            self.rect.right > other.rect.left and
            self.rect.top < other.rect.bottom and
            self.rect.bottom > other.rect.top
        )
    ### Old Code with corner detection ###
    # collided = False
    # sprite1Corners = [
    #     (sprite1.rect.bottomleft),
    #     (sprite1.rect.bottomright),
    #     (sprite1.rect.topleft),
    #     (sprite1.rect.topright)
    # ]
    # for i in sprite1Corners:
    #     if (
    #         i[0] > sprite2.rect.left and 
    #         i[0] < sprite2.rect.right and 
    #         i[1] > sprite2.rect.top and 
    #         i[1] < sprite2.rect.bottom
    #     ):
    #             collided =  True
    # return collided
    def resize(self, width, height):
        # self.image = pygame.transform.flip(self.inverted, True, False)
        self.image = pygame.transform.scale(
            self.baseImg, 
            (
                (width), 
                (height)
            )
        )
        self.inverted = pygame.transform.flip(self.image, True, False)
        self.fadedImage = pygame.transform.grayscale(self.image)
        self.fadedInversion = pygame.transform.grayscale(self.inverted)

        old_center = self.rect.center  # save before changing image
        self.rect = self.image.get_rect()
        self.rect.center = old_center  # restore after
    
    def setVisible(self, visible: bool):
        if visible:
            spriteList.add(self)
        else:
            spriteList.remove(self)


# Text Sprite List
textSpriteList = pygame.sprite.Group()

# Text Sprite setups
class textSprite(pygame.sprite.Sprite):
    def __init__(self, startText: str, x: int, y: int):
        super().__init__()
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.image = self.font.render(startText, True, (255, 255, 255), (0, 0, 0))
        self.rect = self.image.get_rect()
        spriteList.add(self)
        textSpriteList.add(self)
        self.name = startText
        self.rect.topleft = x, y
    # Pos Updater
    def setPos(self, x, y):
        self.rect.left = x
        self.rect.top = y
    # Relabeler
    def relabel(self, newText: str):
        X, Y = self.rect.topleft
        self.image = self.font.render(newText, True, (255, 255, 255), (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (X, Y)
    # To fix a loop through sprites
    def tick(self):
        pass
    def setVisible(self, visible: bool):
        if visible:
            spriteList.add(self)
        else:
            spriteList.remove(self)
