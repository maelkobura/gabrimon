import pyxel

from engine.entity.Entity import Entity
from engine.services.Service import Service


class Personnage(Entity):
    def __init__(self, service: Service):
        super().__init__(service)
        self.taille_x = 8
        self.taille_y = 8
        self.x = 0
        self.y = 0
        self.color = 9

    def draw(self):
        pyxel.rect(self.y, self.x, self.taille_x, self.taille_y, 9)