from engine.Engine import Engine
from game.GabrimonCore import GabrimoneCore

Engine("Gabrimon",
       gamepath="../example/",
       splash_screen="assets/splash.png",
       game_class=GabrimoneCore)