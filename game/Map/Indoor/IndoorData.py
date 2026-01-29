from game.Map.Position import Position
from game.Map.Zone.Zone import Zone
from game.Map.Zone.House.HouseZone import HouseZone


class IndoorData:
    def __init__(self, service, id: int, name: str, indoor_pos: Position, outside_pos: Position, go_coor: tuple, return_coor: tuple):
        self.id = id
        self.name = name
        self.indoor_pos = indoor_pos
        self.outside_pos = outside_pos
        self.go_coor = go_coor
        self.return_coor = return_coor

        zone_service = service.engine.get_service("zone")

        go_zone = Zone(zone_service, go_coor[0][0], go_coor[0][1], go_coor[1][0], go_coor[1][1], HouseZone(self))
        out_zone = Zone(zone_service, return_coor[0][0], return_coor[0][1], return_coor[1][0], return_coor[1][1], HouseZone(self),1)
        service.engine.get_service("zone").add_child(go_zone)
        service.engine.get_service("zone").add_child(out_zone)
