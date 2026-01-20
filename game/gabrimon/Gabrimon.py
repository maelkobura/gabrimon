class Gabrimon:
    def __init__(self, nom, pv_max, attaques):
        self.nom = nom
        self.pv_max = pv_max
        self.pv = pv_max
        self.attaques = attaques

    def utiliser_capacite(self, capacite, cible):
        if capacite.type_action == "degats":
            cible.pv -= capacite.valeur
            if cible.pv < 0:
                cible.pv = 0

        elif capacite.type_action == "soin":
            self.pv += capacite.valeur
            if self.pv > self.pv_max:
                self.pv = self.pv_max

    def est_ko(self):
        return self.pv <= 0