import random
from settings import ENEMY_SPEED

class Enemy:
    def __init__(self,image):
        self.image = image
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        self.x_change = ENEMY_SPEED
        self.y_change = 40

    def move(self):
        self.x += self.x_change

        if self.x <= 0 or self.x >= 736:
            self.x_change *= -1
            self.y += self.y_change

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))