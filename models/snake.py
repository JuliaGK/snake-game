import random
import pygame
from pygame.locals import *

from screens.game import SIZE

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.color = self.randomize_color()
        self.block_head = pygame.image.load(f"resources/snake/{self.color}/head_down.png").convert_alpha()
        self.block_tail = pygame.image.load(f"resources/snake/{self.color}/body_down.png").convert_alpha() 
        self.direction = "down"
        self.increase = 0
        self.length = 1
        self.x = [40]
        self.y = [40]
        
    def move_left(self):
        self.direction = "left"
        self.block_head = pygame.image.load(f"resources/snake/{self.color}/head_left.png").convert_alpha()
        self.block_tail = pygame.image.load(f"resources/snake/{self.color}/body_left.png").convert_alpha() 
    
    def move_right(self):
        self.direction = "right"
        self.block_head = pygame.image.load(f"resources/snake/{self.color}/head_right.png").convert_alpha()
        self.block_tail = pygame.image.load(f"resources/snake/{self.color}/body_right.png").convert_alpha() 

    def move_up(self):
        self.direction = "up"
        self.block_head = pygame.image.load(f"resources/snake/{self.color}/head_up.png").convert_alpha()
        self.block_tail = pygame.image.load(f"resources/snake/{self.color}/body_up.png").convert_alpha() 

    def move_down(self):
        self.direction = "down"
        self.block_head = pygame.image.load(f"resources/snake/{self.color}/head_down.png").convert_alpha()
        self.block_tail = pygame.image.load(f"resources/snake/{self.color}/body_down.png").convert_alpha() 

    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == "up":
            self.y[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE
        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "right":
            self.x[0] += SIZE

        self.check_border()

        self.draw()

    def check_border(self):
        if self.x[0] < 0:
            self.x[0] = 960
        if self.x[0] >= 1000:
            self.x[0] = 0
        if self.y[0] < 0:
            self.y[0] = 760
        if self.y[0] >= 800:
            self.y[0] = 0

    def draw(self):
        if self.increase > 0:
            self.x.append(-40)
            self.y.append(-40)
            self.increase -= 1
            self.length += 1 

        for i in range(self.length):
            if i == 0:
                self.parent_screen.blit(self.block_head, (self.x[i],self.y[i]))
            else:
                self.parent_screen.blit(self.block_tail, (self.x[i],self.y[i]))
    
    def increase_length(self, blocks):
        self.increase += blocks
    
    def randomize_color(self):
        rand = random.randint(1,2)
        if rand == 1:
            return "orange"
        else:
            return "blue"