import pyxel

from Joueur import Joueur

def dessiner_barre_pv(x, y, largeur, hauteur, pv, pv_max):
    # Cadre
    pyxel.rect(x - 1, y - 1, largeur + 2, hauteur + 2, 7)

    # Calcul du ratio
    ratio = pv / pv_max
    if ratio < 0:
        ratio = 0

    largeur_pv = int(largeur * ratio)

    # Couleur selon PV
    if ratio > 0.5:
        couleur = 11  # vert
    elif ratio > 0.2:
        couleur = 10  # orange
    else:
        couleur = 8   # rouge

    # Barre de PV
    pyxel.rect(x, y, largeur_pv, hauteur, couleur)

class Combat:
    def __init__(self, joueur: Joueur, ennemi):
        self.joueur = joueur
        self.ennemi = ennemi

        #gabrimon actif
        self.joueur.gabrimon_actuel = self.joueur.equipe[0]

        self.tour = "joueur"
        self.attaque_selectionnee = 0
        # Pokémon en combat

        self.etat = "choix_action"   # choix / animation /fin
        self.selection_gabrimon = 0
        self.selection_action = 0
        self.timer = 0
        self.resultat = None  # "victoire", "defaite", "capture", "fuite"

    def update(self):
        # Si combat fini
        if self.etat == "fin":
            return

        #Menu principle
        elif self.etat == "choix_action":
            options = ["Attaques" , "Gabrimon", "Capture", "Fuite"]
            #déplacement dans le menu
            if pyxel.btnp(pyxel.KEY_UP):
                self.selection_action = (self.selection_action - 1) % len(options)
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.selection_action = (self.selection_action + 1) % len(options)

            #Validation
            if pyxel.btnp(pyxel.KEY_RETURN):
                choix = options[self.selection_action]
                if choix == "Attaques":
                    self.etat = "attaque"
                    self.attaque_selectionnee = 0
                elif choix == "Gabrimon":
                    self.etat = "choix_gabrimon"
                    self.selection_gabrimon = 0
                elif choix == "Capture":
                    self.etat = "capture"
                    self;timer = 30
                elif choix == "Fuite":
                    self.etat = "fuite"
                    self;timer = 30




        # Menu de choix Gabrimon
        elif self.etat == "choix_gabrimon":
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
                    self.etat = "choix_action"  # Retour menu principle

        # Menu des attaques
        elif self.etat == "attaque" and self.tour == "joueur":

            attaques = self.joueur.gabrimon_actuel.attaques

            if pyxel.btnp(pyxel.KEY_UP):
                self.attaque_selectionnee = (self.attaque_selectionnee - 1) % len(self.joueur.gabrimon_actuel.attaques)
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.attaque_selectionnee = (self.attaque_selectionnee + 1) % len(self.joueur.gabrimon_actuel.attaques)
            if pyxel.btnp(pyxel.KEY_RETURN):
                capacite = attaques[self.attaque_selectionnee]

                if capacite.type_action == "degats":
                    self.joueur.gabrimon_actuel.utiliser_capacite(capacite, self.ennemi)
                elif capacite.type_action == "soin":
                    self.joueur.gabrimon_actuel.utiliser_capacite(capacite, None)

                if self.ennemi.est_ko():
                    self.etat = "fin"
                    return

                self.tour = "ennemi"
                self.timer = 30
                self.etat = "animation"

        #Capture
        elif self.etat == "capture":
            import random
            if random.random() < 0.5:
                #capture réussie
                self.resultat = "capture"
                self.etat = "fin"
                print("Réussi")
            else:
                #échec
                self.tour = "ennemi"
                self.timer = 30
                self.etat = "animation"
                print("Échec")

        elif self.etat == "fuite":
            import random
            if random.random() < 0.7:  # 70% chance de fuir
                self.etat = "fin"
                self.resultat = "fuite"
                print("Fuite")
            else:
                self.tour = "ennemi"
                self.etat = "animation"
                print("pas Fuite")

        # Tour de l'ennemi
        elif self.etat == "animation" and self.tour == "ennemi":
            self.timer -= 1
            if self.timer <= 0:
                attaque = self.ennemi.attaques[0]
                self.ennemi.utiliser_capacite(attaque, self.joueur.gabrimon_actuel)

                if self.joueur.gabrimon_actuel.est_ko():
                    self.etat = "choix_gabrimon"
                    self.selection_gabrimon = 0
                    self.tour = "joueur"
                else:
                    self.tour = "joueur"
                    self.etat = "choix_action"


    def draw(self):
        pyxel.cls(0)

        #Affichage pv en forme de barre
            # Gabrimon du joueur
        pyxel.text(10, 5, self.joueur.gabrimon_actuel.nom, 7)
        dessiner_barre_pv(
            x=10,
            y=15,
            largeur=60,
            hauteur=6,
            pv=self.joueur.gabrimon_actuel.pv,
            pv_max=self.joueur.gabrimon_actuel.pv_max
        )

        # Gabrimon ennemi
        pyxel.text(90, 5, self.ennemi.nom, 7)
        dessiner_barre_pv(
            x=90,
            y=15,
            largeur=60,
            hauteur=6,
            pv=self.ennemi.pv,
            pv_max=self.ennemi.pv_max
        )


        # Menu Gabrimon
        if self.etat == "choix_gabrimon":
            pyxel.text(10, 50, "Choisis ton Gabrimon :", 7)
            for i, g in enumerate(self.joueur.equipe):
                couleur = 10 if i == self.selection_gabrimon else 7
                status = "(KO)" if g.est_ko() else ""
                pyxel.text(20, 60 + i*10, f"{g.nom} {status}", couleur)

        # Menu attaques
        if self.etat == "attaque":
            pyxel.text(10, 50, "Choisis une attaque :", 7)
            for i, a in enumerate(self.joueur.gabrimon_actuel.attaques):
                couleur = 10 if i == self.attaque_selectionnee else 7
                pyxel.text(20, 60 + i*10, a.nom, couleur)

        if self.etat == "choix_action":
            options = ["Attaques", "Gabrimon", "Capture", "Fuite"]
            pyxel.text(10, 50, "Que faire ?", 7)
            for i, opt in enumerate(options):
                couleur = 10 if i == self.selection_action else 7
                pyxel.text(20, 60 + i * 10, opt, couleur)

        # Affichage victoire / défaite
        if self.etat == "fin" and self.resultat == "capture" or self.resultat == "fuite":
            if self.resultat == "capture":
                pyxel.text(60, 50, "Gabrimon capturer", pyxel.COLOR_YELLOW)
            elif self.resultat == "fuite":
                pyxel.text(30, 50, "Vous decider de fuir le combat", pyxel.COLOR_YELLOW)


        elif self.etat == "fin":
            if self.ennemi.est_ko():
                pyxel.text(60, 50, "VICTOIRE", pyxel.COLOR_YELLOW)
            else:
                pyxel.text(60, 50, "DEFAITE", pyxel.COLOR_RED)