import pygame

class Game:
    def __init__(self):
        self.block = 48
        self.width = 768
        self.height = 768
        self.colour = (100, 255, 255)
        self.game_quit = 0
        self.game_window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        background_image = pygame.image.load('crossgame/assets/background.png')
        self.background_image = pygame.transform.scale(background_image, (self.width, self.height))
        character_front = pygame.image.load('crossgame/assets/character_front1.png')
        self.character_front = pygame.transform.scale(character_front, (self.block, self.block))
        chest = pygame.image.load('crossgame/assets/chest.png')
        self.chest = pygame.transform.scale(chest, (self.block, self.block))

    def draw_objects(self):
        self.game_window.fill(self.colour)
        self.game_window.blit(self.background_image, (0, 0))
        self.game_window.blit(self.character_front, (0, 0))
        self.game_window.blit(self.chest, (360, 48))
        pygame.display.update()

    def game_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    print("---quit game---")
                    return
            self.draw_objects()
            self.clock.tick(60)
