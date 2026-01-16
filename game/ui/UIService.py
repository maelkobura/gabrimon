from engine.services.Service import Service


class UIService(Service):

    def draw_container(
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