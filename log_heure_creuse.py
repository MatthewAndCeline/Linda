#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK logique heure creuse ")

from Tkinter import *
import linda
import time
import threading

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Configuration
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Logique Heure Creuse")
fenetre.geometry('150x50+200+300')

message = StringVar()
Label(fenetre,textvariable=message).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj():
	message.set("En attente heure creuse")
	ts._in(("Heure_creuse_detecté",))
	#Modifier les seuils
	nouveau_seuil_H2O = ts._rd(("Seuil_H2O_haut_HC",float))[1]
	ts._in(("Seuil_H2O_haut",float))
	ts._out(("Seuil_H2O_haut",nouveau_seuil_H2O))
	#
	#Eteindre les lampes
	ts._out(("Lampe_Arreté",))
	#
	#Couper l'ascenseur
	ts._out(("Interdire_Ascenseur",))
	#
	message.set("detection_heure_pleine")
	ts._out(("detection_heure_pleine",)) 
	fenetre.after(temps,maj)
	
T = threading.Thread(None,maj)
T.start()

# On lance la boucle d'exécution
fenetre.mainloop()

