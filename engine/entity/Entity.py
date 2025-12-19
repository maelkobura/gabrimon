from engine.entity.Component import Component
from engine.services.Service import Service


class Entity:
    def __init__(self, service: Service):
        self.service = service
        self.components = {}

    def register_component(self, name, component):
        c = component(self)
        c.init()
        self.components[name] = c
        return c

    def get_component(self, name):
        return self.components[name]

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def get_state(self, name):
        return self.service.get_state(name)

    def set_state(self, name, value):
        return self.service.set_state(name, value)