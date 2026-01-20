import pyxel
from Joueur import Joueur

class Combat:
    def __init__(self, joueur: Joueur, ennemi):
        self.joueur = joueur
        self.ennemi = ennemi

        #gabrimon actif
        self.joueur.gabrimon_actuel = self.joueur.equipe[0]

        self.tour = "joueur"
        self.attaque_selectionnee = 0
        # Pokémon en combat

        self.etat = "choix_gabrimon"   # choix / animation /fin
        self.selection_gabrimon = 0
        self.timer = 0


    def update(self):
        # Si combat fini
        if self.etat == "fin":
            return

        # Menu de choix Gabrimon
        if self.etat == "choix_gabrimon":
            #Vérifier si tous les Gabrimon du joueur sont KO
            if self.joueur.tous_ko():
                self.etat = "fin"
                return  # fin du combat, défaite automatique

            # Menu pour choisir un Gabrimon vivant
            if pyxel.btnp(pyxel.KEY_UP):
                self.selection_gabrimon = (self.selection_gabrimon - 1) % len(self.joueur.equipe)
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.selection_gabrimon = (self.selection_gabrimon + 1) % len(self.joueur.equipe)
            if pyxel.btnp(pyxel.KEY_RETURN):
                g = self.joueur.equipe[self.selection_gabrimon]
                if not g.est_ko():
                    self.joueur.gabrimon_actuel = g
                    self.etat = "choix"  # Retour menu attaques

        # Menu des attaques
        elif self.etat == "choix" and self.tour == "joueur":
            if pyxel.btnp(pyxel.KEY_UP):
                self.attaque_selectionnee = (self.attaque_selectionnee - 1) % len(self.joueur.gabrimon_actuel.attaques)
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.attaque_selectionnee = (self.attaque_selectionnee + 1) % len(self.joueur.gabrimon_actuel.attaques)
            if pyxel.btnp(pyxel.KEY_RETURN):
                attaque = self.joueur.gabrimon_actuel.attaques[self.attaque_selectionnee]
                self.joueur.gabrimon_actuel.attaquer(attaque, self.ennemi)

                if self.ennemi.est_ko():
                    self.etat = "fin"
                    return

                self.tour = "ennemi"
                self.timer = 30
                self.etat = "animation"

        # Tour de l'ennemi
        elif self.etat == "animation" and self.tour == "ennemi":
            self.timer -= 1
            if self.timer <= 0:
                attaque = self.ennemi.attaques[0]
                self.ennemi.attaquer(attaque, self.joueur.gabrimon_actuel)

                if self.joueur.gabrimon_actuel.est_ko():
                    self.etat = "choix_gabrimon"
                    self.selection_gabrimon = 0
                    self.tour = "joueur"
                else:
                    self.tour = "joueur"
                    self.etat = "choix"
    def draw(self):
        pyxel.cls(0)

        # Affichage PV
        pyxel.text(10, 10, f"{self.joueur.gabrimon_actuel.nom} PV: {self.joueur.gabrimon_actuel.pv}", 7)
        pyxel.text(10, 20, f"{self.ennemi.nom} PV: {self.ennemi.pv}", 8)

        # Menu Gabrimon
        if self.etat == "choix_gabrimon":
            pyxel.text(10, 50, "Choisis ton Gabrimon :", 7)
            for i, g in enumerate(self.joueur.equipe):
                couleur = 10 if i == self.selection_gabrimon else 7
                status = "(KO)" if g.est_ko() else ""
                pyxel.text(20, 60 + i*10, f"{g.nom} {status}", couleur)

        # Menu attaques
        if self.etat == "choix":
            pyxel.text(10, 50, "Choisis une attaque :", 7)
            for i, a in enumerate(self.joueur.gabrimon_actuel.attaques):
                couleur = 10 if i == self.attaque_selectionnee else 7
                pyxel.text(20, 60 + i*10, a.nom, couleur)

        # Affichage victoire / défaite
        if self.etat == "fin":
            if self.ennemi.est_ko():
                pyxel.text(60, 50, "VICTOIRE", pyxel.COLOR_YELLOW)
            else:
                pyxel.text(60, 50, "DEFAITE", pyxel.COLOR_RED)