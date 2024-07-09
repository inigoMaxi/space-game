import pygame
import math


class Bullet:
    def __init__(self, x):
        self.img = pygame.image.load("images/bullet.png")
        self.x = x + 16
        self.y = 500
        self.velocity = -1

    def update(self):
        self.y += self.velocity

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))

    def is_collision(self, enemy):
        distance = math.sqrt(math.pow((enemy.x - self.x), 2) + math.pow((enemy.y - self.y), 2))
        return distance < 27
