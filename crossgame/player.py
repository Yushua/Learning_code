from gameObjects import GameObjects
 
class Player(GameObjects):

    def __init__(self, x, y, width, height, image_path, collision, speed, coins, keys):
        super().__init__(x, y, width, height, image_path, collision)
        
        self.speed = speed
        self.coins = coins
        self.keys = keys

    def move(self, directiony, directionx, max_height, max_width):
        if (self.y >= max_height - self.height and directiony > 0) or (self.y == 0 and directiony < 0):
            return
        self.y += (directiony * self.speed)
        if (self.x >= max_width - self.width and directionx > 0) or (self.x == 0 and directionx < 0):
            return
        self.x += (directionx * self.speed)