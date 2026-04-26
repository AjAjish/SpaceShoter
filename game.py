import pygame
import math
import random
from player import Player
from enemy import Enemy
from bullet import Bullet
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space Shooter')
        
        self.background = pygame.image.load('assets/background.png')
        self.player = Player(pygame.image.load('assets/player.png'))
        self.bullet = Bullet(pygame.image.load('assets/bullet.png'))

        self.enemies = [
            Enemy(pygame.image.load('assets/alien.png'))
            for _ in range(NUMBER_OF_ENEMIES)
        ]

        self.score = 0
        self.running = True
        self.game_over = False
        self.font = pygame.font.Font(None, 36)
        self.game_over_font = pygame.font.Font(None, 72)

    def is_collision(self, enemy, bullet):
        distance = math.sqrt((enemy.x - bullet.x)**2 + (enemy.y - bullet.y)**2)
        return distance < 27

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.velocity = -PLAYER_SPEED
                if event.key == pygame.K_RIGHT:
                    self.player.velocity = PLAYER_SPEED
                if event.key == pygame.K_SPACE:
                    self.bullet.fire(self.player.x)

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    self.player.velocity = 0

    def update(self):
        if self.game_over:
            return
            
        self.player.move()
        self.bullet.move()

        for enemy in self.enemies:
            enemy.move()

            if enemy.y > 480:
                self.game_over = True

            if self.is_collision(enemy, self.bullet):
                self.bullet.reset()
                self.score += 1
                enemy.x, enemy.y = random.randint(0, 736), random.randint(50, 150)

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

        self.player.draw(self.screen)
        self.bullet.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            self.show_game_over()
        else:
            pygame.display.update()
    
    def show_game_over(self):
        game_over_text = self.game_over_font.render("GAME OVER", True, (255, 0, 0))
        final_score_text = self.font.render("Final Score: " + str(self.score), True, (255, 255, 255))
        restart_text = self.font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        
        self.screen.blit(game_over_text, (200, 200))
        self.screen.blit(final_score_text, (250, 300))
        self.screen.blit(restart_text, (150, 400))
        
        pygame.display.update()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart_game()
                        waiting = False
                    if event.key == pygame.K_q:
                        self.running = False
                        waiting = False
    
    def restart_game(self):
        self.game_over = False
        self.score = 0
        self.player.x = 368
        self.bullet.y = 480
        self.bullet.state = "ready"
        for enemy in self.enemies:
            enemy.x = random.randint(0, 736)
            enemy.y = random.randint(50, 150)