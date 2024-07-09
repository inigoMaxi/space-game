import pygame


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ResourceManager(metaclass=SingletonMeta):
    def __init__(self):
        self.resources = {}

    def load(self, name, path):
        self.resources[name] = pygame.image.load(path)

    def get(self, name):
        return self.resources[name]
