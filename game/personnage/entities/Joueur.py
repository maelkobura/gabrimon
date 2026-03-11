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
        self.starter_required = True
        self.register_component("gabrimon", GestionGabrimonComponent)
        self.register_component("gabridex", GabridexComponent)

        self.nom = "Raphanathanael"

        self.x = 1016
        self.y = 396
        #self.x = 1599
        #self.y = 971
        self.doorstep = 0
        self.entering = False

        self.freeze_movement = False
        self.freeze_interact = False

        if CLICK_DEBUG:
            pyxel.mouse(True)

        self.combat_cooldown = 0
        self._starter_choisi = False
        self._starter_index = 0
        self.freeze_movement = True
        self.freeze_interact = True
        self._toast_text = None
        self._toast_timer = 0
        # Etats UI par defaut (evite KeyError avant le 1er update complet)
        self.set_state("player_x", self.x)
        self.set_state("player_y", self.y)
        self.set_state("heal_prompt", False)
        self._heal_points = [
            # Centres Gabrimon (world=1) - positions donnees
            (1, 443.0, 297.0),
            (1, 442.0, 41.0),
        ]


    def update(self):
        super().update()

        if self._toast_timer > 0:
            self._toast_timer -= 1
            if self._toast_timer == 0:
                self._toast_text = None

        if not self._starter_choisi:
            self.set_state("player_x", self.x)
            self.set_state("player_y", self.y)
            self._update_choix_starter()
            return

        if self.service.engine.get_service("combat").is_combat(): return

        self._update_heal_interaction()

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
            pos = self.service.engine.get_service("indoor").get_pos(self.doorstep)
            self.get_component("teleportation").teleport(pos)
            self.doorstep=0

    def _update_heal_interaction(self):
        if self.freeze_interact:
            return
        if self.service.engine.get_service("combat").is_combat():
            return

        current_world = self.service.engine.get_service("map").current_world
        near = False
        for w, hx, hy in self._heal_points:
            if w != current_world:
                continue
            if self._is_near_point(hx, hy, radius=14):
                near = True
                break

        if not near:
            self.set_state("heal_prompt", False)
            return

        self.set_state("heal_prompt", True)
        if pyxel.btnp(pyxel.KEY_E):
            comp = self.get_component("gabrimon")
            if not getattr(comp, "equipe", None):
                self.show_toast("Aucun gabrimon a soigner", 90)
                return
            for g in comp.equipe:
                if hasattr(g, "pv_max"):
                    g.pv = g.pv_max
            if comp.gabrimon_actuel is None and comp.equipe:
                comp.gabrimon_actuel = comp.equipe[0]
                self.gabrimon_actuel = comp.equipe[0]
            self.show_toast("Equipe soignee", 120)

    def _is_near_point(self, x, y, radius=14):
        px = self.x + (self.taille_x / 2)
        py = self.y + (self.taille_y / 2)
        dx = px - x
        dy = py - y
        return (dx * dx + dy * dy) <= (radius * radius)

    def _update_choix_starter(self):
        # Navigation au clavier (gauche/droite ou 1/2/3) + validation (Entrée).
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_UP):
            self._starter_index = (self._starter_index - 1) % 3
        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.KEY_DOWN):
            self._starter_index = (self._starter_index + 1) % 3

        if pyxel.btnp(pyxel.KEY_1):
            self._starter_index = 0
            self._valider_starter()
        elif pyxel.btnp(pyxel.KEY_2):
            self._starter_index = 1
            self._valider_starter()
        elif pyxel.btnp(pyxel.KEY_3):
            self._starter_index = 2
            self._valider_starter()
        elif pyxel.btnp(pyxel.KEY_RETURN):
            self._valider_starter()

    def _valider_starter(self):
        starters = ["flamigi", "aquapti", "mouskin"]
        gabrimon_id = starters[self._starter_index]
        starter = self.service.engine.get_service("gabrimon").get_gabrimon(gabrimon_id, niveau=5)
        comp = self.get_component("gabrimon")
        comp.equipe = [starter]
        comp.gabrimon_actuel = starter
        self.gabrimon_actuel = starter  # utilisé par Combat
        self._starter_choisi = True
        self.freeze_movement = False
        self.freeze_interact = False


    def set_doorstep(self, id):
        self.doorstep = id

    def teleport(self, world, x, y):
        self.x = x
        self.y = y
        self.service.engine.get_service("map").set_world(world)

    def draw(self):
        if self.service.engine.get_service("combat").is_combat(): return
        pyxel.camera(self.x - pyxel.width // 2, self.y - pyxel.height // 2)
        if not self._starter_choisi:
            self._draw_choix_starter()
        if self.service.engine.states.get("heal_prompt", False):
            ui = self.service.engine.get_service("ui")
            text = "E: Soigner"
            w = 4 * len(text) + 14
            ui.draw_container(img=2, sx=232, sy=232, x=8, y=28, w=w, h=16)
            ui.draw_text(text, 13, 33, 0)
        if self._toast_text:
            ui = self.service.engine.get_service("ui")
            w = 4 * len(self._toast_text) + 14
            ui.draw_container(img=2, sx=232, sy=232, x=8, y=8, w=w, h=16)
            ui.draw_text(self._toast_text, 13, 13, 0)
        if self.doorstep != 0 and self.service.engine.get_service("map").current_world == 0:
            indoorname=self.service.engine.get_service("indoor").get_indoor(self.doorstep).name
            self.service.engine.get_service("ui").draw_container(img=2, sx=232, sy=232, x=10, y=100, w=4*len(indoorname)+10, h=16)
            self.service.engine.get_service("ui").draw_text(indoorname, 15, 105, 0)
        super().draw()

    def show_toast(self, text, duration=120):
        self._toast_text = text
        self._toast_timer = max(1, int(duration))

    def _draw_choix_starter(self):
        ui = self.service.engine.get_service("ui")
        titre = "Choisis ton starter"
        options = ["1) Flamigi", "2) Aquapti", "3) Mouskin"]
        w = max(4 * len(titre) + 16, 4 * max(len(o) for o in options) + 16)
        h = 16 + 12 + (len(options) * 10) + 10
        x = (pyxel.width // 2) - (w // 2)
        y = 30
        ui.draw_container(img=2, sx=232, sy=232, x=x, y=y, w=w, h=h)
        ui.draw_text(titre, x + 8, y + 8, 0)
        for i, opt in enumerate(options):
            color = 11 if i == self._starter_index else 7
            ui.draw_text(opt, x + 10, y + 26 + (i * 10), color)
        ui.draw_text("Entree pour valider", x + 10, y + h - 12, 6)
