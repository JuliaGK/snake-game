import pygame
import numpy as np
from pygame.locals import *
import csv
from global_variables import *

class Scores():
    def __init__(self, player):
        self.highest_scores = []
        self.populate_scores_from_file()
        self.player = player
        self.last_score = 0

    def save_scores_file(self):
        with open("scores.csv", "w") as file:
            for value in self.highest_scores:
                file.write(f"{str(value[0])},{value[1]}\n")
        
    def update_scores_list(self, score):
        if len(self.highest_scores) < 5:
            self.highest_scores.append([score, self.player.name])
            self.highest_scores = np.array(self.highest_scores)
            self.highest_scores = self.highest_scores[self.highest_scores[:,0].argsort()][::-1]
            self.highest_scores = self.highest_scores.tolist()
            self.save_scores_file()

        elif score > int(min(self.highest_scores)[0]):
            self.highest_scores.remove(min(self.highest_scores))
            self.highest_scores.append([score, self.player.name])
            self.highest_scores = np.array(self.highest_scores)
            self.highest_scores = self.highest_scores[self.highest_scores[:,0].argsort()][::-1]
            self.highest_scores = self.highest_scores.tolist()
            self.save_scores_file()
    
    def populate_scores_from_file(self):
        with open("scores.csv", "r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                self.highest_scores.append([int(row[0]), row[1]])
        self.highest_scores.sort(reverse=True)

    def get_list_strings_top_5(self):
        font = pygame.font.Font("resources/font.ttf", 40)
        top_5 = []
        with open("scores.csv", "r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                score = self.format_score(str(row[0]))
                top_5.append(font.render(f"{score} {row[1]}", True, FONT_COLOR))
        return top_5
    
    def format_score(self, score):
        if len(score) == 1:
            return f"00{score}"
        elif len(score) == 2:
            return f"0{score}"
        else:
            return f"{score}"

    def set_last_score(self, score):
        self.last_score = score
        self.update_scores_list(score)