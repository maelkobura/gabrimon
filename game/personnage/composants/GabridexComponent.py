from gc import garbage
from itertools import repeat

from engine.Engine import Engine
from engine.entity.Component import Component
from game.ui.UIService import UIService

import pyxel


class GabridexComponent(Component):
    def __init__(self, entity):
        super().__init__(entity)
        self.state = False
        self.index = 0



    def switch(self):
        self.state = not self.state

        if self.state:
            self.entity.freeze_interact = True
            self.entity.freeze_movement = True
        else:
            self.entity.freeze_interact = False
            self.entity.freeze_movement = False

        self.index = 0

    def update(self):
        if not self.state:
            return

        gabrimons = list(
            Engine.INSTANCE.get_service("gabrimon").gabrimons.values()
        )

        if len(gabrimons) == 0:
            return

        if pyxel.btnp(pyxel.KEY_DOWN, hold=15, repeat=2) and self.index < len(gabrimons) - 1:
            self.index += 1
        elif pyxel.btnp(pyxel.KEY_UP, hold=15, repeat=2) and self.index > 0:
            self.index -= 1

    def draw(self):
        if not self.state:
            return

        ui: UIService = Engine.INSTANCE.get_service("ui")

        # ✔ On récupère une vraie liste
        gabrimons = list(
            Engine.INSTANCE.get_service("gabrimon").gabrimons.values()
        )

        total = len(gabrimons)
        if total == 0:
            return

        pyxel.rect(
            ui.absx(0),
            ui.absy(0),
            Engine.INSTANCE.screen_size[0],
            Engine.INSTANCE.screen_size[1],
            15
        )

        pyxel.text(ui.absx(10), ui.absy(10), "Gabridex", 7)

        max_visible = 7
        half = max_visible // 2
        start = self.index - half
        end = self.index + half + 1

        if start < 0:
            start = 0
            end = min(max_visible, total)

        if end > total:
            end = total
            start = max(0, total - max_visible)

        basey = ui.absy(20)

        for i in range(start, end):
            color = 10 if i == self.index else 9

            pyxel.rect(
                ui.absx(10),
                basey,
                Engine.INSTANCE.screen_size[0] / 2 - 20,
                10,
                color
            )

            pyxel.text(
                ui.absx(15),
                basey + 2,
                gabrimons[i].nom,
                7
            )

            basey += 12

        # -------- DÉTAIL DU GABRIMON SÉLECTIONNÉ --------

        gabrimon = gabrimons[self.index]

        pyxel.rect(
            ui.absx(Engine.INSTANCE.screen_size[0] / 2),
            ui.absy(20),
            Engine.INSTANCE.screen_size[0] / 2 - 10,
            Engine.INSTANCE.screen_size[1] - 38,
            9
        )

        pyxel.text(
            ui.absx(Engine.INSTANCE.screen_size[0] / 2 + 5),
            ui.absy(23),
            gabrimon.nom,
            7
        )

        pyxel.blt(
            ui.absx(Engine.INSTANCE.screen_size[0] / 2 + 20),
            ui.absy(44),
            0,
            gabrimon.sprite_u_normal,
            gabrimon.sprite_v_normal,
            -31,
            31,
            colkey=13,
            scale=2
        )

        pyxel.text(
            ui.absx(Engine.INSTANCE.screen_size[0] / 2 + 5),
            ui.absy(93),
            "Type: " + gabrimon.type,
            7
        )
