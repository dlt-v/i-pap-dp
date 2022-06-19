import pygame
from network import Network

width = 500
height = 500
window = pygame.display.set_mode((width, height))

pygame.display.set_caption("client")

client_number = 0


class Player():
    def __init__(self, x, y, width, height, color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.velocity = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
        if keys[pygame.K_DOWN]:
            self.y += self.velocity
        if keys[pygame.K_UP]:
            self.y -= self.velocity

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str: str):
    '''
    Convert a string into a tuple with player coordinates.
    '''
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup) -> str:
    '''
    Convert a tuple with player coordinates into a string.
    '''
    return f"{tup[0]},{tup[1]}"


def redraw_window(window, player, player2):
    window.fill((255, 255, 255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()


def main():
    run = True
    n = Network()
    start_pos = read_pos(n.get_pos())

    player = Player(start_pos[0], start_pos[1], 100, 100, (0, 255, 0))
    player2 = Player(0, 0, 100, 100, (0, 0, 255))

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        player2_pos = read_pos(n.send(make_pos((player.x, player.y))))
        player2.x = player2_pos[0]
        player2.y = player2_pos[1]
        player2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player.move()
        redraw_window(window, player, player2)


main()
