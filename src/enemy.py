import pygame
import random


class Enemy:
    def __init__(self):
        self.img = pygame.image.load("images/enemy.png")
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 200)
        self.move_x = 0.3
        self.move_y = 50

    def update(self):
        self.x += self.move_x
        if self.x <= 0:
            self.move_x = 0.3
            self.y += self.move_y
        elif self.x >= 736:
            self.move_x = -0.3
            self.y += self.move_y

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))

    def reset(self):
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 200)
        self.move_x = 0.3
        self.move_y = 50
