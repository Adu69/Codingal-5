import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player vs Enemies")
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))

# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create player
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
all_sprites.add(player)

# Create 7 enemies
for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Game loop
score = 0
running = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()
    
    # Check collisions
    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        score += 1
        # Spawn new enemy
        new_enemy = Enemy()
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)
    
    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

pygame.quit()