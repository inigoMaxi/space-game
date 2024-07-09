import pygame
from pygame import mixer
from src.bullet import Bullet
from src.resource_manager import SingletonMeta


class State(metaclass=SingletonMeta):
    def handle_event(self, event):
        pass

    def update(self):
        pass

    def render(self, display):
        pass


class GameOverState(State):
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 40)

    def render(self, display):
        text_game_over = self.font.render("JUEGO TERMINADO", True, (255, 255, 255))
        display.blit(text_game_over, (205, 250))


class PlayState(State):
    def __init__(self, game):
        self.game = game

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.game.player.move(-0.3)
            if event.key == pygame.K_RIGHT:
                self.game.player.move(0.3)
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('sounds/shoot.mp3')
                bullet_sound.play()
                self.game.bullets.append(Bullet(self.game.player.x))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.game.player.move(0)

    def update(self):
        self.game.player.update()
        if self.game.player.x <= 0:
            self.game.player.x = 0
        elif self.game.player.x >= 736:
            self.game.player.x = 736

        for enemy in self.game.enemies:
            if enemy.y > 500:
                for en in self.game.enemies:
                    en.y = 1000
                self.game.set_state(GameOverState())
                return

            enemy.update()
            for bullet in self.game.bullets:
                if bullet.is_collision(enemy):
                    collision_sound = mixer.Sound('sounds/collision.mp3')
                    collision_sound.play()
                    self.game.bullets.remove(bullet)
                    self.game.score += 1
                    enemy.reset()

        for bullet in self.game.bullets:
            bullet.update()
            if bullet.y < 0:
                self.game.bullets.remove(bullet)

    def render(self, display):
        self.game.display.blit(self.game.img_background, (0, 0))
        self.game.player.draw(display)
        for enemy in self.game.enemies:
            enemy.draw(display)
        for bullet in self.game.bullets:
            bullet.draw(display)
        self.game.show_score(display)
