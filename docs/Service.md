# Services

## C'est quoi un service ?

Un service est un ensemble de fonctionnalité permettant de remplir un besoin précis du projet. Par exemple, **UIService** va gérer toutes les systèmes relatifs à l'interface utilisateur.

### Comment récupérer un service ?

Un service peut se récupérer dans l'instance de engine

```python
Engine.INSTANCE.get_service("nom_du_service")
```

## Création d'un service

Un service se crée depuis la classe **Service**

```python
class MonService(Service):
    def init(self):
        pass
    def start(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass
```

- ``init()``: Cette méthode est appelé juste après l'inscription du service
- ``start()``: Cette méthode est appelé quand le jeu est lancé et que tous les services ont été initialisé. Recommandé pour les interactions entre les services
- ``draw() & update()``: Ces méthodes sont des extensions directes de update() et draw() de pyxel

### Etats de jeu

Un service peut enregistrer ou récupérer un état de jeu. Ces états sont des variables globales qui donne des informations sur le jeu.

Exemple:
```python
self.get_state("player_x")
self.set_state("xp", 100)
```

### Inscription d'un service

L'inscription d'un service se fait dans le fichier ``GabrimonCore.py``. Sans cette étape, le service ne sera jamais initialisé par le moteur

```python
Engine.INSTANCE.register_service(MonService())
```

## Host Services

Les services hôtes sont des services spéciaux qui peuvent accueillir des entités. Ces entités sont des extensions de services qui représentent un objet réplicable sur le jeu (exemple: le service PersonnageService a comme entité les personnages)

```python
class MonServiceHote(HostService):
    def init(self):
        self.add_child(MonEntity(self))
    def start(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass
```

### Les entités

```python
class MonEntity(Entity):
    def __init__(self, service):
        super().__init__(service)
    def update(self):
        pass
    def draw(self):
        pass
```