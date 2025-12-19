from engine.services.Service import Service


class Entity:
    def __init__(self, service: Service):
        self.service = service

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