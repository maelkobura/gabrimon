from engine.services.Service import Service

class TerrainService(Service):
    def init(self):
        speed_modifier = {
            (0, 2): {"speed": 0.0},
            (1, 2): {"speed": 0.0},
            (0, 3): {"speed": 0.0},
            (1, 3): {"speed": 0.0},
        }

    def can_i(self, dy, dx, x, y):
        return True


