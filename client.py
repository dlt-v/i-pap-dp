import pygame


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

        self.rect = (self.x, self.y, self.width, self.height)


def redraw_window(player):
    window.fill((255, 255, 255))
    player.draw(window)
    pygame.display.update()


def main():
    run = True
    player = Player(50, 50, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player.move()
        redraw_window(player)


main()
