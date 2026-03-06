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
        self.indoors[10] = IndoorData(self, 11, "Arene", Position(187, 748, 1, 1), Position(1594, 952, 3, 0),((1592, 951), (15, 17)), ((177, 753), (32, 24)))
        self.indoors[11] = IndoorData(self, 12, "???", Position(403, 594, 3, 1), Position(131, 594, 3, 1),((128, 592), (16, 16)),((400, 592), (16, 16)))
        #self.indoors[12] = IndoorData(self, 13, "???", Position(187, 748, 3, 1), Position(162, 545, 3, 1),((160, 544), (16, 16),1), ((432, 544), (16, 16),1))
        #self.indoors[13] = IndoorData(self, 14, "???", Position(187, 748, 3, 1), Position(258, 513, 3, 1),((256, 512), (16, 16),1), ((528, 512), (16, 16),1))
        #self.indoors[14] = IndoorData(self, 15, ")???", Position(187, 748, 3, 1), Position(226, 625, 3, 1),((224, 624), (16, 16),1), ((496, 624), (16, 16),1))



        self.indoors[16] = IndoorData(self, 17, "Boutique Pokemon", Position(1594,105 , 1, 1), Position(987, 1099, 3, 0),((984, 1096), (15, 17)), ((1585, 113), (32, 16)))
        self.indoors[17] = IndoorData(self, 18, "Boutique Pokemon", Position(1594,361, 1, 1), Position(643,826.5, 3, 0), ((640,823.5),(15,17)), ((1585,369),(32,16)))
        self.indoors[18] = IndoorData(self, 19, "Centre Pokemon", Position(441, 375, 1, 1),Position(1050, 1002.5, 3, 0), ((1047.5, 999.5), (15, 17)), ((432, 384), (32, 24)))
        self.indoors[19] = IndoorData(self, 20, "Centre Pokemon", Position(441, 123, 1, 1), Position(667, 914, 3, 0),((664, 911), (15, 17)), ((432, 128), (32, 24)))
        self.indoors[20] = IndoorData(self, 21, "Grotte", Position(100, 31, 1 , 2), Position(565, 1190, 1, 0),((562,1187),(25,15)),((97,30),(22,15)))
        self.indoors[21] = IndoorData(self, 22, "Grotte", Position(400, 575, 1, 2), Position(1141.5, 1204, 1, 0),((1138.5, 1201), (25, 15)), ((396, 576), (22, 15)))
        
    def get_indoor(self, id):
        for indoor in self.indoors.values():
            if indoor.a_id == id or indoor.b_id == id:
                return indoor
        return None

    def get_pos(self, abid):
        for indoor in self.indoors.values():
            if indoor.a_id == abid:
                return indoor.indoor_pos
            if indoor.b_id == abid:
                return indoor.outside_pos
        return None
