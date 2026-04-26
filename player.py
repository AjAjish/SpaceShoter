import pygame
from settings import PLAYER_SPEED

class Player:
    def __init__(self,image):
        self.image = image
        self.x = 368
        self.y = 480
        self.velocity = 0

    def move(self):
        self.x += self.velocity
        self.x = max(0, min(self.x, 736))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))