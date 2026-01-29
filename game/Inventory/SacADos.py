"""

class SacADos:
    def __init__(self, x, y, width, height, max_pages):

        Initialise le sac à dos.
        x, y: Position du coin en haut a gauche du sac
        width, height: Taille du rectangle
        max_pages: Nombre total de pages du sac

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.est_ouvert = False
        self.page_actuelle = 1
        self.max_pages = max_pages

        self.col_fond = 10
        self.col_bordure = 7
        self.col_texte = 0

    def update(self):
        Gère les touche du clavier pour le sac à dos.

        # Ouvrir / Fermer avec la touche B
        if pyxel.btnp(pyxel.KEY_B):
            self.est_ouvert = not self.est_ouvert

        if self.est_ouvert:
            # Flèche Droite, Page suivante
            if pyxel.btnp(pyxel.KEY_RIGHT):
                if self.page_actuelle < self.max_pages:
                    self.page_actuelle += 1

            # Flèche Gauche, Page précédente
            if pyxel.btnp(pyxel.KEY_LEFT):
                if self.page_actuelle > 1:
                    self.page_actuelle -= 1

    def draw(self):
        Affiche le sac à dos s'il est ouvert.
        if self.est_ouvert:
            pyxel.rect(self.x, self.y, self.width, self.height, self.col_fond)
            pyxel.rectb(self.x, self.y, self.width, self.height, self.col_bordure)

            titre = "SAC A DOS"
            pyxel.text(self.x + 10, self.y + 10, titre, self.col_texte)

            info_page = f"PAGE {self.page_actuelle} / {self.max_pages}"
            pyxel.text(self.x + 55, self.y + 15, info_page, self.col_texte)

            pyxel.text(self.x + 10, self.y + 30, f"Contenu de la page {self.page_actuelle}...", 13)


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Demo Sac a Dos")

        self.mon_sac = SacADos(x=30, y=20, width=100, height=80, max_pages=3)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.mon_sac.update()

    def draw(self):
        pyxel.cls(0)

        if not self.mon_sac.est_ouvert:
            pyxel.text(40, 50, "Appuie sur B", 7)

        self.mon_sac.draw()


App()
"""