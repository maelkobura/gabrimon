from engine.services.Service import Service
import pyxel

DISABLE_COLLISIONS = False

class TerrainService(Service):
    def init(self):
        # Walls et speed par tilemap

        walls_1 = [
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

        speed_1 = {
            (0,0): 0.75,
            (3,0): 0.6
        }

        walls_2 = [
            (0,0)
        ]

        self.tilemap_walls = {}
        self.tilemap_speed = {}
        self.set_tilemap_data(0, walls_1, speed_1)
        self.set_tilemap_data(1, walls_2, {})

    def set_tilemap_data(self, tilemap_id, walls=None, speed=None):
        walls_set = set()
        if walls:
            for x, y in walls:
                bx, by = x * 2, y * 2
                walls_set.update([
                    (bx, by),
                    (bx, by + 1),
                    (bx + 1, by),
                    (bx + 1, by + 1),
                ])
        self.tilemap_walls[tilemap_id] = walls_set

        speed_dict = {}
        if speed:
            for (x, y), value in speed.items():
                bx, by = x * 2, y * 2
                speed_dict.update({
                    (bx, by): value,
                    (bx, by + 1): value,
                    (bx + 1, by): value,
                    (bx + 1, by + 1): value,
                })
        self.tilemap_speed[tilemap_id] = speed_dict

    def can_i(self, x, y, largeur, hauteur, tilemap_id=None):
        if DISABLE_COLLISIONS:
            return True
        if tilemap_id is None:
            tilemap_id = self.get_state("current_world")


        walls = self.tilemap_walls.get(tilemap_id)
        corners = [
            (x, y),
            (x + largeur - 1, y),
            (x, y + hauteur - 1),
            (x + largeur - 1, y + hauteur - 1),
        ]

        tilemap = pyxel.tilemap(tilemap_id)
        for px, py in corners:
            tx, ty = px // 8, py // 8
            tile = tilemap.pget(tx, ty)
            if tile in walls:
                return False

        return True

    def get_speed(self, x, y, tilemap_id=None):
        if tilemap_id is None:
            tilemap_id = self.engine.get_state("current_world")

        speed_dict = self.tilemap_speed.get(tilemap_id, {})
        tx, ty = x // 8, y // 8
        tile = pyxel.tilemap(tilemap_id).pget(tx, ty)
        return speed_dict.get(tile, 1.0)