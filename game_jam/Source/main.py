import os  # File navigation
import pygame
from background import BACKGROUND
from spaceship import SPACESHIP_IMAGE, SPACESHIP


WIDTH, HEIGHT = 700, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # Creates window
pygame.display.set_caption("Failure is Inevitable")  # Title

BLACK = (0, 0, 0)

FPS = 60


def draw_window():  # Draws window and loads assets/updates accordingly
    WINDOW.fill(BLACK)
    WINDOW.blit(BACKGROUND, (0, 0))
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


if __name__ == "__main__":
    main()
