

from engine.Game import Game
from example.map.building.BuildingService import BuildingService
from example.map.MapService import MapService
from example.player.PlayerService import PlayerService
from example.collision.CollisionService import CollisionService


class GattouzGame(Game):
    def init(self):
        self.engine.reg_service("collision", CollisionService)
        self.engine.reg_service("player", PlayerService)
        self.engine.reg_service("map", MapService)
        self.engine.reg_service("build", BuildingService)