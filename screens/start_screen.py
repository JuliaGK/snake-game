import sys
import pygame
import screens.game
from models.player import *

from global_variables import *
from pygame.locals import *

pygame.init()
pygame.display.set_caption("SNAKE")

class StartScreen():
    def __init__(self):
        self.player_name = ""
        self.background = pygame.image.load("resources/menu.png")
    def show(self) -> str:

        font_big = pygame.font.Font("resources/font.ttf", 45)        

        click = False
        running = True
        while running:

            SCREEN.blit(self.background,(0,0))
            
            mx, my = pygame.mouse.get_pos()

            button_play = pygame.Rect(340,100,340,100)
            button_play.center = (1000/2, 685)

            if button_play.collidepoint((mx,my)):
                if click:
                    running = False
                    print(self.player_name)
                    player = Player(self.player_name)
                    gameScreen = screens.game.Game(player)
                    gameScreen.run()
                    click = False

            click = False
            
         #  pygame.draw.rect(SCREEN, (255, 255, 255, 0), button_play)

            player_name_line = font_big.render(self.player_name, True, FONT_COLOR)
            player_name_rect = player_name_line.get_rect(center=(1000/2, 520))
            
            SCREEN.blit(player_name_line, player_name_rect)
            

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    else:
                        self.player_name += event.unicode 
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                
            pygame.display.update()
            CLOCK.tick(60)