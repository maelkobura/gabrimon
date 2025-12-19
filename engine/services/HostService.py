from engine.Engine import Engine
from engine.entity.Entity import Entity
from engine.services.Service import Service


class HostService(Service):
    def __init__(self, engine: Engine):
        self.entities = []
        super().__init__(engine)

    def add_child(self, entity: Entity):
        self.entities.append(entity)

    def remove_child(self, entity: Entity):
        self.entities.remove(entity)

    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self):
        for entity in self.entities:
            entity.draw()