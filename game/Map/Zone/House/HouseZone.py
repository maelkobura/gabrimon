from game.Map.Zone.ZoneEvent import ZoneEvent


class TestZone(ZoneEvent):
    def __init__(self, maison_id):
        self.maison_id = maison_id
    def on_update(self, personnage):
        personnage.service.engine.get_service("ui").draw_container(img=2, sx=232, sy=232, x=10, y=100, w=32, h=16)
        personnage.service.engine.get_service("ui").draw_text("Maison", 15, 105,0)