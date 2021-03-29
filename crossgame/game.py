import pygame
from gameObjects import GameObjects
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        self.block = 48
        self.width = 768
        self.height = 768
        self.colour = (100, 255, 255)
        self.game_quit = 0
        self.game_window = pygame.display.set_mode((self.width, self.height))

        #image objects paths
        self.backgroundpng = 'crossgame/assets/background.png'
        self.character_frontpng = 'crossgame/assets/character_front1.png'
        self.chestpng = 'crossgame/assets/chest.png'
        self.keypng = 'crossgame/assets/key.png'
        #endif

        self.clock = pygame.time.Clock()

        #set objects
        self.background = GameObjects(0, 0, self.width, self.height, self.backgroundpng, 0)
        self.chest = GameObjects(360, 48, self.block, self.block, self.chestpng, 0)
        self.level = 1.0
        self.set_map()
        #endif

    def set_map(self):
        self.player = Player(336, 672, self.block, self.block, self.character_frontpng, 0, 4)
        self.chestpng = 'crossgame/assets/chest.png'
        self.chest = GameObjects(360, 48, self.block, self.block, self.chestpng, 0)
        self.enemies = [
            Enemy(0, 144, self.block, self.block, self.keypng, 1, 2),
            Enemy(0, 144 + self.block, self.block, self.block, self.keypng, 1, 2),
            Enemy(0, 144 - self.block, self.block, self.block, self.keypng, 1, 2),
        ]

    def move_objects(self, player_direction_y, player_direction_x):
        self.player.move(player_direction_y, player_direction_x, self.height, self.width)
        for enemy in self.enemies:
            enemy.move(self.width)

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.set_map()
                return True
        if self.detect_collision(self.player, self.chest):
            self.chestpng = 'crossgame/assets/chest_open.png'
            self.chest = GameObjects(self.chest.x, self.chest.y, self.chest.width, self.chest.height, self.chestpng, 0)
            self.game_window.blit(self.chest.image, (self.chest.x, self.chest.y))
        return False

    def detect_collision(self, object_1, object_2):
        if  object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False
        if  object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False
        return True

    def draw_objects(self):
        self.game_window.fill(self.colour)
        self.game_window.blit(self.background.image, (0, 0))
        self.game_window.blit(self.chest.image, (self.chest.x, self.chest.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        pygame.display.update()

    def game_loop(self):
        player_direction_y = 0
        player_direction_x = 0
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    print("---quit game---")
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction_y = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction_y = 1
                    elif event.key == pygame.K_LEFT:
                        player_direction_x = -1
                    elif event.key == pygame.K_RIGHT:
                        player_direction_x = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction_y = 0
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player_direction_x = 0
            self.move_objects(player_direction_y, player_direction_x)
            self.draw_objects()

            if self.check_if_collided():
                self.set_map()
            self.clock.tick(60)
