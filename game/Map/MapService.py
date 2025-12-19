import pyxel

from engine.services.Service import Service


class MapService(Service):

    def init(self):
        self.engine.load("assets/res (5).pyxres")
        self.x = 0
        self.y = 0

    def draw(self):
        pyxel.bltm(0, 0, 0, self.x, self.y, 160, 120)


    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = self.x + 3

        if pyxel.btn(pyxel.KEY_LEFT):
            if self.x >= 0 :
                self.x = self.x - 3