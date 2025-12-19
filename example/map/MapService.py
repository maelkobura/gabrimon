import pyxel

from engine.services.Service import Service


class MapService(Service):

    def draw(self):
        camera_x = self.get_state("camera_x")
        camera_y = self.get_state("camera_y")

        grid_size = 25

        start_x = (camera_x // grid_size) * grid_size
        for x in range(start_x, camera_x + self.engine.screen_size[0] + grid_size, grid_size):
            pyxel.line(x, camera_y, x, camera_y + self.engine.screen_size[1] - 1, 1)

        start_y = (camera_y // grid_size) * grid_size
        for y in range(start_y, camera_y + self.engine.screen_size[1] + grid_size, grid_size):
            pyxel.line(camera_x, y, camera_x + self.engine.screen_size[0] - 1, y, 1)