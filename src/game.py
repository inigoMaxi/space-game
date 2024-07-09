import pygame
from pygame import mixer
from src.resource_manager import ResourceManager
from src.player import Player
from src.enemy import Enemy
from src.bullet import Bullet
from src.state import PlayState, GameOverState


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Invasión Espacial")
        self.resource_manager = ResourceManager()
        self.resource_manager.load("icon", "images/ufo.png")
        pygame.display.set_icon(self.resource_manager.get("icon"))
        self.resource_manager.load("background", "images/background.jpg")
        self.img_background = self.resource_manager.get("background")
        mixer.music.load('sounds/music.mp3')
        mixer.music.play(-1)
        self.player = Player()
        self.enemies = [Enemy() for _ in range(8)]
        self.bullets = []
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.state = PlayState(self)

    def set_state(self, state):
        self.state = state

    def show_score(self, display):
        text = self.font.render(f"Puntaje: {self.score}", True, (255, 255, 255))
        display.blit(text, (10, 10))

    def run(self):
        while isinstance(self.state, PlayState) or isinstance(self.state, GameOverState):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = None
                else:
                    self.state.handle_event(event)

            self.state.update()
            self.state.render(self.display)
            pygame.display.update()
