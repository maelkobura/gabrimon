from engine.entity.Entity import Entity
from example.collision.Collision import Collision


class MovingEntity(Entity):
    def __init__(self, service, x, y):
        super().__init__(service)
        self.x = x
        self.y = y

    def move(self, dx, dy):
        new_rect = Collision(self.x + dx, self.y + dy, 8, 8, None)

        if not self.service.engine.get_service("collision").i_am_colliding(new_rect):
            self.x += dx
            self.y += dy
