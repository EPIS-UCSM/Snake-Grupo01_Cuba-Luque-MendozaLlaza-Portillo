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

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * gridsize)) % screen_width), (cur[1] + (y * gridsize)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        if self.highscore <= self.score:
            self.highscore = self.score
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (0, 0, 0), r, 1)


    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width - 1) * gridsize, random.randint(0, grid_height - 1) * gridsize)

