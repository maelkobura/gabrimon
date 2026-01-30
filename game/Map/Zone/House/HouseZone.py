from game.Map.Zone.ZoneEvent import ZoneEvent
from game.personnage.entities.Joueur import Joueur


class HouseZone(ZoneEvent):
    def __init__(self, indoor):
        self.indoor = indoor

    def on_enter(self, personnage):
        if type(personnage) == Joueur:
            personnage.set_doorstep(self.indoor.id)

    def on_exit(self, personnage):
        if type(personnage) == Joueur:
            personnage.set_doorstep(0)
