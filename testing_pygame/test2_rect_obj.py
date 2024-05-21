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
    
    print(f"line start: ({rect.left},{rect.top}) line End: ({rect.right},{rect.top})")

    # Draw lines representing different attributes
    pygame.draw.line(screen, GREEN, (rect.left, rect.top), (rect.right, rect.top), 2)
    pygame.draw.line(screen, GREEN, (rect.left, rect.top), (rect.left, rect.bottom), 2)
    pygame.draw.line(screen, GREEN, (rect.right, rect.top), (rect.right, rect.bottom), 2)
    pygame.draw.line(screen, GREEN, (rect.left, rect.bottom), (rect.right, rect.bottom), 2)

    # Draw a circle at the center of the rectangle
    pygame.draw.circle(screen, BLUE, rect.center, 5)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
