from engine.deco.priority import priority
from engine.services.HostService import HostService
from game.personnage.entities.Joueur import Joueur
from game.personnage.entities.PNJ import PNJ


class PersonnageService(HostService):
    def init(self):
        self.add_child(Joueur(self))

    @priority(20)
    def draw(self):
        super().draw()