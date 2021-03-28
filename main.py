class gameobject:

    def __init__(self, name, xpos, ypos, health):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.health = health
    def move_x(self, xmov):
        self.xpos += xmov
    def move_y(self, ymov):
        self.ypos += ymov
c_yusha = gameobject("yusha", 0, 0, 200)

print(c_yusha.xpos)