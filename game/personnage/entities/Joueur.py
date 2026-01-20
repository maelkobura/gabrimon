import pyxel

from game.personnage.composants.MouvementComponent import MouvementComponent
from game.personnage.entities.Personnage import Personnage
from game.personnage.composants.TransitionAnimationComponent import TransitionAnimationComponent

CLICK_DEBUG = True

class Joueur(Personnage):
    def __init__(self, service):
        super().__init__(service)
        self.speed = 2
        self.register_component("mouvement", MouvementComponent)
        self.register_component("transition", TransitionAnimationComponent)

        self.x = 1016
        self.y = 396
        self.doorstep = 0
        self.entering = False

        self.freeze_movement = False
        self.freeze_interact = False

        if CLICK_DEBUG:
            pyxel.mouse(True)


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

        if CLICK_DEBUG and pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
            x = pyxel.mouse_x
            y = pyxel.mouse_y
            print(f"Location : x={x}, y={y}")

        self.get_component("mouvement").move(dx, dy)
        self.set_state("player_x", self.x)
        self.set_state("player_y", self.y)

        # TODO Faire mieux

        if pyxel.btn(pyxel.KEY_E) and not self.freeze_interact:
            self.entering = True
            self.freeze_movement = True
            self.freeze_interact = True

        if self.entering:
            self.enter()

        if self.get_component("transition").transition == 0:
            self.teleport(1, 56, 134)
            self.direction = 1
            self.get_component("transition").transition = 2

        super().update()

    def enter(self):
        if self.doorstep == 0:
            return
        if self.get_component("transition").transition == 0:
            indoor = self.service.engine.get_service("indoor").get_indoor(self.doorstep)
            if indoor:
                self.teleport(indoor.world, indoor.x, indoor.y)
                self.get_component("transition").transition = 2
                self.freeze_movement=False
                self.freeze_interact=False
                self.entering = False

    def set_doorstep(self, id):
        self.doorstep = id

    def teleport(self, world, x, y):
        self.x = x
        self.y = y
        self.service.engine.get_service("map").set_world(world)

    def draw(self):
        pyxel.camera(self.x - pyxel.width // 2, self.y - pyxel.height // 2)
        super().draw()