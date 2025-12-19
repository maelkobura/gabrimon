from engine.services.HostService import HostService
from game.personnage.Joueur import Joueur
from game.personnage.PNJ import PNJ


class PersonnageService(HostService):
    def init(self):
        self.add_child(Joueur(self))
        self.add_child(PNJ(self))