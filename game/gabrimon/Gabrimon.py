class Gabrimon:
    def __init__(self, nom, pv_max, attaques):
        self.nom = nom
        self.pv_max = pv_max
        self.pv = pv_max
        self.attaques = attaques

    def attaquer(self, attaque, cible):
        cible.subir_degats(attaque.degats)

    def subir_degats(self, degats):
        self.pv -= degats
        if self.pv < 0:
            self.pv = 0

    def est_ko(self):
        return self.pv == 0