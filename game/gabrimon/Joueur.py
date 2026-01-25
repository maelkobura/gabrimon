class Joueur:
    def __init__(self, nom, equipe):
        self.nom = nom
        self.equipe = equipe  # liste d'objets Pokemon
        self.pokemon_actuel = equipe[0]  # Pokémon en combat
        self.pc = []  # boite PC
        self.equipe_max = 6

    def choisir_pokemon(self, index):
        self.pokemon_actuel = self.equipe[index]
    def tous_ko(self):
        return all(g.est_ko() for g in self.equipe)
    def ajouter_gabrimon(self, gabrimon):
        if len(self.equipe) < self.equipe_max:
            self.equipe.append(gabrimon)
            return "equipe"
        else:
            self.pc.append(gabrimon)
            return "pc"
