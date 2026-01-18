from engine.entity.Component import Component
import pyxel

class TransitionAnimationComponent(Component):
    def __init__(self, entity):
        super().__init__(entity)
        self.transition = -1 # 0 = ecran noir, 1 = transition fermeture, 2 = transition ouverture, -1 = pas de transition (ecran normal)
        self.step = 0
        self.screen_size = entity.service.engine.screen_size
        self.speed = 2.0

    def draw(self):
        x = int((self.entity.get_state("player_x") - pyxel.width // 2))
        y = int((self.entity.get_state("player_y") - pyxel.height // 2))
        if self.transition == 1:

            pyxel.rect(x, y, self.screen_size[0], self.step, 0)
            pyxel.rect(x, y+int(self.screen_size[1]) - self.step, self.screen_size[0], int(self.screen_size[1]),0)

            if self.step <= self.screen_size[1]/2:
                self.step = int(self.speed*(self.step+1))
            else:
                self.transition = 0
                self.step = 0

        elif self.transition == 2:
            pyxel.rect(x, y, self.screen_size[0], int(self.screen_size[1] / 2) - self.step, 0)

            pyxel.rect(
                x,
                y + int(self.screen_size[1] / 2) + self.step,
                self.screen_size[0],
                int(self.screen_size[1] / 2) - self.step,
                0
            )

            if self.step <= self.screen_size[1]/2:
                self.step = int(self.speed * (self.step + 1))
            else:
                self.transition = -1
                self.step = 0
        elif self.transition == 0:
            pyxel.rect(x, y, self.screen_size[0], self.screen_size[1], 0)



