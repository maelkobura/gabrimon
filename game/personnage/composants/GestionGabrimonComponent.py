from engine.entity.Component import Component


class GestionGabrimonComponent(Component):
    def __init__(self, entity):
        super().__init__(entity)
        team_size = getattr(entity, "team_size", 6)
        self.equipe = [
            entity.service.engine.get_service("gabrimon").get_random_gabrimon(),
            entity.service.engine.get_service("gabrimon").get_random_gabrimon(),
            entity.service.engine.get_service("gabrimon").get_random_gabrimon(),
            entity.service.engine.get_service("gabrimon").get_random_gabrimon(),
            entity.service.engine.get_service("gabrimon").get_random_gabrimon(),
            entity.service.engine.get_service("gabrimon").get_random_gabrimon(),
        ][:team_size]  # liste d'objets Pokemon
        self.gabrimon_actuel = None  # Pokemon en combat
        self.pc = []  # boite PC
        self.equipe_max = max(1, team_size)

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
