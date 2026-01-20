import pyxel

from engine.entity.Entity import Entity
from engine.services.Service import Service


class Personnage(Entity):
    def __init__(self, service: Service):
        super().__init__(service)
        self.taille_x = 16
        self.taille_y = 16
        self.x = 0
        self.y = 0
        self.color = 9
        self.direction = 0

        self.sheet_index = 0
        self.sprite_index = 0
        self.animation_index = 0
        self.animation_speed = 0.1

        self.frame_counter = 0

    def update(self):
        self.frame_counter += 1


        if self.direction == 1:
            self.sprite_index = 4
        elif self.direction == 3:
            self.sprite_index = 0
        elif self.direction == 2:
            self.sprite_index = 8
        elif self.direction == 4:
            self.sprite_index = 12

        if self.frame_counter >= 30*self.animation_speed:
            self.frame_counter = 0
            self.animation_index += 1
            if self.animation_index > 3:
                self.animation_index = 0

    def draw(self):
        pyxel.blt(self.x, self.y, 1, (self.sprite_index + self.animation_index)*16, self.sheet_index*16, self.taille_x, self.taille_y, colkey=13)
        super().draw()
