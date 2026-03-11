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
        # Garde-fou: si toute l'equipe est KO, on ne relance pas un combat.
        try:
            comp = player.get_component("gabrimon")
            if comp.tous_ko():
                if hasattr(player, "show_toast"):
                    player.show_toast("Equipe KO: va au centre", 120)
                return
        except Exception:
            # Si le joueur n'a pas de composant gabrimon, on laisse le combat se lancer.
            pass

        self.combat = Combat(self.engine, player, ennemi, dresseur=dresseur)

    def stop_combat(self):
        self.combat = None

    def update(self):
        if self.combat is not None:
            self.combat.update()

    def draw(self):
        if self.combat is not None:
            self.combat.draw()
