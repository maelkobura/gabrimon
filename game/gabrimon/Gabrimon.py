class Gabrimon:
    def __init__(
        self,
        nom,
        pv_max,
        attaques,
        type,
        niveau=1,
        sprite_bank=0,
        sprite_u_normal=0,
        sprite_v_normal=0,
        sprite_u_attaque=0,
        sprite_v_attaque=0,
        sprite_w=31,
        sprite_h=31,
    ):
        self.type = type
        self.nom = nom

        self.xp = 0
        self.xp_max = 20  # recalcule par set_niveau()

        # Base PV (niveau 1), sert a recalculer pv_max en fonction du niveau.
        self.pv_base = int(pv_max)

        self.pv_max = int(pv_max)
        self.pv = int(pv_max)
        self.attaques = attaques

        # Sprites
        self.sprite_bank = sprite_bank
        self.sprite_u_normal = sprite_u_normal
        self.sprite_v_normal = sprite_v_normal
        self.sprite_u_attaque = sprite_u_attaque
        self.sprite_v_attaque = sprite_v_attaque
        self.sprite_w = sprite_w
        self.sprite_h = sprite_h

        self.niveau = 1
        self.set_niveau(niveau, full_heal=True)

    def set_niveau(self, niveau, *, full_heal=True):
        """
        Met a jour les stats dependantes du niveau (pv_max, xp_max).

        full_heal=True: PV actuels = PV max (utile au spawn).
        full_heal=False: n'effectue pas un soin complet: on ajoute seulement
        l'augmentation de PV max (comportement type Pokemon).
        """
        niveau = max(1, int(niveau))

        old_pv_max = self.pv_max
        self.niveau = niveau
        self.xp_max = 20 * self.niveau
        self.pv_max = self.pv_base + 5 * (self.niveau - 1)

        if full_heal:
            self.pv = self.pv_max
        else:
            gain = max(0, self.pv_max - old_pv_max)
            self.pv = min(self.pv_max, self.pv + gain)

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
        # Pas de soin complet au level-up.
        self.set_niveau(self.niveau + 1, full_heal=False)

    def copie(self):
        # Copie "template": meme base + meme niveau, PV pleins.
        return Gabrimon(
            nom=self.nom,
            pv_max=self.pv_base,
            attaques=self.attaques,
            type=self.type,
            niveau=self.niveau,
            sprite_bank=self.sprite_bank,
            sprite_u_normal=self.sprite_u_normal,
            sprite_v_normal=self.sprite_v_normal,
            sprite_u_attaque=self.sprite_u_attaque,
            sprite_v_attaque=self.sprite_v_attaque,
            sprite_w=self.sprite_w,
            sprite_h=self.sprite_h,
        )

