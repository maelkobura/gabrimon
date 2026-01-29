from engine.services.Service import Service
from game.Map.Indoor.IndoorData import IndoorData
from game.Map.Position import Position


class IndoorService(Service):

    def init(self):
        self.indoors = {}
        self.indoors[0] = IndoorData(self, 1, "Maison", Position(56,131, 1, 1), Position(754,513, 3, 0), ((752,512),(15,17)), ((48,128),(32,24)))
        self.indoors[1] = IndoorData(self, 2, "Chambre", Position(282,67, 1, 1), Position(642,827, 3, 0), ((640,824),(15,17)), ((272,64),(32,24)))
        
    def get_indoor(self, id):
        for indoor in self.indoors.values():
            if indoor.id == id:
                return indoor
        return None
