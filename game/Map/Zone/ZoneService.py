import pyxel

from engine.deco.priority import priority
from engine.services.HostService import HostService
from engine.services.Service import Service
from game.Map.Zone.TestZone import TestZone
from game.Map.Zone.Zone import Zone


class ZoneService(HostService):
    def init(self):
        self.add_child(Zone(self, 752,512,15,17, TestZone()))

    @priority(15)
    def draw(self):
        super().draw()