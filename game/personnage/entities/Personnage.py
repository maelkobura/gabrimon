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
        self.idle_sprite_index = 0
        self.animation_speed = 0.1
        self.idle_animation_speed = 0.5

        self.moving_animation_index = 0
        self.idle_animation_index = 0

        self.frame_counter = 0
        self.is_moving = False

    def update(self):
        super().update()
        self.frame_counter += 1

        if self.direction == 1:
            self.sprite_index = 4
        elif self.direction == 3:
            self.sprite_index = 0
        elif self.direction == 2:
            self.sprite_index = 8
        elif self.direction == 4:
            self.sprite_index = 12

        speed = self.idle_animation_speed

        if self.is_moving:
            self.idle_sprite_index = self.sprite_index/2
            speed = self.animation_speed


        if self.frame_counter >= 30*speed:
            self.frame_counter = 0
            if self.is_moving:
                self.moving_animation_index += 1
                if self.moving_animation_index > 3:
                    self.moving_animation_index = 0
            else:
                self.idle_animation_index += 1
                if self.idle_animation_index > 1:
                    self.idle_animation_index = 0

    def draw(self):
        index = self.sheet_index
        anim = self.moving_animation_index
        sprite = self.sprite_index
        if not self.is_moving:
            index+=1
            anim = self.idle_animation_index
            sprite = self.idle_sprite_index
        pyxel.blt(self.x, self.y, 1, (sprite + anim)*16, index*16, self.taille_x, self.taille_y, colkey=13)
        super().draw()
