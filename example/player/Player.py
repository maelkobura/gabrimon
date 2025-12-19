import pyxel

from engine.entity.Entity import Entity
from example.player.MovingEntity import MovingEntity


class Player(MovingEntity):
    def __init__(self, service):
        super().__init__(service, 80, 60)
        self.speed = 2

    def update(self):
        dx, dy = 0, 0
        if pyxel.btn(pyxel.KEY_LEFT):
            dx = -self.speed
        if pyxel.btn(pyxel.KEY_RIGHT):
            dx = self.speed
        if pyxel.btn(pyxel.KEY_UP):
            dy = -self.speed
        if pyxel.btn(pyxel.KEY_DOWN):
            dy = self.speed

        self.move(dx, dy)


    def draw(self):
        camera_x = self.set_state("camera_x",self.x - pyxel.width // 2)
        camera_y = self.set_state("camera_y",self.y - pyxel.width // 2)
        pyxel.camera(camera_x, camera_y)
        self.service.engine.load("assets/res (5).pyxres")
        pyxel.rect(self.x, self.y, 8, 8, 9)