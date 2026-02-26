from engine.services.Service import Service
from game.Map.Indoor.IndoorData import IndoorData
from game.Map.Position import Position


class IndoorService(Service):

    def init(self):
        self.indoors = {}
        self.indoors[0] = IndoorData(self, 1, "Maison", Position(56,131, 1, 1), Position(754,513, 3, 0), ((752,512),(15,17)), ((48,128),(32,24)))
        self.indoors[1] = IndoorData(self, 2, "Maison", Position(1089, 126, 1, 1), Position(714, 825, 3, 0),((712, 824), (15, 17)), ((1080, 126), (32, 24)))
        self.indoors[2] = IndoorData(self, 3, "Maison", Position(633, 126, 1, 1), Position(778, 825, 3, 0),((776, 824), (15, 17)), ((624, 126), (32, 24)))
        self.indoors[3] = IndoorData(self, 4, "Maison", Position(857, 149, 1, 1), Position(602, 912, 3, 0),((600, 911), (15, 17)), ((848, 150), (32, 24)))
        self.indoors[4] = IndoorData(self, 5, "Maison", Position(56, 387, 1, 1), Position(722, 912, 3, 0),((720, 911), (15, 17)), ((48, 384), (32, 24)))
        self.indoors[5] = IndoorData(self, 6, "Maison", Position(633, 382, 1, 1), Position(770, 912, 3, 0),((768, 911), (15, 17)), ((624, 382), (32, 24)))
        self.indoors[6] = IndoorData(self, 7, "Maison", Position(857, 405, 1, 1), Position(746, 993, 3, 0),((744, 992), (15, 17)), ((848, 406), (32, 24)))
        self.indoors[7] = IndoorData(self, 8, "Maison", Position(1089, 382, 1, 1), Position(674, 993, 3, 0),((672, 992), (15, 17)), ((1080, 382), (32, 24)))
        self.indoors[8] = IndoorData(self, 9, "Maison", Position(1336, 399, 1, 1), Position(977.5, 1000.5, 3, 0),((975.5, 999.5), (15, 17)), ((1328, 384), (32, 24)))
        self.indoors[9] = IndoorData(self, 10, "Maison", Position(1345, 127, 1, 1), Position(1546, 480.5, 3, 0),((1544, 479.5), (15, 17)), ((1336, 126), (32, 24)))

        self.indoors[18] = IndoorData(self, 19, "Centre Pokemon", Position(441, 375, 1, 1), Position(1050, 1002.5, 3, 0),((1047.5, 999.5), (15, 17)), ((432, 384), (32, 24)))
        self.indoors[19] = IndoorData(self, 20, "Centre Pokemon", Position(441,123, 1, 1), Position(667,914, 3, 0), ((664,911),(15,17)), ((432,128),(32,24)))
        self.indoors[20] = IndoorData(self, 21, "Grotte", Position(100, 31, 1 , 2), Position(565, 1190, 1, 0),((562,1187),(25,15)),((97,30),(22,15)))
        
    def get_indoor(self, id):
        for indoor in self.indoors.values():
            if indoor.id == id:
                return indoor
        return None
