from engine.Game import Game
from game.Map.MapService import MapService
from game.personnage.PersonnageService import PersonnageService


class GabrimoneCore(Game):
    def init(self):
        self.engine.reg_service("map", MapService)
        self.engine.reg_service("personnages", PersonnageService)