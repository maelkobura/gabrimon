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


def creer_gabrimon(nom,pv, attaques, type,u, v):
    return Gabrimon(
        nom=nom,
        pv_max=pv,
        attaques=attaques,
        type=type,
        sprite_bank=0,
        sprite_u=u,
        sprite_v=v,
        sprite_w=31,
        sprite_h=31
    )


repos = Attaque ("Repos" , 5, "soin")

etincelle = Attaque("etincelle", 20, "degats")
griffes_chaudes = Attaque("Griffes Chaudes", 30,"degats")
souffle_brulant = Attaque("Souffle Brulant", 40,"degats")

#Mouskin
fouet_liane= Attaque("Fouet Liane", 20,"degats")
pollen_soin = Attaque("Pollen Soin", 20, "soin")
charge_verte = Attaque("Charge Verte", 35,"degats")

#aquapti
jet_deau= Attaque("Jet d'eau", 20,"degats")
vague_rapide = Attaque("Vague Rapide", 35,"degats")
bulle_percutante = Attaque("Bulle Percutante", 30, "degats")

#voltch
etincoup = Attaque("Etincoup", 25,"degats")
eclair = Attaque("Eclair", 40,"degats")
vitesse_foudre = Attaque("Vitesse foudre", 30,"degats")

#Roclin
jet_de_pierre = Attaque("Jet de Pierre", 30,"degats")
ecrasement =Attaque("Ecrasement", 45,"degats")
mur_mineral = Attaque("Mur mineral", 15,"soin")

#Noctyra
regard_noir = Attaque("Regard Noir", 20,"degats")
police = Attaque("Police", 35,"degats")
ombre_vive = Attaque("Ombre vive", 35,"degats")
morsure_nuit = Attaque("Morsure nuit", 40,"degats")

#Givrin
souffle_froid = Attaque("Soufle froid", 25,"degats")
pic_de_glace =Attaque("Pic de glace", 35,"degats")
gel_total =Attaque("Gel total", 45,"degats")

#aerion
tornade = Attaque("Tornade", 30,"degats")
coup_daile = Attaque("Coup d'aile", 25,"degats")
rafale =Attaque("Rafale", 40,"degats")

#psymio
choc_mental = Attaque("Choc mental", 30,"degats")
onde_psy =Attaque("Onde psy", 40,"degats")
soin_mental = Attaque("Soin mental", 25,"soin")

#Drakid
griffe_dragon = Attaque("Griffe dragon", 35,"degats")
rugissement = Attaque("Rugissement", 20,"degats")
flamme_draco = Attaque("Flamme draco", 50,"degats")

flamigi = creer_gabrimon("Flamigi", 60,[etincelle,griffes_chaudes,souffle_brulant, repos],"Feu", 144 , 0)
aquapti = creer_gabrimon("Aquapti",65, [jet_deau,vague_rapide,bulle_percutante, repos],"Eau", 208, 0)
mouskin = creer_gabrimon("Mouskin", 70,[fouet_liane,pollen_soin,jet_deau, repos],"Plante", 176 , 0 )
rocling = creer_gabrimon("Rocling", 90,[jet_de_pierre, ecrasement, mur_mineral, repos],"Roche",208, 64)
#flamigi = Gabrimon("Flamigi", 60, [etincelle,griffes_chaudes,souffle_brulant, repos])
#mouskin = Gabrimon("Mouskin", 70, [fouet_liane,pollen_soin,jet_deau, repos])
#aquapti = Gabrimon("Aquapti", 65, [jet_deau,vague_rapide,bulle_percutante, repos])
#voltchu = Gabrimon("Voltchu", 55 , [etincoup, eclair, vitesse_foudre, repos])
#rocling = Gabrimon("Rocling", 90, [jet_de_pierre, ecrasement, mur_mineral, repos])
#noctyra = Gabrimon("Noctyra" , 60, [regard_noir, ombre_vive, morsure_nuit,repos])
#givrin = Gabrimon("Givrin", 65, [souffle_brulant, pic_de_glace, gel_total , repos])
#aerion = Gabrimon("Aerion", 60, [tornade, coup_daile, rafale, repos])
#psymio = Gabrimon("Psymio", 70 , [choc_mental, onde_psy, soin_mental,repos])
#drakid = Gabrimon("Drakid", 85 , [griffe_dragon, rugissement, flamme_draco, repos])

gabriel = Joueur("Gabriel", [rocling,flamigi,aquapti, mouskin])
ennemi = aquapti.copie()
combat = Combat(gabriel,ennemi)
pyxel.run(update, draw)