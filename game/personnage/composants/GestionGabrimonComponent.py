from engine.entity.Component import Component


class GestionGabrimonComponent(Component):
    def __init__(self, entity):
        super().__init__(entity)
        self.equipe = [
            entity.service.engine.get_service("gabrimon").get_random_gabrimon(),
            entity.service.engine.get_service("gabrimon").get_random_gabrimon(),
            entity.service.engine.get_service("gabrimon").get_random_gabrimon(),
            entity.service.engine.get_service("gabrimon").get_random_gabrimon(),
            entity.service.engine.get_service("gabrimon").get_random_gabrimon(),
            entity.service.engine.get_service("gabrimon").get_random_gabrimon()
        ]  # liste d'objets Pokemon
        self.gabrimon_actuel = None # Pokémon en combat
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
