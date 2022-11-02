import pygame
import sys

from global_variables import *
from pygame.locals import *

class GameOverScreen():
    def __init__(self, scores):
        self.scores = scores

    def show(self):
        SCREEN.fill(BACKGROUND_COLOR)
        
        font_big = pygame.font.Font("resources/font.ttf", 30)       
        font_small = pygame.font.Font("resources/font.ttf", 25)

        line1 = font_big.render("--------- GAME OVER! ---------", True, FONT_COLOR)
        line1_rect = line1.get_rect(center=(1000/2, 200))
        SCREEN.blit(line1, line1_rect)

        line2 = font_small.render(f"LAST SCORE: {self.scores.last_score}",  True, FONT_COLOR)
        line2_rect = line2.get_rect(center=(1000/2, 250))
        SCREEN.blit(line2, line2_rect)

        line3 = font_big.render(f"HIGHEST SCORES:",  True, FONT_COLOR)
        line3_rect = line3.get_rect(center=(1000/2, 300))
        SCREEN.blit(line3, line3_rect)
    
        scores_list = self.scores.get_list_strings_top_5()
        y_line = 350
        for line in scores_list:
            line_rect = line.get_rect(center=(1000/2, y_line))
            SCREEN.blit(line, line_rect)
            y_line += 50

        pygame.display.flip()

        running = True
        while running:

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

            pygame.display.update()
            CLOCK.tick(60)