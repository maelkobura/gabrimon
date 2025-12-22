from engine.services.HostService import HostService
from game.personnage.entities.Joueur import Joueur
from game.personnage.entities.PNJ import PNJ


class PersonnageService(HostService):
    def init(self):

        self.engine.load("assets/personnages.pyxres")

        self.add_child(Joueur(self))