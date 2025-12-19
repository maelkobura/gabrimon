from engine.Game import Game
from game.Map.MapService import MapService


class GabrimoneCore(Game):
    def init(self):
        self.engine.reg_service("map", MapService)