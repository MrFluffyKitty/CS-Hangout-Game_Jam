import os
import pygame

WIDTH, HEIGHT = 700, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Failure is Inevitable')

PURPLE = (50, 40, 110)

FPS = 60
SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'Spaceship', 'Spaceship-shooter-environment',
                                           'Spaceship-shooter-environment', 'spritesheets', 'ship.png'))
SPACESHIP = pygame.transform.scale(SPACESHIP_IMAGE, (150, 150))


def draw_window():
    WINDOW.fill(PURPLE)
    WINDOW.blit(SPACESHIP, (320, 550))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
