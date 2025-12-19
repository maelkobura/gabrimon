import pyxel

from engine.entity.Entity import Entity
from example.collision.Collision import Collision


class HouseEntity(Entity):

    def __init__(self, service):
        super().__init__(service)
        self.x = 125
        self.y = 55
        self.size_x = 50
        self.size_y = 40

        self.service.engine.get_service("collision").register_collision(Collision(self.x, self.y, self.size_x, self.size_y, "build"))

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.size_x, self.size_y)