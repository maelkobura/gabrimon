import pyxel

from game.personnage.composants.MouvementComponent import MouvementComponent
from game.personnage.entities.Personnage import Personnage


class Joueur(Personnage):
    def __init__(self, service):
        super().__init__(service)
        self.speed = 5
        self.register_component("mouvement", MouvementComponent)

    def update(self):
        dx, dy = 0, 0
        if pyxel.btn(pyxel.KEY_LEFT):
            dx = -self.speed
        elif pyxel.btn(pyxel.KEY_RIGHT):
            dx = self.speed
        elif pyxel.btn(pyxel.KEY_UP):
            dy = -self.speed
        elif pyxel.btn(pyxel.KEY_DOWN):
            dy = self.speed

        self.get_component("mouvement").move(dx, dy)
        super().update()

    def draw(self):
        camera_x = self.set_state("camera_x", self.x - pyxel.width // 2)
        camera_y = self.set_state("camera_y", self.y - pyxel.height // 2)
        #pyxel.camera(camera_x, camera_y)

        super().draw()