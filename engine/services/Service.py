from engine.Engine import Engine


class Service:
    def __init__(self, engine: Engine):
        self.engine = engine

    def init(self):
        pass

    def start(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def get_state(self, name):
        return self.engine.get_state(name)

    def set_state(self, name, value):
        return self.engine.set_state(name, value)

