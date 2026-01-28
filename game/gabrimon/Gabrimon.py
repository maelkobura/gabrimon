class Gabrimon:
    def __init__(self, nom, pv_max, attaques,type , niveau=1, 
        sprite_u_normal=0,
        sprite_v_normal=0,
        sprite_u_attaque= 0,
        sprite_v_attaque=0,
        sprite_w=31,
        sprite_h=31 ):


        self.type = type
        self.nom = nom
        self.niveau = niveau

        self.xp = 0
        self.xp_max  = 20 * niveau #XP nécessaire pour level up


        self.pv_max = pv_max
        self.pv = pv_max
        self.attaques = attaques

        # 🎨 SPRITE
        self.sprite_bank = 0
        self.sprite_u_normal = sprite_u_normal  # position dans l’image
        self.sprite_v_normal = sprite_v_normal
        self.sprite_u_attaque = sprite_u_attaque
        self.sprite_v_attaque = sprite_v_attaque
        self.sprite_w = sprite_w
        self.sprite_h = sprite_h


    def utiliser_capacite(self, capacite, cible):
        if capacite.type_action == "degats":
            cible.pv -= capacite.valeur
            if cible.pv < 0:
                cible.pv = 0

        elif capacite.type_action == "soin":
            self.pv += capacite.valeur
            if self.pv > self.pv_max:
                self.pv = self.pv_max

    def est_ko(self):
        return self.pv <= 0

    def gagner_xp(self, quantite):
        self.xp += quantite
        while self.xp >= self.xp_max:
            self.xp -= self.xp_max
            self.monter_niveau()

    def monter_niveau(self):
        self.niveau += 1
        self.xp_max = 20 * self.niveau

        self.pv_max += 5
        self.pv = self.pv_max  # soin complet en montant de niveau

    def copie(self):
        return Gabrimon(
            self.nom,
            self.pv_max,
            self.attaques,
            self.niveau,
            self.sprite_bank ,
            self.sprite_u_normal ,
            self.sprite_v_normal ,
            self.sprite_u_attaque ,
            self.sprite_v_attaque ,
            self.sprite_w ,
            self.sprite_h
        )
