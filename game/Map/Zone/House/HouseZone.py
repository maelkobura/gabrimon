from game.Map.Zone.ZoneEvent import ZoneEvent
from game.personnage.entities.Joueur import Joueur


class HouseZone(ZoneEvent):
    def __init__(self, indoor):
        self.indoor = indoor
    def on_update(self, personnage):
        if type(personnage) == Joueur:
            personnage.service.engine.get_service("ui").draw_container(img=2, sx=232, sy=232, x=10, y=100, w=32, h=16)
            personnage.service.engine.get_service("ui").draw_text(self.indoor.name, 15, 105, 0)

    def on_enter(self, personnage):
        if type(personnage) == Joueur:
            personnage.set_doorstep(self.indoor.id)
