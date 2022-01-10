import pygame
from pygame.locals import *
import sys
import random
import time
from tkinter import filedialog
from tkinter import *

#https://coderslegacy.com/python/pygame-rpg-code-review1/

pygame.init()

#Declaring variables
vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 700
FPS = 12
FPS_CLOCK = pygame.time.Clock()

#game assets
Ground_image_path = 'm/Ground.png'
Background_image_path = 'm/Background.png'

#game assets players
Wind_hashashin_image_stand_paths = ['m/wind_hashashin/stand/frame_' + str(x) + '_delay-0.1s.png' for x in range(1,7)]
Wind_hashashin_standing_imgs = {}
i = 0
for path in Wind_hashashin_image_stand_paths:
    Wind_hashashin_standing_imgs[i] = pygame.image.load(path)
    i += 1
    
Wind_hashashin_image_attack_paths = ['m/wind_hashashin/attack/07_2_atk-' + str(x) + '-removebg-preview.png' for x in range(1,18)]
Wind_hashashin_attacking_imgs = {}
i = 0
for path in Wind_hashashin_image_attack_paths:
    Wind_hashashin_attacking_imgs[i] = pygame.image.load(path)
    i += 1
    
Wind_hashashin_image_defend_paths = ['m/wind_hashashin/defend/10_defend-' + str(x) + '-removebg-preview.png' for x in range(1,8)]
Wind_hashashin_defending_imgs = {}
i = 0
for path in Wind_hashashin_image_defend_paths:
    Wind_hashashin_defending_imgs[i] = pygame.image.load(path)
    i += 1    
    
Wind_hashashin_image_charge_paths = ['m/wind_hashashin/charge/11_take_hit-' + str(x) + '-removebg-preview.png' for x in range(6)]
Wind_hashashin_charging_imgs = {}
i = 0
for path in Wind_hashashin_image_charge_paths:
    Wind_hashashin_charging_imgs[i] = pygame.image.load(path)
    i += 1  
    
health_image_paths = ['m/health/heart' + str(x) + '.png' for x in range(6)]  
health_imgs = {}
i = 0
for path in health_image_paths:
    health_imgs[i] = pygame.image.load(path)
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
        self.rect = (-150,-35)
        
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = 'RIGHT'
        
        self.attacking = False
        self.defending = False
        self.charging = False
        self.stand_frame = 0
        self.attack_frame = 0
        self.defend_frame = 0
        self.charge_frame = 0
        
        self.health = 5   
        self.atk = 1
        self.state = True
        

    def charge(self):
        if self.charging == False:
            self.charging = True
            self.defending = False
            self.attacking = False
            
        if self.charge_frame > 5:
            self.charge_frame = 0
            
        self.image = Wind_hashashin_charging_imgs[self.charge_frame]
        self.charge_frame += 1           
    
    def attack(self):
        if self.attacking == False:
            self.attacking = True
            self.defending = False
            self.charging = False
            
        if self.attack_frame > 16:
            self.attack_frame = 0
            
        self.image = Wind_hashashin_attacking_imgs[self.attack_frame]
        self.attack_frame += 1
        

            
        
    def defend(self):
        if self.defending == False:
            self.defending = True
            self.attacking = False
            self.charging = False
            
        if self.defending == True:
            if self.defend_frame > 6:
                self.defend_frame = 0
                
            self.image = Wind_hashashin_defending_imgs[self.defend_frame]
            self.defend_frame += 1
        

    
    def update(self):
        if self.stand_frame > 5:
            self.stand_frame = 0
        
        if self.defending == False and self.charging == False and self.attacking == False:
            self.image = Wind_hashashin_standing_imgs[self.stand_frame]
            self.stand_frame += 1
    
     
 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('m/enemy/Enemy.png')
        self.rect = (150,-35)
        self.attacking = False
        self.defending = False
        self.charging = False
        self.health = 5
        self.atk = 1
        self.state = True
        
    def attack(self):
        if self.attacking == False:
            self.attacking = True
            self.defending = False
       
    def defend(self):
        if self.defending == False:
            self.defending = True
            self.attacking = False
               
    def render(self):
        displaysurface.blit(self.image, (550,235))
        
class HealthBar(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.image = health_imgs[5]
        
    def render(self):
        displaysurface.blit(self.image, (10,10))

def fight(m, w):
    if m.health > 0 and w.health > 0:
        # time.sleep(5)
        if m.attacking == True and w.defending == True:
            pass
        if m.attacking == True and w.attacking == True:
            w.health = w.health - m.atk
            m.health = m.health - w.atk
        if m.defending == True and w.attacking == True:
            pass
        if m.defending == True and w.defending == True:
            pass
        if m.charging == True and w.attacking == True:
            pass
        if m.charging == True and w.defending == True:
            m.health = m.health + 1
        else:
            pass
    if m.health <= 0:
        pass
    elif w.health <= 0:
        pass
    
    
        
        
        
#draw all
displaysurface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Game')
background = Background()
ground = Ground()
player = Player()
enemy = Enemy()
health = HealthBar()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.attack()
            if event.key == pygame.K_RIGHT:
                player.defend()
            if event.key == pygame.K_UP:
                player.charge()
                    
        
        

    if player.attacking == True:
        player.attack()
    if player.defending == True:
        player.defend()
    if player.charging == True:
        player.charge()
    
    background.render() 
    ground.render()
    displaysurface.blit(player.image, player.rect)
    enemy.render()
    health.render()
    player.update()
    
    fight(player,enemy)
 
    pygame.display.update() 
    FPS_CLOCK.tick(FPS)

