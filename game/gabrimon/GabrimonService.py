from pathlib import Path
import json
from engine.services.Service import Service
from game.gabrimon.Attaque import Attaque
from game.gabrimon.Gabrimon import Gabrimon

GABRIMON_PATH = "assets/lists/gabrimon/"
ATTAQUES_PATH = "assets/lists/attaques/"

class GabrimonService(Service):

    def init(self):

        gabrimons = {}
        attaques = {}

        print("Chargement des Attaques...")
        attaques_files = list(Path(self.engine.get_absolute_path(ATTAQUES_PATH)).glob("*.json"))
        for f in attaques_files:
            with open(f) as json_file:
                data = json.load(json_file)
                id = data["id"]
                name = data["name"]
                type = data["type"]
                damage = data["damage"]
                attaques[id] = Attaque(name,damage,type)
                print("Attaque '" + id + "' chargé")
        print(len(attaques), "attaques chargés")

        print("Chargement des Gabrimons...")
        gabrimons_files = list(Path(self.engine.get_absolute_path(GABRIMON_PATH)).glob("*.json"))
        for f in gabrimons_files:
            with open(f) as json_file:
                data = json.load(json_file)
                id = data["id"]
                name = data["nom_affichage"]
                # TODO: Type, min_level, max_level
                pv_max = data["pv"]
                atta = []
                for i in data["attaques"]:
                    if i in attaques:
                        atta.append(attaques[i])
                    else:
                        print("[" + id + "] Attaque '" + i + "' introuvable")
                gabrimons[id] = Gabrimon(name,pv_max,atta)
                print("Gabrimon '" + id + "' chargé")
            print(len(gabrimons), "gabrimons chargés")












