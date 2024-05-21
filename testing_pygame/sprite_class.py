import pygame
from pygame.sprite import Sprite, Group

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create a display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pixel-Perfect Collision Example')

# Define a sprite class with a mask
class Player(Sprite):
    def __init__(self, image_file, position):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # Example movement logic for demonstration
        self.rect.x += 1
        self.rect.y += 1

class Enemy(Sprite):
    def __init__(self, image_file, position):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # Example movement logic for demonstration
        self.rect.x -= 1
        self.rect.y -= 1

# Create sprite groups
all_sprites = Group()
enemies = Group()

# Create player and enemy sprites
player = Player('UltimatePygame\graphics\Player\player_walk_1.png', (100, 100))
enemy1 = Enemy('UltimatePygame\graphics\snail\snail1.png', (200, 150))

# Add sprites to the groups
all_sprites.add(player, enemy1)
enemies.add(enemy1)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Check for pixel-perfect collisions
    if pygame.sprite.collide_mask(player, enemy1):
        print("Pixel-perfect collision detected!")

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw all sprites
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

pygame.quit()
