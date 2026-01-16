# Pyxel Studio

import pyxel
from Attaque import Attaque
from Gabrimon import Gabrimon
from Combat import Combat
from Joueur import Joueur

def update():
    combat.update()

def draw():
    combat.draw()

pyxel.init(160, 120, title="Pokemon Combat")


repos = Attaque ("Repos" , 0, 5)

etincelle = Attaque("etincelle", 20, 0)
griffes_chaudes = Attaque("Griffes Chaudes", 30,0)
souffle_brulant = Attaque("Souffle Brulant", 40,0)

#Mouskin
fouet_liane= Attaque("Fouet Liane", 20,0)
pollen_soin = Attaque("Pollen Soin", 0, 20)
charge_verte = Attaque("Charge Verte", 35,0)

#aquapti
jet_deau= Attaque("Jet d'eau", 20,0)
vague_rapide = Attaque("Vague Rapide", 35,0)
bulle_percutante = Attaque("Bulle Percutante", 30, 0)

#voltch
etincoup = Attaque("Etincoup", 25,0)
eclair = Attaque("Eclair", 40,0)
vitesse_foudre = Attaque("Vitesse foudre", 30,0)

#Roclin
jet_de_pierre = Attaque("Jet de Pierre", 30,0)
ecrasement =Attaque("Ecrasement", 45,0)
mur_mineral = Attaque("Mur mineral", 0,15)

#Noctyra
regard_noir = Attaque("Regard Noir", 20,0)
ombre_vive = Attaque("Ombre vive", 35,0)
morsure_nuit = Attaque("Morsure nuit", 40,0)

#Givrin
souffle_froid = Attaque("Soufle froid", 25,0)
pic_de_glace =Attaque("Pic de glace", 35,0)
gel_total =Attaque("Gel total", 45,0)

#aerion
tornade = Attaque("Tornade", 30,0)
coup_daile = Attaque("Coup d'aile", 25,0)
rafale =Attaque("Rafale", 40,0)

#psymio
choc_mental = Attaque("Choc mental", 30,0)
onde_psy =Attaque("Onde psy", 40,0)
soin_mental = Attaque("Soin mental", 0,25)

#Drakid
griffe_dragon = Attaque("Griffe dragon", 35,0)
rugissement = Attaque("Rugissement", 20,0)
flamme_draco = Attaque("Flamme draco", 50,0)

flamigi = Gabrimon("Flamigi", 60, [etincelle,griffes_chaudes,souffle_brulant, repos])
mouskin = Gabrimon("Mouskin", 70, [fouet_liane,pollen_soin,jet_deau, repos])
aquapti = Gabrimon("Aquapti", 65, [jet_deau,vague_rapide,bulle_percutante, repos])
voltchu = Gabrimon("Voltchu", 55 , [etincoup, eclair, vitesse_foudre, repos])
rocling = Gabrimon("Rocling", 90, [jet_de_pierre, ecrasement, mur_mineral, repos])
noctyra = Gabrimon("Noctyra" , 60, [regard_noir, ombre_vive, morsure_nuit,repos])
givrin = Gabrimon("Givrin", 65, [souffle_brulant, pic_de_glace, gel_total , repos])
aerion = Gabrimon("Aerion", 60, [tornade, coup_daile, rafale, repos])
psymio = Gabrimon("Psymio", 70 , [choc_mental, onde_psy, soin_mental,repos])
drakid = Gabrimon("Drakid", 85 , [griffe_dragon, rugissement, flamme_draco, repos])

joueur = Joueur("Sacha", [flamigi, mouskin, voltchu, aerion, rocling, givrin])

combat = Combat(joueur,aquapti)

pyxel.run(update, draw)