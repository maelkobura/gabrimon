from engine.entity.Component import Component
from game.Map.Position import Position


class TeleportationComponent(Component):

    def __init__(self, entity):
        super().__init__(entity)
        self.next_pos: Position = None

    def _teleport(self, pos: Position):
        self.entity.x = pos.x
        self.entity.y = pos.y
        self.entity.direction = pos.direction
        self.entity.service.engine.get_service("map").set_world(pos.world)

    def teleport(self, pos: Position,transition=True):
        if not transition:
            self._teleport(pos)
        self.next_pos = pos
        self.entity.freeze_movement = True
        self.entity.freeze_interact = True
        self.get_component("transition").transition = 1


    def update(self):
        if self.next_pos is None:
            return
        if self.get_component("transition").transition == 0:
            self._teleport(self.next_pos)
            self.next_pos = None
            self.entity.freeze_movement = False
            self.entity.freeze_interact = False
            self.get_component("transition").transition = 2

