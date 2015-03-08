#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK logique heure pleine ")

from Tkinter import *
import linda
import time

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Configuration
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Logique Heure Pleine")
fenetre.geometry('600x100+0+400')

message = StringVar()
Label(fenetre,textvariable=message).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj():
	message.set("En attente heure pleine")
	ts._in(("Heure_pleine_detecté",))
	#Modifier les seuils
	nouveau_seuil_H2O = ts._rd(("Seuil_H2O_haut_HP",float))[1]
	ts._in(("Seuil_H2O_haut",float))
	ts._out(("Seuil_H2O_haut",nouveau_seuil_H2O))
	#
	#Allumer les lampes
	ts._out(("Lampe_En_Route",))
	#
	message.set("detection_heure_creuse")
	ts._out(("detection_heure_creuse",)) 
	fenetre.after(temps,maj)
	
maj()

# On lance la boucle d'exécution
fenetre.mainloop()

