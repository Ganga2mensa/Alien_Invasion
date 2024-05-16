import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,400)) # This is a display surface
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('sky.jpg').convert()
#print("Height of image= " + str(sky_surface.get_height())) 
#print("Width of image= " + str(sky_surface.get_width())) 
#print("size of image is (width,height):", sky_surface.get_size()) 
sky_surface = pygame.transform.scale(sky_surface,(800,300))
#print("Height of image= " + str(sky_surface.get_height())) 
#print("Width of image= " + str(sky_surface.get_width())) 
#print("size of image is (width,height):", sky_surface.get_size()) 
ground_surface = pygame.image.load('ground.jpg').convert() 
ground_surface = pygame.transform.scale(ground_surface,(800,100))
text_surf = test_font.render('My game', False, 'Black')
score_surf = text_surf.get_rect(center=(400,50))
snail_surface = pygame.image.load('snail2.png').convert_alpha()
#print("Height of image= " + str(snail_surface.get_height())) 
#print("Width of image= " + str(snail_surface.get_width())) 
#print("size of image is (width,height):", snail_surface.get_size()) 
# Set the size for the image
DEFAULT_IMAGE_SIZE = (100, 75)
# Scale the image to your needed size
snail_surface = pygame.transform.scale(snail_surface, DEFAULT_IMAGE_SIZE)
#print("Height of image= " + str(snail_surface.get_height())) 
#print("Width of image= " + str(snail_surface.get_width())) 
#print("size of image is (width,height):", snail_surface.get_size()) 
snail_rect = snail_surface.get_rect(midtop = (500,300) )
#test_surface = pygame.Surface((200,100)) # This is one is (regular) surface
#test_surface.fill('Red')
snail_x_pos = 400
snail_y_pos = 250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEMOTION:
            if snail_rect.collidepoint(event.pos): print("Collision")
    screen.blit(sky_surface, (0,0)) # dispaly the (regular) surface on a display surface
    screen.blit(ground_surface, (0,300)) # dispaly the (regular) surface on a display surface
    pygame.draw.rect(screen,'Pink', score_surf,4,20)
    #pygame.draw.line(screen,'Gold', (0,0),pygame.mouse.get_pos(),10)
    #pygame.draw.ellipse(screen,'Brown', pygame.Rect(50, 200, 100, 100))


    screen.blit(text_surf,score_surf)
    snail_rect.x -= 1
    screen.blit(snail_surface,snail_rect)


    pygame.display.update()
    clock.tick(60)