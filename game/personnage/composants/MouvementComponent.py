from engine.entity.Component import Component


class MouvementComponent(Component):
    def move(self, dx, dy):

        speed = self.entity.service.engine.get_service("terrain").get_speed(self.entity.x + self.entity.taille_x/2, self.entity.y + self.entity.taille_y/2)
        # X
        if self.entity.service.engine.get_service("terrain").can_i(self.entity.x + dx, self.entity.y, self.entity.taille_x, self.entity.taille_y):
            self.entity.x += dx*speed

        # Y
        if self.entity.service.engine.get_service("terrain").can_i(self.entity.x, self.entity.y+dy, self.entity.taille_x, self.entity.taille_y):
            self.entity.y += dy*speed

        if dx+dy==0:
            self.entity.is_moving = False
        else:
            self.entity.is_moving = True

        if dx < 0:
            self.entity.direction = 4
        elif dx > 0:
            self.entity.direction = 2

        if dy < 0:
            self.entity.direction = 1
        elif dy > 0:
            self.entity.direction = 3
