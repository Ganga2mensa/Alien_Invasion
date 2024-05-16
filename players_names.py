import pygame
import sys

def get_player_name(screen, clock, base_font):
    # Initialize variables for player name input
    user_text = ''
    input_rect = pygame.Rect(200, 200, 200, 32)  # Initial size of the input box
   # color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    active = False
    
    # Cursor variables
    cursor_visible = True
    cursor_timer = 0
    BLINK_RATE = 500  # Blink rate in milliseconds

    placeholder_text = "Enter your name here"
    placeholder_font = pygame.font.Font(None, 24)
    placeholder_surface = placeholder_font.render(placeholder_text, True, (150, 150, 150))
    placeholder_rect = placeholder_surface.get_rect(x=input_rect.x + 5, centery=input_rect.centery)
    

    # Loop for to until the player enter his/her name
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        # Save user name to a text file
                        with open('players_names.txt', 'a') as file:
                            file.write(user_text + '\n')
                        return user_text
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                    # Reset cursor visibility when typing
                    cursor_visible = True
                    cursor_timer = pygame.time.get_ticks()
                    
                    # Dynamically adjust the width of the input box
                    text_surface = base_font.render(user_text, True, (255, 255, 255))
                    input_rect.w = max(140, text_surface.get_width() + 10)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

        # Clear the screen
        screen.fill((255, 255, 255))
        
        # Draw input box
        pygame.draw.rect(screen, color, input_rect)
        
        # Render placeholder text
        if not user_text and not active:
            screen.blit(placeholder_surface, placeholder_rect)
        
        # Render user text
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        
        # Update cursor visibility
        current_time = pygame.time.get_ticks()
        if current_time - cursor_timer > BLINK_RATE:
            cursor_visible = not cursor_visible
            cursor_timer = current_time
        
        # Render cursor
        if active and cursor_visible:
            cursor_pos = input_rect.x + 5 + text_surface.get_width()
            pygame.draw.line(screen, (0, 0, 0), (cursor_pos, input_rect.y + 5),
                             (cursor_pos, input_rect.y + input_rect.height - 5), 2)
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)

