class Attaque:
    def __init__(self, nom, valeur, type_action):
        self.nom = nom
        self.valeur = valeur # dégâts OU soins
        self.type_action = type_action # "degats" ou "soin"