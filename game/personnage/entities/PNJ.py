from game.personnage.entities.Personnage import Personnage


class PNJ(Personnage):
    def __init__(self, service):
        super().__init__(service)
        self.x = 5
        self.y = 5
