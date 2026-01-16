from engine.entity.Entity import Entity
import pyxel

from game.Map.Zone.ZoneEvent import ZoneEvent


class Zone(Entity):
    def __init__(self, service,x,y,w,h,events=ZoneEvent()):
        super().__init__(service)
        self.set_size(x,y,w,h)
        self.events = events
        self.container = []

    def set_size(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def update(self):
        for i in self.service.engine.get_service("personnages").entities:
            if self.is_in_zone(i.x+i.taille_x/2,i.y+i.taille_y/2):
                if not i in self.container:
                    self.events.on_enter(i)
                    self.container.append(i)
                self.events.on_update(i)
            else:
                if i in self.container:
                    self.events.on_exit(i)
                    self.container.remove(i)

    def is_in_zone(self, x, y):
        return ((self.x <= x <= (self.x+self.w))
                and self.y <= y <= (self.y + self.h))

    def draw(self):
        pyxel.rect(self.x,self.y,self.w,self.h, 9)