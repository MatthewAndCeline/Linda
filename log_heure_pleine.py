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
fenetre.title("Log.H.P.")
fenetre.geometry('350x50+0+600')

message = StringVar()
Label(fenetre,textvariable=message).pack(padx=5,pady=5)

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
	#Faire rentrer les travailleurs
	heure = ts._rd(("heure",int))[1]
	if ((heure >= 5) and (heure <= 13)):
		ts._out(("Equipe_Entrer",1))
		ts._out(("Equipe_Entrer",1))
		ts._out(("Equipe_Entrer",1))
		ts._out(("Equipe_Entrer",1))
	else:
		ts._out(("Equipe_Entrer",2))
		ts._out(("Equipe_Entrer",2))
		ts._out(("Equipe_Entrer",2))
		ts._out(("Equipe_Entrer",2))
	#
	message.set("detection_heure_creuse")
	ts._out(("detection_heure_creuse",)) 
	fenetre.after(temps,maj)
	
def init():
	message.set("En attente heure pleine")
	fenetre.after(temps,maj)

init()

# On lance la boucle d'exécution
fenetre.mainloop()
