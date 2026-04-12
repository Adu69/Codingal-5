import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Color Change Event")
clock = pygame.time.Clock()

# Custom event for color change
COLOR_CHANGE_EVENT = pygame.USEREVENT + 1

# Sprite class
class Sprite:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
    
    def change_color(self, new_color):
        self.color = new_color

# Create sprites
sprite1 = Sprite(100, 150, 100, 100, (255, 0, 0))
sprite2 = Sprite(600, 150, 100, 100, (0, 0, 255))

# Set timer for color change event
pygame.time.set_timer(COLOR_CHANGE_EVENT, 200)

# Main loop
running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == COLOR_CHANGE_EVENT:
            sprite1.change_color((0, 255, 0))
            sprite2.change_color((255, 255, 0))
    
    screen.fill((255, 255, 255))
    sprite1.draw(screen)
    sprite2.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()