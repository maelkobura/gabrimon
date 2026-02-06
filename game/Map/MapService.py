import pyxel

from engine.deco.priority import priority
from engine.services.Service import Service


class MapService(Service):

    def init(self):
        self.current_world = 0
        self.engine.load("assets/GABRIMON.pyxres")
        self.set_state("current_world", self.current_world)

    def set_world(self, world: int):
        self.current_world = world
        self.set_state("current_world", world)

    @priority(0)
    def draw(self):
        if self.engine.get_service("combat").is_combat(): return
        pyxel.bltm(0, 0, self.current_world, 0, 0, 3000,3000)
