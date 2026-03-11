import random
from pathlib import Path
import json

from engine.services.Service import Service
from game.gabrimon.Attaque import Attaque
from game.gabrimon.Gabrimon import Gabrimon

GABRIMON_PATH = "assets/lists/gabrimon/"
ATTAQUES_PATH = "assets/lists/attaques/"


class GabrimonService(Service):
    def init(self):
        self.gabrimons = {}
        self.attaques = {}

        print("Chargement des Attaques...")
        attaques_files = list(Path(self.engine.get_absolute_path(ATTAQUES_PATH)).glob("*.json"))
        for f in attaques_files:
            try:
                with open(f) as json_file:
                    data = json.load(json_file)
                    id = data["id"]
                    name = data["nom"]
                    type_action = data["type_action"]
                    valeur = data["valeur"]
                    self.attaques[id] = Attaque(name, valeur, type_action)
                    print("Attaque '" + id + "' charge")
            except Exception as e:
                print("[ERREUR] Chargement de", f.name, "|", e)

        print(len(self.attaques), "attaques chargees")

        print("Chargement des Gabrimons...")
        gabrimons_files = list(Path(self.engine.get_absolute_path(GABRIMON_PATH)).glob("*.json"))
        for f in gabrimons_files:
            with open(f) as json_file:
                data = json.load(json_file)
                id = data["id"]
                name = data["nom_affichage"]
                types = data["type"]
                pv_max = data["pv"]
                sprite_bank = data["sprite"]["id"]
                sprite_u = data["sprite"]["idle"]["u"]
                sprite_v = data["sprite"]["idle"]["v"]
                sprite_attack_u = data["sprite"]["attack"]["u"]
                sprite_attack_v = data["sprite"]["attack"]["v"]
                sprite_w = data["sprite"]["w"]
                sprite_h = data["sprite"]["h"]

                attaques = []
                for a_id in data["attaques"]:
                    if a_id in self.attaques:
                        attaques.append(self.attaques[a_id])
                    else:
                        print("[" + id + "] Attaque '" + a_id + "' introuvable")

                self.gabrimons[id] = Gabrimon(
                    nom=name,
                    pv_max=pv_max,
                    attaques=attaques,
                    type=types,
                    niveau=1,
                    sprite_bank=sprite_bank,
                    sprite_u_normal=sprite_u,
                    sprite_v_normal=sprite_v,
                    sprite_u_attaque=sprite_attack_u,
                    sprite_v_attaque=sprite_attack_v,
                    sprite_w=sprite_w,
                    sprite_h=sprite_h,
                )
                print("Gabrimon '" + id + "' charge")

        print(len(self.gabrimons), "gabrimons charges")

    def get_random_gabrimon(self):
        gab = self.gabrimons[random.choice(list(self.gabrimons.keys()))].copie()
        gab.set_niveau(random.randint(2, 99), full_heal=True)
        return gab

    def get_gabrimon(self, gabrimon_id, niveau=5):
        """
        Retourne une copie d'un gabrimon par id (ex: 'flamigi').
        """
        if gabrimon_id not in self.gabrimons:
            raise KeyError(f"Gabrimon introuvable: {gabrimon_id}")
        gab = self.gabrimons[gabrimon_id].copie()
        if niveau is not None:
            gab.set_niveau(niveau, full_heal=True)
        return gab

