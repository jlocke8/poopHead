#!/usr/bin/python3
import pygame
import sys
from pygame.locals import *


pygame.init()
screenSize = width, height = 1024, 786
flags=pygame.RESIZABLE 
screen = pygame.display.set_mode(screenSize,flags)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250,250,250))

titleobject = pygame.font.Font(None, 36)
text = titleobject.render("Hello World", 1, (10, 10, 10))
textpos = text.get_rect(centerx=background.get_width()/2)
background.blit(text, textpos)

screen.blit(background, (0,0))

pygame.display.set_caption("Poop On Head")


class player:
    playerImage = pygame.image.load("pigeonStand.png")
    xpos = 0
    ypos = 0
    xdelta = 0
    ydelta = 0
    speed = 1.5

    def blitPlayer(self, x,y):
        screen.blit(self.playerImage, (x,y))
    
    

player1 = player()



running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit(0)
    keys = pygame.key.get_pressed()
    player1.xpos += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])*player1.speed
    player1.ypos += (keys[pygame.K_DOWN] - keys[pygame.K_UP])*player1.speed
       
   #    if event.type == pygame.KEYDOWN:
   #         if event.key == pygame.K_LEFT:
   #             player1.xdelta = -1.5
   #         if event.key == pygame.K_RIGHT:
   #             player1.xdelta = 1.5
   #         if event.key == pygame.K_UP:
   #             player1.ydelta = -1.5
   #         if event.key == pygame.K_DOWN:
   #             player1.ydelta = 1.5
   #     if event.type == pygame.KEYUP:
   #         if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
   #             player1.xdelta = 0
   #         if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
   #             player1.ydelta = 0
   # player1.xpos += player1.xdelta
   # player1.ypos += player1.ydelta
    player1.blitPlayer(player1.xpos, player1.ypos) 





