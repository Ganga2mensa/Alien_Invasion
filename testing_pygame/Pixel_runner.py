import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f"Score: {current_time}", 'UltimatePygame\font\Pixeltype.ttf', (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rec in obstacle_list:
            obstacle_rec.x -= 5
            if obstacle_rec.bottom == 300: screen.blit(snail_surf, obstacle_rec)
            else: screen.blit(fly_surf, obstacle_rec)

        filitered_obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        # print(obstacle_list)

        return filitered_obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]

pygame.init()

screen = pygame.display.set_mode((800,400)) # This is a display surface
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0
#test_font = pygame.font.Font('UltimatePygame\font\Pixeltype.ttf', 50)
test_font = pygame.font.Font(None, 50)
sky_surf = pygame.image.load("UltimatePygame\graphics\Sky.png").convert()
ground_surf = pygame.image.load('UltimatePygame\graphics\ground.png').convert() 

# Score point
# score_surf = test_font.render('My game', False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

# Objstacle 
snail_frame_1 = pygame.image.load('UltimatePygame\graphics\snail\snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('UltimatePygame\graphics\snail\snail2.png').convert_alpha()
snail_frame_list = [snail_frame_1, snail_frame_2]
snail_index = 0
snail_surf = snail_frame_list[snail_index]

fly_frame1 = pygame.image.load('UltimatePygame\graphics\Fly\Fly1.png')
fly_frame2 = pygame.image.load('UltimatePygame\graphics\Fly\Fly2.png')
fly_frame_list = [fly_frame1, fly_frame2]
fly_index = 0
fly_surf = fly_frame_list[fly_index]



obstacle_rec_list = []

# player
player_walk_1 = pygame.image.load('UltimatePygame\graphics\Player\player_walk_1.png').convert_alpha()
player_walk_2  = pygame.image.load('UltimatePygame\graphics\Player\player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('UltimatePygame\graphics\Player\jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

player_stand = pygame.image.load('UltimatePygame\graphics\Player\player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center=(400,200))

# Intro screen
game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))
game_message = test_font.render('Press space to run',False,(111, 196, 169))
game_message_rect = game_message.get_rect(center = (400,340))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snial_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snial_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

player_gravity = -20
# Set the size for the image
DEFAULT_IMAGE_SIZE = (100, 75)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN :
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: player_gravity = -20
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                #snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)
        if game_active:
            if event.type == obstacle_timer and game_active:
                if randint(0,2):
                    obstacle_rec_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
                else:
                    obstacle_rec_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),210)))
            if event.type == snial_animation_timer:
                if snail_index == 0: snail_index = 1
                else: snail_index = 0
                snail_surf = snail_frame_list[snail_index]
            if event.type == fly_animation_timer:
                if fly_index == 0: fly_index = 1
                else: fly_index = 0
                fly_surf = fly_frame_list[fly_index]

    
    if game_active:
        screen.blit(sky_surf, (0,0)) # dispaly the (regular) surface on a display surface
        screen.blit(ground_surf, (0,300)) # dispaly the (regular) surface on a display surface
        # pygame.draw.rect(screen,'#c0e8ec', score_rect)
        # pygame.draw.rect(screen,'#c0e8ec', score_rect,10)
        # screen.blit(score_surf,score_rect)
        score = display_score()

        # Snail movement
        # snail_rect.x -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surf,snail_rect)

        # Displaying player in the screen
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom=300
        player_animation()
        screen.blit(player_surf, player_rect)

        # Obstacle Movement
        obstacle_rec_list = obstacle_movement(obstacle_rec_list)

        # Collision
        game_active = collisions(player_rect, obstacle_rec_list)

    else:
        screen.fill((94,129,162))
        obstacle_rec_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0 
        screen.blit(player_stand,player_stand_rect)
        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 340))
        screen.blit(game_name,game_name_rect)
        if score  == 0: screen.blit(game_message, game_message_rect)
        else: screen.blit(score_message,score_message_rect)
       
    pygame.display.update()
    clock.tick(60)