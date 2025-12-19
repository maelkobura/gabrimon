


class Component:
    def __init__(self, entity):
        self.entity = entity

    def init(self):
        pass

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def get_state(self, name):
        return self.entity.get_state(name)

    def set_state(self, name, value):
        return self.entity.set_state(name, value)