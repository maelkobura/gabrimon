import pyxel

from game.personnage.composants.MouvementComponent import MouvementComponent
from game.personnage.entities.Personnage import Personnage
from game.personnage.composants.TransitionAnimationComponent import TransitionAnimationComponent


class Joueur(Personnage):
    def __init__(self, service):
        super().__init__(service)
        self.speed = 2
        self.register_component("mouvement", MouvementComponent)
        self.register_component("transition", TransitionAnimationComponent)

        self.x = 1016
        self.y = 396
        self.doorstep = 0

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
        self.set_state("player_x", self.x)
        self.set_state("player_y", self.y)

        # TODO Faire mieux

        if pyxel.btn(pyxel.KEY_E):
            if self.doorstep != 0:
                print("Entering to door", self.doorstep)
                self.doorstep = 0
                self.get_component("transition").transition = 1

        if self.get_component("transition").transition == 0:
            self.teleport(1, 56, 134)
            self.get_component("transition").transition = 2

        super().update()

    def set_doorstep(self, id):
        self.doorstep = id

    def teleport(self, world, x, y):
        self.x = x
        self.y = y
        self.service.engine.get_service("map").set_world(world)

    def draw(self):
        pyxel.camera(self.x - pyxel.width // 2, self.y - pyxel.height // 2)
        super().draw()