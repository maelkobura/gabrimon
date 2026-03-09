from engine.deco.priority import priority
from engine.services.HostService import HostService
from game.personnage.entities.Joueur import Joueur
from game.personnage.entities.Dresseur import Dresseur
from game.personnage.entities.PNJ import PNJ


class PersonnageService(HostService):
    def init(self):
        self.player = self.add_child(Joueur(self))
        self.add_child(
            Dresseur(
                self,
                nom="Lia",
                x=129,
                y=688,
                sheet_index=0,
                direction=2,
                interaction_size=31,
                render_sprite=False,
            )
        )
        self.add_child(
            Dresseur(
                self,
                nom="Dresseur 2",
                x=208,
                y=576,
                sheet_index=0,
                direction=2,
                interaction_size=31,
                render_sprite=False,
            )
        )
        self.add_child(
            Dresseur(
                self,
                nom="Dresseur 3",
                x=449,
                y=656,
                sheet_index=0,
                direction=2,
                interaction_size=31,
                render_sprite=False,
            )
        )
        self.add_child(
            Dresseur(
                self,
                nom="Dresseur 4",
                x=401,
                y=495,
                sheet_index=0,
                direction=2,
                interaction_size=31,
                render_sprite=False,
            )
        )
        self.add_child(
            Dresseur(
                self,
                nom="Dresseur 5",
                x=193,
                y=520,
                sheet_index=0,
                direction=2,
                interaction_size=31,
                render_sprite=False,
            )
        )

    def get_player(self):
        return self.player

    @priority(20)
    def draw(self):
        super().draw()
