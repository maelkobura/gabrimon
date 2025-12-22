from engine.Game import Game
from game.personnage.PersonnageService import PersonnageService


class GabrimoneCore(Game):
    def init(self):
        self.engine.reg_service("personnages", PersonnageService)