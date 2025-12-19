from engine.services.HostService import HostService
from example.player.Bot import Bot
from example.player.Player import Player


class PlayerService(HostService):

    def init(self):
        self.add_child(Player(self))
        for i in range(10000):
            self.add_child(Bot(self))

