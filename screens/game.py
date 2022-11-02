import pygame
from global_variables import *

import models.food as food
import models.snake as snake
import models.scores as scores
import models.player as player
import models.super_food as super_food

from screens.game_over import GameOverScreen

from pygame.locals import *
import time

class Game:
    def __init__(self, player):
        pygame.init()
        pygame.display.set_caption("Snake game")

        pygame.mixer.init()
        self.play_background_music()

        self.sleep_time = 0.2

        self.snake = snake.Snake(SCREEN)
        self.snake.draw()
        
        self.food = food.Food(SCREEN)
        
        self.super_food = super_food.SuperFood(SCREEN)

        self.scores = scores.Scores(player)

        self.player = player

    def play_background_music(self):
        pygame.mixer.music.load("resources/background.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1, 0)
        pass

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound("resources/impact.ogg")
            sound.set_volume(1)
        elif sound_name == "food":
            sound = pygame.mixer.Sound("resources/food.ogg")
            sound.set_volume(0.2)
        elif sound_name == "power_up":
            sound = pygame.mixer.Sound("resources/powerUp.ogg")
            sound.set_volume(0.3)

        pygame.mixer.Sound.play(sound)


    def reset(self):
        self.snake = snake.Snake(SCREEN)
        self.food = food.Food(SCREEN)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and  x1 < x2 + SIZE:
            if y1 >= y2 and  y1 < y2 + SIZE:
                return True
        return False

    def play(self):
        SCREEN.fill(BACKGROUND_COLOR)
        self.food.draw()
        self.super_food.draw()

        self.snake.walk()

        self.display_score()
        self.control_sleep_time()

        pygame.display.flip()

        # collision with food
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
            self.play_sound("food")
            self.snake.increase_length(1)
            self.food.move()
            self.super_food.randomize_show()

        # collision with super food
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.super_food.x, self.super_food.y):
            self.play_sound("power_up")
            self.snake.increase_length(5)
            self.super_food.show = False

        # collision with itselfs
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise "Collision Ocurred"

    def display_score(self):
        font = pygame.font.Font("resources/font.ttf", 30)
        score = font.render(f"SCORE: {self.snake.length}", True, FONT_COLOR)
        SCREEN.blit(score, (800,10))
    
    def control_sleep_time(self):
        snake_size = self.snake.length

        if snake_size < 5:
            self.sleep_time = 0.2
        elif snake_size < 10:
            self.sleep_time = 0.17
        elif snake_size < 15:
            self.sleep_time = 0.13
        else:
            self.sleep_time = 0.1

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.scores.set_last_score(self.snake.length)
                gameOver = GameOverScreen(self.scores)
                gameOver.show()
                self.reset()

            time.sleep(self.sleep_time)
