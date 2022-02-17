import pygame
import math
from math import sin, cos, degrees, atan, pi
import os
from constants import *
from Game import *
import time

class Ball():
    def __init__(self, pos_x, pos_y):

#determining the x and y position of the ball
        self.pos_x = pos_x
        self.pos_y = pos_y

#sets the dimensions of the ball
        self.width = 20
        self.length = 20

#sets velocity of the ball
        self.velocityY = 1
        self.velocityX = 1

    def update (self):

#resets the ball if the ball hits the right or left side of the screen       
        self.pos_x += self.velocityX
        self.pos_y += self.velocityY
        
        if self.pos_x < 0:
            self.reset()
        elif self.pos_x > SCREEN_SIZE[0] - self.length:
            self.reset()
#when the ball hits the top and bottom, change direction of the ball        
        if self.pos_y < 0:
            self.velocityY = 1
        elif self.pos_y > SCREEN_SIZE[1] - self.width:
            self.velocityY = -1
    def draw_ball(self, screen):
        pygame.draw.rect(screen,[255,255,255],[self.pos_x, self.pos_y, self.width, self.length])
    
    def reset (self):
        self.pos_x = SCREEN_SIZE[0]/2
        self.pos_y = SCREEN_SIZE[1]/2
        time.sleep(1)