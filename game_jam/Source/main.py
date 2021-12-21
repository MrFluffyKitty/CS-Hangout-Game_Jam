import os  # File navigation
import pygame
from spaceship import SPACESHIP_IMAGE, SPACESHIP

WIDTH, HEIGHT = 700, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # Creates window
pygame.display.set_caption("Failure is Inevitable")  # Title

BLACK = (0, 0, 0)

FPS = 60


def main():
    # Sets background image
    BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(
        'game_jam', 'Assets', 'Background', 'Galaxy_bg', 'Purple_Nebula', 'PN1.png')), (700, 700)).convert()

    # Background coordinate (y)
    y = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WINDOW.fill(BLACK)

        # Ensures that rel_y never goes over/under height of image
        rel_y = y % BACKGROUND.get_rect().height

        # Renders background
        WINDOW.blit(BACKGROUND, (0, rel_y - BACKGROUND.get_rect().height))

        # Keeps background img on screen
        if rel_y < HEIGHT:
            WINDOW.blit(BACKGROUND, (0, rel_y))

        # Scrolls background on y-axis
        y += 1

        # Renders spaceship sprite
        WINDOW.blit(SPACESHIP, (320, 550))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
