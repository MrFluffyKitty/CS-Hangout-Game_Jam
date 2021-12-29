import pygame
import os
import time
from spaceship import *
from pygame.locals import *


# constants
WIDTH, HEIGHT = 700, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Failure is Inevitable")
BLACK = (0, 0, 0)
FPS = 60
VEL = 4
p_x = 330
p_y = 650
width = 50
height = 50
movement = False

# player perameters


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite = [pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship3.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship4.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship5.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship6.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship7.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship8.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship9.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship10.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship1.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship2.png'))]
        self.current_sprite = 0
        self.image = self.sprite[self.current_sprite]

        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT-100))

    def update(self):
        self.current_sprite += 0.3
        if self.current_sprite >= len(self.sprite):
            self.current_sprite = 0
        self.image = self.sprite[int(self.current_sprite)]
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

# bullet perameters


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join('game_jam', 'Assets',
                         'Laser Animations', 'laser1.png'))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.y -= 5

        if self.rect.y <= 0:
            self.kill()


# player and bullet groups
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
pygame.mouse.set_visible(False)
bullet_group = pygame.sprite.Group()

# main function


def main():

    # background image
    BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(
        'game_jam', 'Assets', 'Background', 'Galaxy_bg',
        'Purple_Nebula', 'PN1.png')), (WIDTH, HEIGHT)).convert()

    # variables
    clock = pygame.time.Clock()
    run = True
    y = 0


# constants
WIDTH, HEIGHT = 700, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Failure is Inevitable")
BLACK = (0, 0, 0)
FPS = 60
VEL = 4
p_x = 330
p_y = 650
width = 50
height = 50
movement = False

# player perameters


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite = [pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship3.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship4.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship5.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship6.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship7.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship8.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship9.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship10.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship1.png')),
                       pygame.image.load(
            os.path.join("game_jam", "Assets",
                         'Spaceship', 'ship', 'ship2.png'))]
        self.current_sprite = 0
        self.image = self.sprite[self.current_sprite]

        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT-100))

    def update(self):
        self.current_sprite += 0.3
        if self.current_sprite >= len(self.sprite):
            self.current_sprite = 0
        self.image = self.sprite[int(self.current_sprite)]
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

# bullet perameters


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join('game_jam', 'Assets',
                         'Laser Animations', 'laser1.png'))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.y -= 5

        if self.rect.y <= 0:
            self.kill()


# player and bullet groups
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
pygame.mouse.set_visible(False)
bullet_group = pygame.sprite.Group()

# main function


def main():

    # background image
    BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(
        'game_jam', 'Assets', 'Background', 'Galaxy_bg',
        'Purple_Nebula', 'PN1.png')), (WIDTH, HEIGHT)).convert()


    # variables
    # Initializes mixer
    pygame.mixer.init()

    # Grabs sound file
    pygame.mixer.music.load(os.path.join(
        'game_jam', 'Assets', 'Sounds', 'spaceship_music', 'Far-Out_OST', 'OST', 'Far-Out-Hurry_Up.wav'))

    # Plays music indefinitely
    pygame.mixer.music.play(-1)

    # Sets music volume
    pygame.mixer.music.set_volume(0.3)
    
    clock = pygame.time.Clock()
    run = True
    y = 0

    # music
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(
        'game_jam', 'Assets', 'Sounds', 'Far Out Hurry Up.wav'))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    # run
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet_group.add(player.create_bullet())

            if event.type == pygame.KEYDOWN:
                player.animate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False


        # updates backgroud for scrolling effect
        WINDOW.fill(BLACK)
        rel_y = y % BACKGROUND.get_rect().height
        WINDOW.blit(BACKGROUND, (0, rel_y - BACKGROUND.get_rect().height))
        if rel_y < HEIGHT:
            WINDOW.blit(BACKGROUND, (0, rel_y))
        y += 1

        # update screen
        bullet_group.draw(WINDOW)
        bullet_group.update()
        player_group.draw(WINDOW)
        player_group.update()
        pygame.display.update()


# starts main function
if __name__ == "__main__":
    main()
main.py
