import os
import pygame

SPACESHIP_IMAGE = pygame.image.load(
    os.path.join(
        "game_jam",
        "Assets",
        "Spaceship",
        "Spaceship-shooter-environment",
        "Spaceship-shooter-environment",
        "spritesheets",
        "ship.png",
    )
)

SPACESHIP = pygame.transform.scale(SPACESHIP_IMAGE, (150, 150))
