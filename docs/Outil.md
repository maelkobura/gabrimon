# Outil de placement

## Comment activer l'outil ?

Par défaut, l'outil est désactivé, pour l'activer il faut mettre la valeur ENABLE_DEBUG sur True dans la classe Joueur

```python
CLICK_DEBUG = True
```

## Comment utiliser l'outil ?

Après avoir activé l'outil, un curseur apparaîtra et va permettre d'obtenir les coordonnées du clic.

Le click gauche permet de récupérer les coordonnées dans le monde, pour placer des zones, des intérieurs, des points de téléportations, etc...

Le click droit permet lui de récupérer les coordonnées brut de l'écran afin de placer des interfaces utilisateurs.

### Click gauche
``Location (World Space) : x=994.0, y=379.0``
### Click droit
``Location (UI Space) : x=58, y=43``
