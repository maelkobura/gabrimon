from engine.deco.priority import priority
from engine.services.HostService import HostService


class ZoneService(HostService):

    def init(self):
        pass

    def update(self):
        current_world = self.get_state("current_world")
        for entity in self.entities:
            if entity.world == current_world:
                entity.update()



    @priority(15)
    def draw(self):
        super().draw()