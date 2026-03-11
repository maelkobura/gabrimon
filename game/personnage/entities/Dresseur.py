import pyxel

from game.personnage.composants.GestionGabrimonComponent import GestionGabrimonComponent
from game.personnage.entities.Personnage import Personnage


class Dresseur(Personnage):
    def __init__(
        self,
        service,
        nom="Dresseur",
        x=0,
        y=0,
        sheet_index=0,
        direction=3,
        interaction_size=31,
        render_sprite=True,
        team_size=None,
    ):
        super().__init__(service)
        self.nom = nom
        self.x = x
        self.y = y
        self.sheet_index = sheet_index
        self.direction = direction
        self.interaction_size = interaction_size
        self.render_sprite = render_sprite
        if team_size is not None:
            self.team_size = team_size

        self.register_component("gabrimon", GestionGabrimonComponent)
        self.gabrimon_actuel = self.get_current_gabrimon()

        self.defeated = False
        self.active_combat = False
        self.combat_cooldown = 0

    def get_current_gabrimon(self):
        for g in self.get_component("gabrimon").equipe:
            if not g.est_ko():
                return g
        return None

    def has_alive_gabrimon(self):
        return self.get_current_gabrimon() is not None

    def _is_player_in_range(self, player):
        px = player.x + player.taille_x / 2
        py = player.y + player.taille_y / 2
        tx = self.x + self.taille_x / 2
        ty = self.y + self.taille_y / 2
        half = self.interaction_size / 2
        return (tx - half <= px <= tx + half) and (ty - half <= py <= ty + half)

    def start_combat(self, player):
        # Ne pas lancer de combat si le joueur n'a plus de Gabrimon en etat de combattre.
        try:
            if player.get_component("gabrimon").tous_ko():
                if hasattr(player, "show_toast"):
                    player.show_toast("Equipe KO: va au centre", 120)
                return
        except Exception:
            pass
        enemy = self.get_current_gabrimon()
        if enemy is None:
            self.defeated = True
            return
        self.gabrimon_actuel = enemy
        self.active_combat = True
        self.service.engine.get_service("combat").start_combat(player, enemy, dresseur=self)

    def update(self):
        super().update()

        if self.combat_cooldown > 0:
            self.combat_cooldown -= 1

        combat_service = self.service.engine.get_service("combat")

        if self.active_combat and not combat_service.is_combat():
            self.active_combat = False
            if not self.has_alive_gabrimon():
                self.defeated = True
            self.combat_cooldown = 60

        if combat_service.is_combat():
            return

        if self.defeated or self.active_combat or self.combat_cooldown > 0:
            return

        player = self.service.get_player()
        if player is None or player.freeze_interact:
            return

        if self._is_player_in_range(player):
            self.start_combat(player)

    def draw(self):
        if self.service.engine.get_service("combat").is_combat():
            return

        player = self.service.get_player()
        if player is not None and not self.defeated and self._is_player_in_range(player):
            pyxel.text(self.x - 6, self.y - 10, "Combat", 7)

        if self.render_sprite:
            super().draw()
