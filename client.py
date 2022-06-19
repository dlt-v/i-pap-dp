import pygame
from network import Network
from Player import Player

width = 500
height = 500
window = pygame.display.set_mode((width, height))

pygame.display.set_caption("client")

client_number = 0


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
