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

        self.etat = "choix_action"
        self.selection_gabrimon = 0
        self.selection_action = 0
        self.timer = 0
        self.resultat = None  # "victoire", "defaite", "capture", "fuite"

        self.gabriball_x = 0
        self.gabriball_y = 0
        self.gabriball_timer = 0
        self.capture_reussie = False
        self.message = ""

        self.xp_a_ajouter = 0
        self.animation_xp = False

        self.texte_combat = ""
        self.timer_texte = 0
        self.bloque_actions = False

        if joueur.gabrimon_actuel is ennemi:
            raise ValueError("Le Gabrimon ennemi doit être une copie")

    def afficher_texte(self, texte, duree=90):
        self.texte_combat = texte
        self.timer_texte = duree
        self.bloque_actions = True

    def decouper_texte(self, texte, max_car=14):
        mots = texte.split(" ")
        lignes = []
        ligne = ""

        for mot in mots:
            if len(ligne) + len(mot) + 1 <= max_car:
                ligne += mot + " "
            else:
                lignes.append(ligne)
                ligne = mot + " "

        lignes.append(ligne)
        return lignes

    def update(self):

        if self.timer_texte > 0:
            self.timer_texte -= 1

            if self.timer_texte > 0 and pyxel.btnp(pyxel.KEY_RETURN):
                self.timer_texte = 0

            if self.timer_texte == 0:
                self.texte_combat = ""
                self.bloque_actions = False

        # Si combat fini
        if self.etat == "fin":
            return

        #Menu principle
        elif self.etat == "choix_action":
            options = ["Attaques" , "Gabrimon", "sacs", "Fuite"]
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
                elif choix == "sacs":
                    self.etat = "sacs"
                    self.timer = 30
                elif choix == "Fuite":
                    self.etat = "fuite"
                    self.timer = 30
            if pyxel.btnp(pyxel.KEY_E):
                self.etat = "capture"
                self.timer = 30




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
            if pyxel.btnp(pyxel.KEY_BACKSPACE):
                self.etat = "choix_action"
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
            if pyxel.btnp(pyxel.KEY_BACKSPACE):
                self.etat = "choix_action"
            if not self.bloque_actions:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    capacite = attaques[self.attaque_selectionnee]

                    if capacite.type_action == "degats":
                        self.joueur.gabrimon_actuel.utiliser_capacite(capacite, self.ennemi)
                        self.afficher_texte(f"{self.joueur.gabrimon_actuel.nom} attaque !",60)

                    elif capacite.type_action == "soin":
                        self.joueur.gabrimon_actuel.utiliser_capacite(capacite, None)
                        self.afficher_texte(f"{self.joueur.gabrimon_actuel.nom} attaque !",60)

                    if self.ennemi.est_ko():
                        xp_gagnee = 10 * self.ennemi.niveau
                        self.joueur.gabrimon_actuel.gagner_xp(xp_gagnee)
                        self.etat = "fin"
                        return

                    self.tour = "ennemi"
                    self.timer = 30
                    self.etat = "animation"

        #Capture
        elif self.etat == "capture":

            # ❌ impossible si ennemi KO
            if self.ennemi.est_ko():
                self.afficher_texte("Impossible de capturer")
                return

            # ✅ taux TOUJOURS défini
            taux = 1 - (self.ennemi.pv / self.ennemi.pv_max)
            import random
            self.afficher_texte("Tentative de capture ...",60)

            if random.random() < taux:
                self.capture_reussie = True
                #capture réussie
                self.gabriball_x = 120
                self.gabriball_y = 70
                self.gabriball_timer = 0
                self.etat = "capture_animation"
                print("Réussi")


            else:
                #échec
                self.gabriball_x = 120
                self.gabriball_y = 70
                self.gabriball_timer = 0
                self.etat = "capture_animation"
                self.capture_reussie = False

                print("Échec")

        if self.etat == "capture_animation":
            self.gabriball_timer += 1

            # Phase 1 : la pokeball tombe
            if self.gabriball_timer < 30:
                self.gabriball_y -= 1

            # Phase 2 : elle tremble
            elif self.gabriball_timer < 90:
                if self.gabriball_timer % 10 < 5:
                    self.gabriball_x += 1
                else:
                    self.gabriball_x -= 1
            elif self.gabriball_timer == 100:
                if self.capture_reussie:
                    self.afficher_texte("Gabrimon capture !", 60 )
                    self.joueur.ajouter_gabrimon(self.ennemi)
                    self.etat = "fin"
                    return
                else:
                    self.afficher_texte("La capture a echouee ...", 60)
                    self.timer = 30
                    self.etat = "animation"
                    self.tour = "ennemi"
                    return





        elif self.etat == "fuite":
            import random
            if random.random() < 0.7:  # 70% chance de fuir
                self.etat = "fin"
                self.afficher_texte("Vous fuiez le combat ...",60)
                print("Fuite")
            else:
                self.tour = "ennemi"
                self.etat = "animation"
                print("pas Fuite")

        # Tour de l'ennemi
        elif self.etat == "animation" and self.tour == "ennemi":
            self.timer -= 1
            if self.timer <= 0:
                import random
                attaque = random.choice(self.ennemi.attaques)
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
        pyxel.text(10, 95, self.joueur.gabrimon_actuel.nom, 7)
        dessiner_barre_pv(
            x=10,
            y=105,
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




        # ----- BARRE D'XP -----
        g = self.joueur.gabrimon_actuel

        barre_x = 9
        barre_y = 112
        barre_largeur = 62
        barre_hauteur = 2

        # Fond de la barre
        pyxel.rect(barre_x, barre_y, barre_largeur, barre_hauteur, 5)

        # Calcul largeur remplie
        xp_ratio = g.xp / g.xp_max
        largeur_xp = int(barre_largeur * xp_ratio)

        # Barre remplie
        pyxel.rect(barre_x, barre_y, largeur_xp, barre_hauteur, 11)


        # coordonnées et taille de ton cadre
        x = 80
        y = 75
        largeur = 75
        hauteur = 40

        # fond et bordure
        pyxel.rect(x, y, largeur, hauteur, 7)
        pyxel.rectb(x, y, largeur, hauteur, 0)

        # texte s’il existe
        if self.texte_combat != "":
            lignes = self.decouper_texte(self.texte_combat, max_car=14)[:4]
            for i, ligne in enumerate(lignes):
                pyxel.text(x + 4, y + 6 + i * 8, ligne, 0)

        # Menu Gabrimon
        if self.etat == "choix_gabrimon":
            pyxel.text(5, 10, "Choisis ton Gabrimon :", 7)
            for i, g in enumerate(self.joueur.equipe):
                couleur = 10 if i == self.selection_gabrimon else 7
                status = "(KO)" if g.est_ko() else ""
                pyxel.text(20, 20 + i*10, f"{g.nom} {status}", couleur)

        # Menu attaques
        if self.etat == "attaque":
            pyxel.text(5, 10, "Choisis une attaque :", 7)
            for i, a in enumerate(self.joueur.gabrimon_actuel.attaques):
                couleur = 10 if i == self.attaque_selectionnee else 7
                pyxel.text(20, 20 + i*10, a.nom, couleur)

        if self.etat == "choix_action":
            options = ["Attaques", "Gabrimon", "sacs", "Fuite"]
            pyxel.text(5, 15, "Que faire ?", 7)
            for i, opt in enumerate(options):
                couleur = 10 if i == self.selection_action else 7
                pyxel.text(20, 25 + i * 10, opt, couleur)

            #Gabriball
            # Partie rouge
            pyxel.circ(40, 4, 4, 8)
            # Partie blanche
            pyxel.circ(40, 4 + 2, 4, 7)
            # Bouton central
            pyxel.circ(40, 4 + 1, 1, 0)
            pyxel.text(30, 3, "E", 7)



        # Affichage victoire / défaite
        elif self.etat == "fin":
            if self.ennemi.est_ko():
                pyxel.text(60, 50, "VICTOIRE", pyxel.COLOR_YELLOW)
            elif self.joueur.tous_ko():
                pyxel.text(60 , 50 ,"Defaite", pyxel.COLOR_RED)

        if self.etat == "capture_animation":
            # Partie rouge
            pyxel.circ(self.gabriball_x, self.gabriball_y, 4, 8)
            # Partie blanche
            pyxel.circ(self.gabriball_x, self.gabriball_y + 2, 4, 7)
            # Bouton central
            pyxel.circ(self.gabriball_x, self.gabriball_y + 1, 1, 0)



