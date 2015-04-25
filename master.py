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
ts._out(("etat_lampe","desactivé"))
ts._out(("etat_alarme","desactivé"))
ts._out(("autorisation_ascenseur","interdit"))
ts._out(("action_ascenseur","attend"))
ts._out(("occupation_ascenseur","vide"))
ts._out(("detection_H2O_haut",))
ts._out(("detection_heure_pleine",))
ts._out(("heure",0))

#Configuration du système
ts._out(("Seuil_CH4_HP",7.0))
ts._out(("Seuil_CO_HP",7.0))
ts._out(("Seuil_CH4_HC",9.0))
ts._out(("Seuil_CO_HC",9.0))
ts._out(("Seuil_CH4",9.0))
ts._out(("Seuil_CO",9.0))
ts._out(("Seuil_H2O_haut_HP",7.0))
ts._out(("Seuil_H2O_haut_HC",9.0))
ts._out(("Seuil_H2O_haut",9.0))
ts._out(("Seuil_H2O_bas",3.0))
ts._out(("Duree_une_heure",3000))
ts._out(("Temps_Rafraichissement",300))

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Master")
fenetre.geometry('150x50+0+0')
Label(fenetre,text="Système en route").pack(padx=5,pady=5)

# On lance la boucle d'exécution
fenetre.mainloop()
