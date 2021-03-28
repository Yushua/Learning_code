def     handle_events():
    global game_quit
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            print("---quit game---")
            game_quit = 1
# def     handle_logic():
#     i = 0
#     i += 1

import pygame

pygame.init()

width = 1500
height = 800
colour = (100, 255, 255)
game_quit = 0
game_window = pygame.display.set_mode((width, height))
game_window.fill(colour)
clock = pygame.time.Clock()
background_image = pygame.image.load('python course\cross game\assets\background.png')

def game_loop():
    while game_quit == 0:
        pygame.display.update()
        clock.tick(60)
        game_window.fill(colour)
        game_window.blit(background_image, (0, 0))
        handle_events()
        # handle_logic()
game_loop()
pygame.quit
quit()