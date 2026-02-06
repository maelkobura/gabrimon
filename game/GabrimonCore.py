from engine.Game import Game
from game.Map.Indoor.IndoorService import IndoorService
from game.Map.MapService import MapService
from game.Map.Terrain.TerrainService import TerrainService
from game.Map.Zone.ZoneService import ZoneService
from game.personnage.PersonnageService import PersonnageService
from game.gabrimon.GabrimonService import GabrimonService
from game.ui.UIService import UIService
from game.gabrimon.CombatService import CombatService


class GabrimonCore(Game):
    def init(self):
        self.engine.reg_service("gabrimon", GabrimonService)
        self.engine.reg_service("personnages", PersonnageService)
        self.engine.reg_service("map", MapService)
        self.engine.reg_service("zone", ZoneService)
        self.engine.reg_service("terrain", TerrainService)
        self.engine.reg_service("ui", UIService)
        self.engine.reg_service("indoor", IndoorService)
        self.engine.reg_service("combat", CombatService)