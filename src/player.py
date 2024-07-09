import pygame


class Player:
    def __init__(self):
        self.img = pygame.image.load("images/player.png")
        self.x = 368
        self.y = 500
        self.move_x = 0

    def move(self, dx):
        self.move_x = dx

    def update(self):
        self.x += self.move_x

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))
