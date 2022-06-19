import pygame


class Paddle():
    def __init__(self, coords) -> None:
        self.shape = pygame.Rect(0, 0, 10, 100)
        self.center = coords
