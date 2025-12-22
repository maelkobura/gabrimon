import pyxel

from engine.services.Service import Service


class MapService(Service):

    def init(self):
        self.engine.load("assets/res (5).pyxres")

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, 3000,3000)
