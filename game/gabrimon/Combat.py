import pyxel




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
    def __init__(self, engine, joueur, ennemi, dresseur=None):
        self.joueur = joueur
        self.engine = engine
        self.ennemi = ennemi
        self.dresseur = dresseur

        #gabrimon actif
        self.joueur.gabrimon_actuel = self.joueur.get_component("gabrimon").equipe[0]

        self.tour = "joueur"
        self.attaque_selectionnee = 0
        # Pokémon en combat

        self.etat = "choix_action"
        self.selection_gabrimon = 0
        self.selection_action = 0
        self.timer = 0
        self.timer_fin = -1
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
        self.capture_phase = 0  # 0 = normal, 1 = aspiration, 2 = disparu
        self.capture_scale = 1.0  # taille du sprite ennemi
        self.ennemi_visible = True
        self.sprite_ennemi = "normal"
        self.timer_animation_ennemi = 0
        self.sprite_joueur = "normal"
        self.timer_sprite = 0
        self.lieux = "normal"

        # Son attaque
        pyxel.sound(0).set(
            notes="c3e3g3",
            tones="nnn",
            volumes="777",
            effects="n",
            speed=10
        )

        # Son dégât reçu
        pyxel.sound(1).set(
            notes="f2",
            tones="n",
            volumes="777",
            effects="n",
            speed=5
        )

        if joueur.get_component("gabrimon").gabrimon_actuel is ennemi:
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

    def reset_capture_animation(self):
        self.capture_phase = 0
        self.capture_scale = 1.0

    def _trainer_has_next(self):
        return self.dresseur is not None and self.dresseur.has_alive_gabrimon()

    def _send_next_ennemi(self):
        self.ennemi = self.dresseur.get_current_gabrimon()
        self.ennemi_visible = True
        self.sprite_ennemi = "normal"
        self.timer_animation_ennemi = 0
        self.etat = "choix_action"
        self.tour = "joueur"
        self.afficher_texte(f"{self.dresseur.nom} envoie {self.ennemi.nom} !", 90)

    def update(self):
        # Gestion du sprite d'attaque
        if self.timer_sprite > 0:
            self.timer_sprite -= 1
            if self.timer_sprite <= 0:
                self.sprite_joueur = "normal"

        # Animation attaque ennemi
        if self.sprite_ennemi == "attaque":
            self.timer_animation_ennemi -= 1
            if self.timer_animation_ennemi <= 0:
                self.sprite_ennemi = "normal"

        if self.timer_texte > 0:
            self.timer_texte -= 1

            if self.timer_texte > 0 and pyxel.btnp(pyxel.KEY_RETURN):
                self.timer_texte = 0

            if self.timer_texte == 0:
                self.texte_combat = ""
                self.bloque_actions = False

        # Si combat fini
        if self.etat == "fin":
            if self.timer_fin == -1:
                self.timer_fin = 30 * 3 # 3 secondes à 30 FPS

            if self.timer_fin > 0:
                self.timer_fin -= 1
                if self.timer_fin == 0:
                    print("FIN")
                    self.engine.get_service("combat").stop_combat()
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
            if self.joueur.get_component("gabrimon").tous_ko():
                self.etat = "fin"
                return  # fin du combat, défaite automatique

            # Menu pour choisir un Gabrimon vivant
            if pyxel.btnp(pyxel.KEY_UP):
                self.selection_gabrimon = (self.selection_gabrimon - 1) % len(self.joueur.get_component("gabrimon").equipe)
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.selection_gabrimon = (self.selection_gabrimon + 1) % len(self.joueur.get_component("gabrimon").equipe)
            if pyxel.btnp(pyxel.KEY_BACKSPACE):
                self.etat = "choix_action"
            if pyxel.btnp(pyxel.KEY_RETURN):
                g = self.joueur.get_component("gabrimon").equipe[self.selection_gabrimon]
                if not g.est_ko():
                    self.joueur.get_component("gabrimon").gabrimon_actuel = g
                    self.etat = "choix_action"  # Retour menu principle

        # Menu des attaques
        elif self.etat == "attaque" and self.tour == "joueur":

            attaques = self.joueur.get_component("gabrimon").gabrimon_actuel.attaques

            if pyxel.btnp(pyxel.KEY_LEFT):
                self.attaque_selectionnee = (self.attaque_selectionnee - 1) % len(attaques)
            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.attaque_selectionnee = (self.attaque_selectionnee + 1) % len(attaques)
            if pyxel.btnp(pyxel.KEY_UP):
                self.attaque_selectionnee = (self.attaque_selectionnee - 2) % len(attaques)
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.attaque_selectionnee = (self.attaque_selectionnee + 2) % len(attaques)
            if pyxel.btnp(pyxel.KEY_BACKSPACE):
                self.etat = "choix_action"
            if not self.bloque_actions:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    capacite = attaques[self.attaque_selectionnee]

                    if capacite.type_action == "degats":
                        self.joueur.get_component("gabrimon").gabrimon_actuel.utiliser_capacite(capacite, self.ennemi)
                        pyxel.play(0, 0)  # son attaque
                        self.afficher_texte(f"{self.joueur.get_component("gabrimon").gabrimon_actuel.nom} attaque !",60)
                        self.sprite_joueur = "attaque"
                        self.timer = 30
                        self.etat = "animation_attaque_joueur"
                        self.timer_sprite = 25


                    elif capacite.type_action == "soin":
                        self.joueur.gabrimon_actuel.utiliser_capacite(capacite, None)
                        self.afficher_texte(f"{self.joueur.get_component("gabrimon").gabrimon_actuel.nom} attaque !",60)

                    if self.ennemi.est_ko():
                        xp_gagnee = 10 * self.ennemi.niveau
                        self.joueur.get_component("gabrimon").gabrimon_actuel.gagner_xp(xp_gagnee)
                        if self.dresseur is not None:
                            if self._trainer_has_next():
                                self._send_next_ennemi()
                                return
                        self.ennemi_visible = False
                        self.etat = "fin"
                        return

                    self.tour = "ennemi"
                    self.timer = 80
                    self.etat = "animation"

        #Capture
        elif self.etat == "capture":
            if self.dresseur is not None:
                self.afficher_texte("Impossible de capturer", 60)
                self.etat = "choix_action"
                return

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
                self.gabriball_x = 120
                self.gabriball_y = 70
                self.gabriball_timer = 0

                # ✅ INIT UNE SEULE FOIS
                self.capture_phase = 1
                self.capture_scale = 1.0

                self.etat = "capture_animation"

                print("Réussi")


            else:
                #échec
                self.capture_reussie = False
                self.gabriball_x = 120
                self.gabriball_y = 70
                self.gabriball_timer = 0

                # ✅ INIT UNE SEULE FOIS
                self.capture_phase = 0
                self.capture_scale = 1.0
                self.ennemi_visible = True

                self.etat = "capture_animation"



                print("Échec")

        if self.etat == "capture_animation":
            self.gabriball_timer += 1

            # Phase 1 : la pokeball tombe
            if self.gabriball_timer < 30:
                self.gabriball_y -= 1

            # Phase 2 : elle tremble
            elif self.gabriball_timer < 90:
                self.ennemi_visible = False
                if self.gabriball_timer % 10 < 5:
                    self.gabriball_x += 1

                else:
                    self.gabriball_x -= 1
            elif self.gabriball_timer == 100:
                if self.capture_reussie:
                    self.afficher_texte("Gabrimon capture !", 60 )
                    self.joueur.get_component("gabrimon").ajouter_gabrimon(self.ennemi)
                    self.etat = "fin"
                    return
                else:
                    self.afficher_texte("La capture a echouee ...", 60)
                    self.ennemi_visible = True

                    self.timer = 30
                    self.etat = "animation"
                    self.tour = "ennemi"
                    return

        elif self.etat == "animation_attaque_joueur":
            self.timer -= 1
            if self.timer <= 0:
                self.sprite_joueur = "normal"
                self.tour = "ennemi"
                self.etat = "animation"

        elif self.etat == "capture_animation" and self.capture_phase == 1:
            self.capture_scale -= 0.025
            if self.capture_scale <= 0:
                self.capture_scale = 0
                self.capture_phase = 2  # aspiration terminée



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

                # 👉 DÉBUT animation attaque ennemi
                self.sprite_ennemi = "attaque"
                self.timer_animation_ennemi = 25
                self.afficher_texte(
                    f"{self.ennemi.nom} sauvage attaque !",
                    60
                )
                self.ennemi.utiliser_capacite(attaque, self.joueur.gabrimon_actuel)
                pyxel.play(0, 0)  # son attaque ennemi
                if self.joueur.gabrimon_actuel.est_ko():
                    self.etat = "choix_gabrimon"
                    self.selection_gabrimon = 0
                    self.tour = "joueur"
                else:
                    self.tour = "joueur"
                    self.etat = "choix_action"


    def draw(self):

        pyxel.cls(5)
        pyxel.camera(0,0)
        if self.lieux =="normal":
            pyxel.bltm(0, 0, 2, 0, 1150, 180, 180)
            couleur_text = 14
        elif self.lieux =="grotte":
            pyxel.bltm(0, 0, 2, 0, 1280, 180, 180)
            couleur_text = 7
        #pyxel.load("../assets/arriere_plan_combat.png")
        #pyxel.images[1].load(0,0, self.engine.get_absolute_path("/assets/arriere_plan_combat.png"))
        #pyxel.images[1].blt(0,0,1,0,0,self.engine.screen_size[0],self.engine.screen_size[1])

        #Affichage pv en forme de barre
            # Gabrimon du joueur

        pyxel.text(90, 70, self.joueur.gabrimon_actuel.nom, couleur_text)

        dessiner_barre_pv(
            x=90,
            y=80,
            largeur=60,
            hauteur=6,
            pv=self.joueur.get_component("gabrimon").gabrimon_actuel.pv,
            pv_max=self.joueur.get_component("gabrimon").gabrimon_actuel.pv_max
        )

        # Gabrimon ennemi
        pyxel.text(90, 5, self.ennemi.nom, couleur_text)
        pyxel.rect(90, 15, 60, 6, 5)
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

        barre_x = 89
        barre_y = 87
        barre_largeur = 62
        barre_hauteur = 2

        # Fond de la barre
        pyxel.rect(barre_x, barre_y, barre_largeur, barre_hauteur, 5)

        # Calcul largeur remplie
        xp_ratio = g.xp / (20 * g.niveau)
        largeur_xp = int(barre_largeur * xp_ratio)

        # Barre remplie
        pyxel.rect(barre_x, barre_y, largeur_xp, barre_hauteur, 11)


        # coordonnées et taille de ton cadre
        menu_x = 0
        menu_y = 88
        menu_largeur = 160
        menu_hauteur = 32

        # fond et bordure
        pyxel.rect(menu_x, menu_y, menu_largeur, menu_hauteur, 13)
        pyxel.rectb(menu_x, menu_y, menu_largeur, menu_hauteur, 0)

        # texte s’il existe
        # (texte de combat dessine plus bas, a la place de l'ancien menu)

        # Menu Gabrimon
        if self.etat == "choix_gabrimon":
            pyxel.text(menu_x + 6, menu_y + 3, "Choisis ton Gabrimon:", couleur_text)
            for i, g in enumerate(self.joueur.get_component("gabrimon").equipe):
                colonne = i % 2
                ligne = i // 2

                x = menu_x + 6 + colonne * 78
                y = menu_y + 12 + ligne * 8

                couleur = 10 if i == self.selection_gabrimon else couleur_text
                status = "(KO)" if g.est_ko() else ""

                pyxel.text(x, y, f"{g.nom} {status}", couleur)

        # Menu attaques
        if self.etat == "attaque":
            pyxel.text(menu_x + 6, menu_y + 3, "Choisis une attaque :", couleur_text)
            for i, a in enumerate(self.joueur.get_component("gabrimon").gabrimon_actuel.attaques):
                couleur = 10 if i == self.attaque_selectionnee else couleur_text
                colonne = i % 2
                ligne = i // 2
                x = menu_x + 6 + colonne * 78
                y = menu_y + 12 + ligne * 8
                pyxel.text(x, y, a.nom, couleur)

        if self.etat == "choix_action":
            options = ["Attaques", "Gabrimon", "sacs", "Fuite"]
            pyxel.text(menu_x + 6, menu_y + 3, "Que faire ?", couleur_text)
            positions = [
                (menu_x + 6, menu_y + 13),
                (menu_x + 86, menu_y + 13),
                (menu_x + 6, menu_y + 21),
                (menu_x + 86, menu_y + 21),
            ]
            for i, opt in enumerate(options):
                px, py = positions[i]
                couleur = 10 if i == self.selection_action else couleur_text
                pyxel.text(px, py, opt, couleur)

            #Gabriball
            # Partie rouge
            pyxel.circ(40, 4, 4, 8)
            # Partie blanche
            pyxel.circ(40, 4 + 2, 4, 7)
            # Bouton central
            pyxel.circ(40, 4 + 1, 1, 0)
            pyxel.text(30, 3, "E", 7)

        # Texte de combat: affiche a la place de l'ancien menu (en haut a gauche)
        if self.texte_combat != "":
            x_msg = 3
            y_msg = 10
            largeur_msg = 70
            hauteur_msg = 24
            pyxel.rect(x_msg, y_msg, largeur_msg, hauteur_msg, 13)
            pyxel.rectb(x_msg, y_msg, largeur_msg, hauteur_msg, 0)
            lignes = self.decouper_texte(self.texte_combat, max_car=18)[:2]
            for i, ligne in enumerate(lignes):
                pyxel.text(x_msg + 4, y_msg + 6 + i * 8, ligne, 7)



        # Affichage victoire / défaite
        elif self.etat == "fin":
            if self.ennemi.est_ko():
                pyxel.text(60, 50, "VICTOIRE", pyxel.COLOR_YELLOW)
            elif self.joueur.get_component("gabrimon").tous_ko():
                pyxel.text(60 , 50 ,"Defaite", pyxel.COLOR_RED)

        if self.etat == "capture_animation":
            # Partie rouge
            pyxel.circ(self.gabriball_x, self.gabriball_y, 4, 8)
            # Partie blanche
            pyxel.circ(self.gabriball_x, self.gabriball_y + 2, 4, 7)
            # Bouton central
            pyxel.circ(self.gabriball_x, self.gabriball_y + 1, 1, 0)

        g = self.joueur.get_component("gabrimon").gabrimon_actuel

        if g.nom == "Rocling":
            colkey_info = 7
        else:
            colkey_info = 13



        e = self.ennemi
        if e.nom == "Rocling":
            colkey_ennemi = 7
        else:
            colkey_ennemi = 13

        TAILLE_SPRITE = 31
        X_ENNEMI = 102
        Y_ENNEMI = 25

        # ===== AFFICHAGE GABRIMON ENNEMI =====

        if self.etat == "capture_animation" and self.capture_phase == 1:
            taille = int(31 * self.capture_scale)

            if taille > 0:
                pyxel.blt(
                    X_ENNEMI + (31 - taille) // 2,
                    Y_ENNEMI + (31 - taille) // 2,
                    0,
                    e.sprite_u_normal,
                    e.sprite_v_normal,
                    taille,
                    taille,
                    colkey=colkey_ennemi
                )


        elif self.ennemi_visible:
            if e.nom == "Givrin":
                w = 44
                h = 47
                X_ENNEMI = 95
                Y_ENNEMI = 20
            elif e.nom == "Psymio":
                X_ENNEMI = 108
                Y_ENNEMI = 28
            else :
                w = 31
                h = 31
            # normal ou attaque
            if self.sprite_ennemi == "attaque":
                u, v = e.sprite_u_attaque, e.sprite_v_attaque
                X_ENNEMI = X_ENNEMI-3
            else:
                u, v = e.sprite_u_normal, e.sprite_v_normal

            pyxel.blt(
                X_ENNEMI,
                Y_ENNEMI,
                0,
                u,
                v,
                31,
                31,
                colkey=colkey_ennemi
            )

        if g.nom == "Givrin":
            x = 40
            y = 45
        else:
            x = 45
            y = 50
        if g.nom == "Psymio":
            x = 43
            y = 55
        else:
            x = 45
            y = 50

        if self.sprite_joueur == "attaque":
            u, v = g.sprite_u_attaque , g.sprite_v_attaque
            x= x+3
        else:
            u , v = g.sprite_u_normal , g.sprite_v_normal


        pyxel.blt(
            x, y,
            0,
            u, v,
            -g.sprite_w,
            g.sprite_h,
            colkey=colkey_info
        )




