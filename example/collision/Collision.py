class Collision:
    def __init__(self, x, y, w, h, flag):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.flag = flag

    def collide(self, collision):
        return (self.x < collision.x + collision.w and
                self.x + self.w > collision.x and
                self.y < collision.y + collision.h and
                self.y + self.h > collision.y)
