from engine.Engine import Engine
from game.GabrimonCore import GabrimoneCore

Engine("Gabrimon",
       gamepath="../game/",
       splash_screen="assets/splash.png",
       game_class=GabrimoneCore)

