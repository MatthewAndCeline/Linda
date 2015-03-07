#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK master ")
from Tkinter import *
import time
import linda

#Initialisation de Linda
linda.connect()
ts = linda.TupleSpace()
linda.universe._out(("TupleSpace drainage", ts))

#Initialisation de l'état du système
ts._out(("Niveau_CH4",0.0))
ts._out(("Niveau_H2O",8.0))
ts._out(("Niveau_CO",0.0))
ts._out(("Presence_Fumee",False))
ts._out(("etat_pompe","desactivé"))
ts._out(("etat_ventilateur","desactivé"))
ts._out(("detection_H2O_haut",))
ts._out(("heure",0))

#Configuration du système
ts._out(("Seuil_CH4_Critique",15.0))
ts._out(("Seuil_CO_Critique",15.0))
ts._out(("Seuil_H2O_Critique",15.0))
ts._out(("Seuil_CH4_HP",7.0))
ts._out(("Seuil_CO_HP",7.0))
ts._out(("Seuil_CH4_HC",9.0))
ts._out(("Seuil_CO_HC",9.0))
ts._out(("Seuil_H2O_Critique",15.0))
ts._out(("Seuil_H2O_haut_HP",7.0))
ts._out(("Seuil_H2O_haut_HC",9.0))
ts._out(("Seuil_H2O_bas",3.0))
ts._out(("Duree_une_heure",10000))
ts._out(("Temps_Rafraichissement",1000))
ts._out(("Proba_Fumer",0.01))
ts._out(("Proba_Action_Manuelle",0.01))


# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Master")
fenetre.geometry('200x50+0+0')
Label(fenetre,text="Système en route").pack(padx=10,pady=10)

# On lance la boucle d'exécution
fenetre.mainloop()
