import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

#https://coderslegacy.com/python/pygame-rpg-code-review1/

pygame.init()

#Declaring variables
vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 700
FPS = 20
FPS_CLOCK = pygame.time.Clock()

#game assets
Ground_image_path = 'm/Ground.png'
Background_image_path = 'm/Background.png'

#game assets players
Wind_hashashin_image_paths = ['m/wind_hashashin/frame_' + str(x) + '_delay-0.1s.png' for x in range(1,7)]
Wind_hashashin_standing_imgs = {}
i = 0
for path in Wind_hashashin_image_paths:
    Wind_hashashin_standing_imgs[i] = pygame.image.load(path)
    i += 1

#Creat
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = pygame.image.load(Background_image_path)
        self.bgY = 0
        self.bgX = 0
    
    def render(self):
        displaysurface.blit(self.bgimage, (self.bgX, self.bgY))
    
 
 
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(Ground_image_path)
        self.rect = self.image.get_rect(center = (350,350))
        
    def render(self):
        displaysurface.blit(self.image, (self.rect.x, self.rect.y))
           
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = Wind_hashashin_standing_imgs[0]
        self.rect = self.image.get_rect()
        
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = 'RIGHT'
        
        self.jump = False
        self.stand_frame = 0
        
        
    def stand(self):
        pass
        
    def move(self):
        pass
    
    def update(self):
        if self.stand_frame > 5:
            self.stand_frame = 0
            return
        
        if self.jump == False:
            self.image = Wind_hashashin_standing_imgs[self.stand_frame]
            self.stand_frame += 1
    
    def attack(self):
        pass
    
    def jump(self):
        pass
     
 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

#draw all
displaysurface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Game')
background = Background()
ground = Ground()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        
        if event.type == pygame.KEYDOWN:
            pass
        
        
    player.update()
    
    background.render() 
    ground.render()
    displaysurface.blit(player.image, player.rect)
 
    pygame.display.update() 
    FPS_CLOCK.tick(FPS)

