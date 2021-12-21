import os
import pygame

# Loads spaceship image
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

# Scales spaceship image
SPACESHIP = pygame.transform.scale(SPACESHIP_IMAGE, (150, 150))
