import pygame
import sys

from global_variables import *
from pygame.locals import *

class EndScreen():
    def __init__(self, scores):
        self.scores = scores
        self.background = pygame.image.load("resources/end_screen.png")

    def show(self):

        SCREEN.blit(self.background,(0,0))

        # Last score
        font_last_score = pygame.font.Font("resources/font.ttf", 37)

        last_score_line = font_last_score.render(f"{self.scores.last_score}",  True, FONT_COLOR)
        last_score_rect = last_score_line.get_rect(center=(700, 580))
        SCREEN.blit(last_score_line, last_score_rect)

        # Play again rect
        button_play = pygame.Rect(340,100,340,100)
        button_play.center = (1000/2, 685)
        
        # Highest scores
        scores_list = self.scores.get_list_strings_top_5()
        y_line = 300
        
        for line in scores_list:
            SCREEN.blit(line, (340, y_line))
            y_line += 43

        
        click = False
        running = True
        while running:

            # Button play mechanic
            mx, my = pygame.mouse.get_pos()
            if button_play.collidepoint((mx,my)):
                if click:
                    running = False

            click = False

            # Event input
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit() 
                    if event.key == K_SPACE:
                        running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            CLOCK.tick(60)