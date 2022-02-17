import pygame
import math
import os
from constants import *

class Player():
    def __init__(self, pos_x, pos_y):
#determining the x and y position of the paddle
        self.pos_x = pos_x
        self.pos_y = pos_y

#sets the dimensions of the paddle
        self.width = 20
        self.length = 70

#the velocity of the paddle
        self.velocity_y = 0

#the change of position based of the velocity of the paddle   
    def update(self):
        self.pos_y += self.velocity_y
        if self.pos_y < 0:
            self.pos_y = 0
        elif self.pos_y > SCREEN_SIZE[1] - self.length:
            self.pos_y = SCREEN_SIZE[1] - self.length
#the velocity when paddle moves up and down
    def moveup(self):
        self.velocity_y = -2
    def movedown(self):
        self.velocity_y = 2
#draws the paddle on the screen
    def draw_paddle(self, screen):
        pygame.draw.rect(screen, [255,255,255], [self.pos_x, self.pos_y, self.width, self.length])
