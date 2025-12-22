import pyxel

from game.personnage.composants.MouvementComponent import MouvementComponent
from game.personnage.entities.Personnage import Personnage


class Joueur(Personnage):
    def __init__(self, service):
        super().__init__(service)
        self.speed = 2
        self.register_component("mouvement", MouvementComponent)
        self.x = 120
        self.y = 110

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
        pyxel.camera(self.x - pyxel.width // 2, self.y - pyxel.height // 2)
        super().draw()