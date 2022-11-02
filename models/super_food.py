import pygame
from pygame.locals import *
import random

from screens.game import SIZE

class SuperFood:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/golden.png").convert_alpha() 
        self.x = 350
        self.y = 350
        self.show = False

    def draw(self):
        if self.show:
            self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE
    
    def randomize_show(self):
        if not self.show:
            rand = random.randint(1,5)
            if rand == 1:
                self.show = True
                self.move()