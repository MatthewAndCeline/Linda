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
ts._out(("Niveau_H2O",7.0))
ts._out(("Niveau_CO",0.0))
ts._out(("etat_pompe","desactivé"))
ts._out(("etat_ventilateur","desactivé"))
ts._out(("detection_H2O_haut",))

#Configuration du système
ts._out(("Seuil_CH4",7.0))
ts._out(("Seuil_CO",7.0))
ts._out(("Seuil_H2O_haut",8.0))
ts._out(("Seuil_H2O_bas",3.0))
ts._out(("Temps_Rafraichissement",5000))

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Master")
fenetre.geometry('200x50+0+0')
Label(fenetre,text="Système en route").pack(padx=10,pady=10)

# On lance la boucle d'exécution
fenetre.mainloop()
