import os
import pygame


class Player (pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):    
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load(
            os.path.join("game_jam","Assets",
                'Spaceship','ship','ship3.png')))
        self.sprites.append(pygame.image.load(
            os.path.join("game_jam","Assets",
                'Spaceship','ship','ship4.png')))
        self.sprites.append(pygame.image.load(
            os.path.join("game_jam","Assets",
                'Spaceship','ship','ship5.png')))
        self.sprites.append(pygame.image.load(
            os.path.join("game_jam","Assets",
                'Spaceship','ship','ship6.png')))
        self.sprites.append(pygame.image.load(
            os.path.join("game_jam","Assets",
                'Spaceship','ship','ship7.png')))
        self.sprites.append(pygame.image.load(
            os.path.join("game_jam","Assets",
                'Spaceship','ship','ship8.png')))
        self.sprites.append(pygame.image.load(
            os.path.join("game_jam","Assets",
                'Spaceship','ship','ship9.png')))
        self.sprites.append(pygame.image.load(
            os.path.join("game_jam","Assets",
                'Spaceship','ship','ship10.png')))
        self.sprites.append(pygame.image.load(
            os.path.join("game_jam","Assets",
                'Spaceship','ship','ship1.png')))
        self.sprites.append(pygame.image.load(
            os.path.join("game_jam","Assets",
                'Spaceship','ship','ship2.png')))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    
    
    def animate(self):
        self.is_animating = True

    
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2
            
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            
            self.image = self.sprites[int(self.current_sprite)]
