import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rect Attributes Example")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create a rectangle for demonstration
rect_width = 100
rect_height = 80
rect = pygame.Rect(0, 0, rect_width, rect_height)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, RED, rect)

    # Draw lines representing different attributes
    pygame.draw.line(screen, GREEN, rect.topleft, rect.topright, 2)
    pygame.draw.line(screen, BLUE, rect.topleft, rect.bottomleft, 2)
    pygame.draw.line(screen, (0,0,0), rect.topright, rect.bottomright, 2)
    pygame.draw.line(screen, (0,255,255), rect.bottomleft, rect.bottomright, 2)

    # Draw a circle at the center of the rectangle
    pygame.draw.circle(screen, BLUE, rect.center, 5)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
