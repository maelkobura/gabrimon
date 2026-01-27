# Zone

## Comment placer une zone ?

Pour placer une zone, il faut utiliser la fonction add_child du service ZoneService.

`engine.get_service("ZoneService").add_child(zone)`

> Etant donnée que le service Zone doit être initialisé au moment du placement, le mieux reste d'inscrire la zone dans la méthode init() du ZoneService directement.

### La Classe Zone

Voici les instructions pour initialiser la classe Zone.

`Zone(zone_service, x, y, w, h, ZoneEvent(),world)`

- `zone_service`: Instance de la zone_service, obligatoire
- `x`: Coordonnée x sur la map (voir Outil.md pour plus d'infos)
- `y`: Coordonnée y sur la map (voir Outil.md pour plus d'infos)
- `w`: Largeur de la zone, en pixels
- `h`: Hauteur de la zone, en pixels
- `ZoneEvent()`: Classe permettant de réagir en fonction de la présence du joueur dans la zone
- `world`: Identifiant du monde dans lequel se trouve la zone (typiquement 0 pour la map principale et 1 pour les intérieurs)

> Pour trouver la hauteur et la largeur de la zone, il faut soustraire la position de fin de zone à la position de début. Par exemple pour une zonne commençant en (150, 300) et finissant en (250, 400), il faut faire
> 
> **w=250-150=50** et **h=400-300=100**.

### La Classe ZoneEvent

ClasseEvent permet d'exécuter des actions en fonction de l'état de la zone.
Voici un exemple d'implémentation:

```python
class MesEvents(ZoneEvent):
    def __init__(self, parametres):
        super().__init__()
        self.parametres = parametres
        
    def on_enter(self, personnage):
        print("Un personnage entre dans la zone")
        
    def on_exit(self, personnage):
        print("Un personnage sort de la zone")
        
    def on_update(self, personnage):
        print("Un personnage est dans la zone")
```

