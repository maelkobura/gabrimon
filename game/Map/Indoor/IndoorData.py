from game.Map.Zone.Zone import Zone
from game.Map.Zone.House.HouseZone import HouseZone


class IndoorData:
    def __init__(self, service, id: int, name: str, indoor_point: tuple, outdoor_point: tuple, go_coor: tuple, return_coor: tuple):
        self.id = id
        self.name = name
        self.indoor_point = indoor_point
        self.outdoor_point = outdoor_point
        self.go_coor = go_coor
        self.return_coor = return_coor

        zone_service = service.engine.get_service("zone")

        go_zone = Zone(zone_service, go_coor[0][0], go_coor[0][1], go_coor[1][0], go_coor[1][1], HouseZone(self))
        # TODO Zone de sortie
        service.engine.get_service("zone").add_child(go_zone)
