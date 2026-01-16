from engine.entity.Component import Component


class MouvementComponent(Component):
    def move(self, dx, dy):
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
