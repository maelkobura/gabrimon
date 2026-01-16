from engine.deco.priority import priority
from engine.services.HostService import HostService
from game.Map.Zone.House.HouseZone import TestZone
from game.Map.Zone.Zone import Zone


class ZoneService(HostService):
    def init(self):
        self.add_child(Zone(self, 752,512,15,17, TestZone(1)))

    @priority(15)
    def draw(self):
        super().draw()