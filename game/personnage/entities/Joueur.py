import random

import pyxel

from game.gabrimon.Combat import Combat
from game.personnage.composants.GestionGabrimonComponent import GestionGabrimonComponent
from game.personnage.composants.MouvementComponent import MouvementComponent
from game.personnage.composants.TeleportationComponent import TeleportationComponent
from game.personnage.composants.GabridexComponent import GabridexComponent
from game.personnage.entities.Personnage import Personnage
from game.personnage.composants.TransitionAnimationComponent import TransitionAnimationComponent
#from game.Inventory.SacADos import SacADos
CLICK_DEBUG = True

class Joueur(Personnage):
    def __init__(self, service):
        super().__init__(service)
        self.speed = 2
        self.register_component("mouvement", MouvementComponent)
        self.register_component("transition", TransitionAnimationComponent)
        self.register_component("teleportation", TeleportationComponent)
        self.register_component("gabrimon", GestionGabrimonComponent)
        self.register_component("gabridex", GabridexComponent)
        self.get_component("gabrimon").gabrimon_actuel = self.get_component("gabrimon").equipe[0]

        self.nom = "Raphanathanael"

        self.x = 1016
        self.y = 396
        self.doorstep = 0
        self.entering = False

        self.freeze_movement = False
        self.freeze_interact = False

        if CLICK_DEBUG:
            pyxel.mouse(True)

        self.combat_cooldown = 0


    def update(self):
        super().update()

        if self.service.engine.get_service("combat").is_combat(): return

        if self.combat_cooldown > 0:
            self.combat_cooldown -= 1
            print(f"COOLDOWN : {self.combat_cooldown}")
        dx, dy = 0, 0
        if not self.freeze_movement:
            if pyxel.btn(pyxel.KEY_LEFT):
                dx = -self.speed
            elif pyxel.btn(pyxel.KEY_RIGHT):
                dx = self.speed
            elif pyxel.btn(pyxel.KEY_UP):
                dy = -self.speed
            elif pyxel.btn(pyxel.KEY_DOWN):
                dy = self.speed

        if pyxel.btnp(pyxel.KEY_P):
            self.get_component("gabridex").switch()


        if CLICK_DEBUG and pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
            x = pyxel.mouse_x
            y = pyxel.mouse_y
            print(f"Location (UI Space) : x={x}, y={y}")
        if CLICK_DEBUG and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            x = pyxel.mouse_x + (self.x - pyxel.width // 2)
            y = pyxel.mouse_y + (self.y - pyxel.height // 2)
            print(f"Location (World Space) : x={x}, y={y}")

        self.get_component("mouvement").move(dx, dy)
        self.set_state("player_x", self.x)
        self.set_state("player_y", self.y)

        if self.service.engine.get_service("terrain").is_in_gabrimon_zone(self.x, self.y) and not self.freeze_interact and dx+dy != 0 and self.combat_cooldown == 0:
            if random.randint(0,100) == 55:
                self.service.engine.get_service("combat").start_combat(self, self.service.engine.get_service("gabrimon").get_random_gabrimon())
                self.combat_cooldown = 1000

        if pyxel.btn(pyxel.KEY_E) and not self.freeze_interact and self.doorstep != 0:
            indoor = self.service.engine.get_service("indoor").get_indoor(self.doorstep)
            if self.service.engine.get_service("map").current_world == 0:
                self.get_component("teleportation").teleport(indoor.indoor_pos)
            else:
                self.get_component("teleportation").teleport(indoor.outside_pos)
            self.doorstep=0


    def set_doorstep(self, id):
        self.doorstep = id

    def teleport(self, world, x, y):
        self.x = x
        self.y = y
        self.service.engine.get_service("map").set_world(world)

    def draw(self):
        if self.service.engine.get_service("combat").is_combat(): return
        pyxel.camera(self.x - pyxel.width // 2, self.y - pyxel.height // 2)
        if self.doorstep != 0 and self.service.engine.get_service("map").current_world == 0:
            indoorname=self.service.engine.get_service("indoor").get_indoor(self.doorstep).name
            self.service.engine.get_service("ui").draw_container(img=2, sx=232, sy=232, x=10, y=100, w=4*len(indoorname)+10, h=16)
            self.service.engine.get_service("ui").draw_text(indoorname, 15, 105, 0)
        super().draw()