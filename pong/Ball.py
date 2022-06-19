import pygame
import random
WIDTH, HEIGHT = 1280, 720


class Ball():
    def __init__(self) -> None:
        self.object = pygame.Rect(0, 0, 20, 20)
        self.object.center = (1280/2, 720/2)
        self.velocity = [1, 1]  # [x, y]

    def check_collision(self, player_paddle, opponent_paddle):
        if self.object.y >= HEIGHT:
            self.velocity[1] = -1
        if self.object.y <= 0:
            self.velocity[1] = 1
        if self.object.x <= 0:
            player_score += 1
            self.object.center = (WIDTH/2, HEIGHT/2)
            self.velocity[0], self.velocity[1] = random.choice(
                [1, -1]), random.choice([1, -1])
        if self.object.x >= WIDTH:
            opponent_score += 1
            self.object.center = (WIDTH/2, HEIGHT/2)
            self.velocity[0], self.velocity[1] = random.choice(
                [1, -1]), random.choice([1, -1])
        if player_paddle.x - self.object.width <= self.object.x <= player_paddle.right and self.object.y in range(player_paddle.top-self.object.width, player_paddle.bottom+self.object.width):
            self.velocity[0] = -1
        if opponent_paddle.x - self.object.width <= self.object.x <= opponent_paddle.right and self.object.y in range(opponent_paddle.top-self.object.width, opponent_paddle.bottom+self.object.width):
            self.velocity[0] = 1
