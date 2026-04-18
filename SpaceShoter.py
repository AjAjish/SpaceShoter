import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Set the title and icon
pygame.display.set_caption('Space Shooter.')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Background image 
backgroundImg = pygame.image.load('background.png')

# For player
playerImg = pygame.image.load('player.png')
playerX = 368
playerY = 480
player_change = 0

# For enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet image
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

# Score variable
score = 0
font = pygame.font.Font(None, 36)

# Game over flag
game_over = False
game_over_font = pygame.font.Font(None, 72)

# Create functions
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    return distance < 27

# Game running loop
running = True
while running:
    # Fill screen color and draw background
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Create player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -5
            if event.key == pygame.K_RIGHT:
                player_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":  # Use == for comparison
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0

    # Update player position
    playerX += player_change
    # Add boundaries for the player
    playerX = max(0, min(playerX, 736))

    for i in range(num_of_enemies):
        # Update enemy position
        enemyX[i] += enemyX_change[i]

        # Check boundaries for enemies
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Check if enemy reached bottom - Game Over condition
        if enemyY[i] > 480:
            game_over = True

        # Collision detection
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print("Score:", score)
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)  # Call the fire_bullet function
        bulletY -= bulletY_change
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

    # Call player function
    player(playerX, playerY)

    # Draw the score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Game Over screen
    if game_over:
        game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        final_score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))
        restart_text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        
        # Display centered text
        screen.blit(game_over_text, (200, 200))
        screen.blit(final_score_text, (250, 300))
        screen.blit(restart_text, (150, 400))
        
        pygame.display.update()
        
        # Wait for player input to restart or quit
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Restart the game
                        game_over = False
                        score = 0
                        playerX = 368
                        bulletY = 480
                        bullet_state = "ready"
                        for i in range(num_of_enemies):
                            enemyX[i] = random.randint(0, 736)
                            enemyY[i] = random.randint(50, 150)
                        waiting = False
                    if event.key == pygame.K_q:
                        running = False
                        waiting = False
        continue

    # Update the display
    pygame.display.update()
