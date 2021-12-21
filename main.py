import os
import pygame
import time
from spaceship import *

WIDTH, HEIGHT = 700, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Failure is Inevitable")

BLACK = (0, 0, 0)
FPS = 60

moving_sprites = pygame.sprite.Group()
player = Player(320, 480)
moving_sprites.add(player)

def draw_window():
    moving_sprites.draw(WINDOW)
    moving_sprites.update()
    pygame.display.flip()
    pygame.display.update()

def main():

    BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(
        'game_jam', 'Assets', 'Background', 'Galaxy_bg', 
        'Purple_Nebula', 'PN1.png')), (700, 700)).convert()

    # Background coordinate (y)
    y = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                player.animate()

        WINDOW.fill(BLACK)

        rel_y = y % BACKGROUND.get_rect().height
        WINDOW.blit(BACKGROUND, (0, rel_y - BACKGROUND.get_rect().height))
        if rel_y < HEIGHT:
            WINDOW.blit(BACKGROUND, (0, rel_y))
        # Scrolls background on y-axis
        y += 1
        draw_window()
        pygame.display.update()

if __name__ == "__main__":
    main()
