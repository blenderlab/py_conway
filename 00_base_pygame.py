#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jan 2021

@author: thomas Hocedez
"""

# loading the  libraries
import numpy
import pygame


#Start pyGame Engine :
pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1500)

# program running ? 
play=True

while play==True:
	# Check if we want to exit :
    for event in pygame.event.get():
        if pygame.event.get(pygame.QUIT):
            break
        if event.type == pygame.KEYDOWN:
            # if key "q" pressed :
            if event.key == pygame.K_q:
                # set running to false :
                play=False
	# Let's clean the screen :
    screen.fill(pygame.color.Color('white'))
    # insert drawing stuff here :
        
        
    # flip screen (to update display)
    pygame.display.flip()
    # set FPS to 3 
    clock.tick(3)

pygame.quit()


