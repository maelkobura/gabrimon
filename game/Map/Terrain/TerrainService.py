from engine.services.Service import Service
import pyxel

class TerrainService(Service):
    def init(self):
        walls = [
            (1, 0),
            (0, 1),
            (2, 0),
            (1, 1),
            (2, 1),
            (3, 1),
            (0, 2),
            (1, 2),
            (2, 2),
        ]

        speed = {
            (0,0): 0.75,
            (3,0): 0.6
        }

        self.walls = []
        self.speed = {}

        for x, y in walls:
            bx, by = x * 2, y * 2
            self.walls.extend([
                (bx, by),
                (bx, by + 1),
                (bx + 1, by),
                (bx + 1, by + 1),
            ])

        for (x, y), value in speed.items():
            bx, by = x * 2, y * 2
            self.speed.update({
                (bx, by): value,
                (bx, by + 1): value,
                (bx + 1, by): value,
                (bx + 1, by + 1): value,
            })


    def can_i(self, x, y, largeur, hauteur):
        corners = [
            (x, y),
            (x + largeur-1, y),
            (x, y + hauteur-1),
            (x + largeur-1, y + hauteur-1),
        ]

        for px, py in corners:
            tx, ty = px // 8, py // 8
            tile = pyxel.tilemap(
                self.engine.get_service("map").current_level

            ).pget(tx, ty)

            if tile in self.walls:
                return True

        return False

    def get_speed(self, x, y):
        tx, ty = x // 8, y // 8
        tile = pyxel.tilemap(self.engine.get_service("map").current_level).pget(tx, ty)
        return self.speed.get(tile, 1.0)
