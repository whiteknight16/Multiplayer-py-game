import pygame
from network import Network
from player import Player

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game Window")


def redraw_window(win, player,player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p=n.get_p()
    while run:
        p2=n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redraw_window(win, p,p2)


main()
