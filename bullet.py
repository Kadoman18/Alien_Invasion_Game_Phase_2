"""
Program Name: bullet.py

Author: Shrrayash Srinivasan

Purpose: Defined the Bullet class with the use of the Sprite system. It is an important part of the alien ship firing mechanism and
the bullets fire out of the ship and the code is done specifically to track the movement and speed of the lasers.

Date: November 16, 2025
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lab12_ssrinivasan3 import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion', position, direction):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load and scale bullet image
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        # Rotate bullet to match horizontal firing direction
        if direction == 1:   # moving right
            self.image = pygame.transform.rotate(self.image, -90)
        else:                # moving left
            self.image = pygame.transform.rotate(self.image, 90)

        # Position bullet at ship’s firing point (slightly offset from center)
        self.rect = self.image.get_rect(center=position)
        if direction == 1:
            self.rect.left = position[0]  # nose of ship on left side
        else:
            self.rect.right = position[0] # nose of ship on right side

        # Track position as float for smooth movement
        self.x = float(self.rect.x)

        # Direction: +1 for rightward (ship on left), -1 for leftward (ship on right)
        self.direction = direction
        self.speed = self.settings.bullet_speed

    def update(self):
        # Move bullet horizontally
        self.x += self.speed * self.direction
        self.rect.x = self.x

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)

