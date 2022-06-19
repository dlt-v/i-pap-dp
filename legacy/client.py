import pygame
from network import Network
from Player import Player

width = 500
height = 500
window = pygame.display.set_mode((width, height))

pygame.display.set_caption("client")


def redraw_window(window, player, player2):
    window.fill((255, 255, 255))
    player2.draw(window)
    player.draw(window)
    pygame.display.update()


def main():
    run = True
    n = Network()
    player = n.get_p()

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        player2 = n.send(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player.move()
        redraw_window(window, player, player2)


main()
