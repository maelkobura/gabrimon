import random
from random import Random

import pyxel

from example.collision.Collision import Collision
from example.player.MovingEntity import MovingEntity


class Bot(MovingEntity):
    def __init__(self, service):
        super().__init__(service,0,0)
        self.speed = 0.5
        self.random = Random()

        collision_service = self.service.engine.get_service("collision")

        for _ in range(100):
            x = random.randint(-2500, 2500)
            y = random.randint(-2500, 2500)
            new_rect = Collision(x, y, 8, 8, None)
            if not collision_service.i_am_colliding(new_rect):
                self.x = x
                self.y = y
                break
        else:
            self.x = 0
            self.y = 0

        # mouvements continus
        self.vx = random.uniform(-1, 1) * self.speed
        self.vy = random.uniform(-1, 1) * self.speed
        self.change_dir_timer = random.randint(60, 180)

    def update(self):
        self.change_dir_timer -= 1
        if self.change_dir_timer <= 0:
            self.vx = random.uniform(-1, 1) * self.speed
            self.vy = random.uniform(-1, 1) * self.speed
            self.change_dir_timer = random.randint(60, 180)

        self.move(self.vx, self.vy)

    def draw(self):
        pyxel.rect(self.x, self.y, 8, 8, 11)
