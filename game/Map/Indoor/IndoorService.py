from engine.services.Service import Service
from game.Map.Indoor.IndoorData import IndoorData


class IndoorService(Service):

    def init(self):
        self.indoors = {}
        self.indoors[0] = IndoorData(self, 1, "Maison", (0, 0), (0, 0), ((752,512),(15,17)), ((0,0),(0,0)))
        
    def get_indoor(self, id):
        for indoor in self.indoors.values():
            if indoor.id == id:
                return indoor
        return None
