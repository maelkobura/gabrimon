import random

from engine.services.Service import Service
from game.gabrimon.Combat import Combat
from game.gabrimon.liste_gabrimon import liste_gabrimon


class CombatService(Service):
    def init(self):
        self.combat = None

    def is_combat(self):
        return not self.combat is None

    def start_combat(self, player, ennemi, dresseur=None):
        self.combat = Combat(self.engine, player, ennemi, dresseur=dresseur)

    def stop_combat(self):
        self.combat = None

    def update(self):
        if self.combat is not None:
            self.combat.update()

    def draw(self):
        if self.combat is not None:
            self.combat.draw()
