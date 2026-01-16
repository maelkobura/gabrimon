from game.Map.Zone.ZoneEvent import ZoneEvent


class TestZone(ZoneEvent):
    def on_update(self, personnage):
        print("update")
    def on_exit(self, personnage):
        print("exit")
    def on_enter(self, personnage):
        print("enter")