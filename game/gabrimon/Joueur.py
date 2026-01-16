class Joueur:
    def __init__(self, nom, equipe):
        self.nom = nom
        self.equipe = equipe  # liste d'objets Pokemon
        self.pokemon_actuel = equipe[0]  # Pokémon en combat

    def choisir_pokemon(self, index):
        self.pokemon_actuel = self.equipe[index]
    def tous_ko(self):
        return all(g.est_ko() for g in self.equipe)