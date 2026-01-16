from engine.entity.Component import Component


class MouvementComponent(Component):
    def move(self, dx, dy):
        speed = self.entity.speed * self.entity.service.engine.get_service("terrain").can_i(self.entity.x, self.entity.y, dx,dy)
        self.entity.x += dx
        self.entity.y += dy


        if dx < 0:
            self.entity.direction = 4
        elif dx > 0:
            self.entity.direction = 2

        if dy < 0:
            self.entity.direction = 1
        elif dy > 0:
            self.entity.direction = 3
