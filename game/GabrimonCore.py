from engine.Game import Game
from game.Map.MapService import MapService
from game.Map.Terrain.TerrainService import TerrainService
from game.Map.Zone.ZoneService import ZoneService
from game.personnage.PersonnageService import PersonnageService
from game.ui.UIService import UIService


class GabrimonCore(Game):
    def init(self):
        self.engine.reg_service("personnages", PersonnageService)
        self.engine.reg_service("map", MapService)
        self.engine.reg_service("zone", ZoneService)
        self.engine.reg_service("terrain", TerrainService)
        self.engine.reg_service("ui", UIService)