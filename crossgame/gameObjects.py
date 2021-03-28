import pygame

class GameObjects:

    def __init__(self, x, y, width, height, image_path, collision):
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (width, height))

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collison = collision
