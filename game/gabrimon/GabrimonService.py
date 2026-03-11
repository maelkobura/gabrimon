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
                    type = data["type_action"]
                    damage = data["valeur"]
                    self.attaques[id] = Attaque(name, damage, type)
                    print("Attaque '" + id + "' chargé")
            except Exception as e:
                print("[ERREUR] Chargement de",f.name,"|",e)

        print(len(self.attaques), "attaques chargés")

        print("Chargement des Gabrimons...")
        gabrimons_files = list(Path(self.engine.get_absolute_path(GABRIMON_PATH)).glob("*.json"))
        for f in gabrimons_files:
            with open(f) as json_file:
                data = json.load(json_file)
                id = data["id"]
                name = data["nom_affichage"]
                # TODO: min_level, max_level
                types = data["type"]
                pv_max = data["pv"]
                image_bank = data["sprite"]["id"]
                image_u = data["sprite"]["idle"]["u"]
                image_v = data["sprite"]["idle"]["v"]
                image_attack_u = data["sprite"]["attack"]["u"]
                image_attack_v = data["sprite"]["attack"]["v"]
                image_w = data["sprite"]["w"]
                image_h = data["sprite"]["h"]
                atta = []
                for i in data["attaques"]:
                    if i in self.attaques:
                        atta.append(self.attaques[i])
                    else:
                        print("[" + id + "] Attaque '" + i + "' introuvable")
                self.gabrimons[id] = Gabrimon(name,pv_max,atta,types,image_bank,image_u,image_v,image_attack_u,image_attack_v,image_w,image_h)
                print("Gabrimon '" + id + "' chargé")
        print(len(self.gabrimons), "gabrimons chargés")

    def get_random_gabrimon(self):
        gab = self.gabrimons[random.choice(list(self.gabrimons.keys()))].copie()
        gab.niveau = random.randint(2,99)
        return gab

    def get_gabrimon(self, gabrimon_id, niveau=5):
        """
        Retourne une copie d'un gabrimon par id (ex: 'flamigi').
        """
        if gabrimon_id not in self.gabrimons:
            raise KeyError(f"Gabrimon introuvable: {gabrimon_id}")
        gab = self.gabrimons[gabrimon_id].copie()
        if niveau is not None:
            gab.niveau = niveau
        return gab












