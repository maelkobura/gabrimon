from engine.entity.Entity import Entity
import pyxel

class Zone(Entity):
    def __init__(self, service,x,y,w,h):
        super().__init__(service)
        self.set_size(x,y,w,h)

    def set_size(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def update(self):
        for i in self.service.engine.get_service("personnages").entities:
            if self.is_in_zone(i.x,i.y):
                print("SBOULA")

    def is_in_zone(self, x, y):
        return ((self.x < x < (self.x+self.w))
                and self.y < y < (self.y + self.h))

    def draw(self):
        pyxel.rect(self.x,self.y,self.w,self.y, 9)