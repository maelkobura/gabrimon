from engine.entity.Component import Component
from example.collision.Collision import Collision


class MouvementComponent(Component):
    def move(self, dx, dy):
        self.entity.x += dx
        self.entity.y += dy
