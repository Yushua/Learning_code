from gameObjects import GameObjects
 
class Player(GameObjects):

    def __init__(self, x, y, width, height, image_path, collision, speed):
        super().__init__(x, y, width, height, image_path, collision)
        
        self.speed = speed

    def move(self, directiony, directionx):
        self.y += (directiony * self.speed)
        self.x += (directionx * self.speed)