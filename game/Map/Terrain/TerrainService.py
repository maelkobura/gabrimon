from engine.services.Service import Service
import pyxel

DISABLE_COLLISIONS = False

class TerrainService(Service):
    def init(self):
        # Walls et speed par tilemap

        self.gabrimon_zone = 0.6



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
            (6, -0.5),
            (0,5.5),
            (0,6),
            (1,5.5),
            (1,6),
            (2,6),
            (2,5.5),
            (3,5.5),
            (3,6),
            (4,5.5),
            (4,6),
            (5,6),
            (6,6),
            (7,6),
            (8,6),
            (9,6),
            (10,6),
            (11,6),
            (12,6),
            (5,5.5),
            (6,5.5),
            (7,5.5),
            (8,5.5),
            (9,5.5),
            (10,5.5),
            (11,5.5),
            (12,5.5),
            (6, 4.5),
            (7.5, 5),
            (8.5, 5),
            (5, 4.5),
            (4, 3),
            (5, 3),
            (5.5, 3),
            (4, 2),
            (5, 2),
            (5.5, 2),
            (5, 1),
            (6, 1),

        ]

        speed_1 = {
            (0,0): 0.75,
            (3,0): 0.6
        }

        walls_2 = [
            (0,0),
            (0,1),
            (3,1),
            (1,2),
            (0,3),
            (1,3),
            (2,3),
            (4,3),
            (3,4),
            (2,4.5),
            (0,4.5),
            (1,4.5),
            (0,6),
            (1,6),
            (2,6),
            (3,6),
            (0,7),
            (1,7),
            (2,7),
            (3,7),
            (0,8),
            (1,8),
            (4,7),
            (4,6),

            (6,0),
            (7,0),
            (8,0),
            (9,0),
            (10,0),
            (12,0),
            (5,1),
            (7,1),
            (8,1),
            (9,0.25),
            (10,0.25),
            (11,0.25),
            (12,0.25),
            (12,2),
            (11,2),
            (10,2),
            (9,2),
            (8,2),
            (7,2),
            (6,2),
            (5,2),
            (12,3),
            (11,3),
            (10,3),
            (5,4.5),
            (6,4.5),

            (0,10),
            (1,10),
            (2,10),
            (0,12),
            (1,11.5),
            (2,11.5),
            (3,11.5),
            (3,12.5),
            (3,13),
            (4,12.5),
            (5,12.5),
            (4,9),
            (4,10),
            (5,9),
            (5,10),
            (0,12.5),
            (1,13),
            (2,12.5),

        ]


        walls_3 = [
            (6, 4.5),
            (7.5, 5),
            (8.5, 5),
            (5, 4.5),
            (4, 3),
            (5, 3),
            (5.5, 3),
            (4, 2),
            (5, 2),
            (5.5, 2),
            (5, 1),
            (6, 1),
        ]

        speed_3 = {
            (4, 4.5): 0.6
        }

        self.tilemap_walls = {}
        self.tilemap_speed = {}
        self.set_tilemap_data(0, walls_1, speed_1)
        self.set_tilemap_data(1, walls_2, {})
        self.set_tilemap_data(2, walls_3, speed_3)

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

        walls = self.tilemap_walls.get(tilemap_id, set())
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

    def is_in_gabrimon_zone(self, x, y, tilemap_id=None):
        return self.get_speed(x, y) == self.gabrimon_zone
