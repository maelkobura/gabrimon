from engine.services.HostService import HostService
from example.map.building.HouseEntity import HouseEntity


class BuildingService(HostService):

    def init(self):
        self.add_child(HouseEntity(self))