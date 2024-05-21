import pygame
import cv2
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Camera Feed')

# Initialize camera
camera = cv2.VideoCapture(0)
print(camera)
def get_camera_frame(camera):
    ret, frame = camera.read()
    if not ret:
        return None
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)  # Rotate frame if necessary
    frame = pygame.surfarray.make_surface(frame)
    return frame

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame = get_camera_frame(camera)
    if frame:
        screen.blit(frame, (0, 0))
        pygame.display.flip()

# Release resources
camera.release()
pygame.quit()