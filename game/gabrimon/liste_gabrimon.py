# Pyxel Studio

import pyxel

from game.gabrimon.Attaque import Attaque
from game.gabrimon.Combat import Combat
from game.gabrimon.Gabrimon import Gabrimon
from game.gabrimon.Joueur import Joueur


def update():
    combat.update()

def draw():
    combat.draw()





def creer_gabrimon(nom,pv, attaques, type,u_normal, v_normal, u_attaque, v_attaque):
    return Gabrimon(
        nom=nom,
        pv_max=pv,
        attaques=attaques,
        type=type,
        sprite_u_normal=u_normal,
        sprite_v_normal=v_normal,
        sprite_u_attaque= u_attaque,
        sprite_v_attaque= v_attaque,
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

flamigi = creer_gabrimon("Flamigi", 60,[etincelle,griffes_chaudes,souffle_brulant],"Feu", 144 , 0 ,144, 32)
aquapti = creer_gabrimon("Aquapti",65, [jet_deau,vague_rapide,bulle_percutante],"Eau", 208, 0,208 , 32)
mouskin = creer_gabrimon("Mouskin", 70,[fouet_liane,pollen_soin,charge_verte],"Plante", 176 , 0, 176 , 32)
rocling = creer_gabrimon("Rocling", 90,[jet_de_pierre, ecrasement, mur_mineral],"Roche",208, 64,208 , 96)
#flamigi = Gabrimon("Flamigi", 60, [etincelle,griffes_chaudes,souffle_brulant]
#mouskin = Gabrimon("Mouskin", 70, [fouet_liane,pollen_soin,jet_deau])
#aquapti = Gabrimon("Aquapti", 65, [jet_deau,vague_rapide,bulle_percutante])
#voltchu = Gabrimon("Voltchu", 55 , [etincoup, eclair, vitesse_foudre])
#rocling = Gabrimon("Rocling", 90, [jet_de_pierre, ecrasement, mur_mineral])
#noctyra = Gabrimon("Noctyra" , 60, [regard_noir, ombre_vive, morsure_nuit])
#givrin = Gabrimon("Givrin", 65, [souffle_brulant, pic_de_glace, gel_total ])
#aerion = Gabrimon("Aerion", 60, [tornade, coup_daile, rafale])
#psymio = Gabrimon("Psymio", 70 , [choc_mental, onde_psy, soin_mental])
#drakid = Gabrimon("Drakid", 85 , [griffe_dragon, rugissement, flamme_draco])
liste_gabrimon = [flamigi,aquapti,mouskin,rocling]
gabriel = Joueur("Gabriel", [rocling,flamigi,aquapti, mouskin])
#ennemi = flamigi.copie()
#combat = Combat(gabriel,ennemi)
#pyxel.run(update, draw)