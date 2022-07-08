import pygame
import sys
import random


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (100, 185, 0)
        self.score = 0
        self.highscore = 0

    def get_head_position(self):
        return self.positions[0]

class Food:
