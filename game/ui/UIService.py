from engine.deco.priority import priority
import pyxel
from engine.services.Service import Service


class UIService(Service):

    def init(self):
        self.container_stack = []
        self.text_stack = []

    def draw_container(
            self,
            img,
            sx, sy,
            x, y,
            w, h,
            border=8
    ):
        self.container_stack.append((img, sx, sy, x, y, w, h, border))

    def draw_text(self, text, x, y, color=7):
        self.text_stack.append((text, x, y, color))

    def _draw_container(
            self,
            img,
            sx, sy,
            x, y,
            w, h,
            border=8
    ):
        b = border
        sw = sh = b * 3

        x = int((self.engine.get_state("player_x") - pyxel.width // 2)) + x
        y = int((self.engine.get_state("player_y") - pyxel.height // 2)) + y

        # Coins
        pyxel.blt(x, y, img, sx, sy, b, b,0)
        pyxel.blt(x + w - b, y, img, sx + 2 * b, sy, b, b,0)
        pyxel.blt(x, y + h - b, img, sx, sy + 2 * b, b, b,0)
        pyxel.blt(x + w - b, y + h - b, img, sx + 2 * b, sy + 2 * b, b, b,0)

        # Haut / Bas
        for i in range(x + b, x + w - b, b):
            pyxel.blt(i, y, img, sx + b, sy, b, b)
            pyxel.blt(i, y + h - b, img, sx + b, sy + 2 * b, b, b)

        # Gauche / Droite
        for j in range(y + b, y + h - b, b):
            pyxel.blt(x, j, img, sx, sy + b, b, b)
            pyxel.blt(x + w - b, j, img, sx + 2 * b, sy + b, b, b)

        # Centre
        for i in range(x + b, x + w - b, b):
            for j in range(y + b, y + h - b, b):
                pyxel.blt(i, j, img, sx + b, sy + b, b, b)

    def absx(self, x):
        return int((self.engine.get_state("player_x") - pyxel.width // 2)) + x

    def absy(self, y):
        return int((self.engine.get_state("player_y") - pyxel.height // 2)) + y

    def _draw_text(self, text, x, y, color=7):
        # Position relative à la caméra
        x = int((self.engine.get_state("player_x") - pyxel.width // 2)) + x
        y = int((self.engine.get_state("player_y") - pyxel.height // 2)) + y

        pyxel.text(x, y, text, color)

    @priority(100)
    def draw(self):
        for img, sx, sy, x, y, w, h, border in self.container_stack:
            self.container_stack.pop()
            self._draw_container(img, sx, sy, x, y, w, h, border)
        for text, x, y, color in self.text_stack:
            self.text_stack.pop()
            self._draw_text(text, x, y, color)