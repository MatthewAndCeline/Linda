#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Capteur Demandes Entrées ")

from Tkinter import *
import time
import linda
import random

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace train", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Capt. Demandes Entrées")
fenetre.geometry('150x50+500+200')
Label(fenetre,text="C.D.E").pack(padx=5,pady=5)
info = StringVar()
Label(fenetre,textvariable=info).pack(padx=5,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj():
	ts._in(("demande_entree",))
	val_nb_demandes_entrees = ts._in(("nombre_demandes_entrees",int))[1]
	val_nb_demandes_entrees += 1
	ts._out(("nombre_demandes_entrees",val_nb_demandes_entrees))
	info.set("nombre_demandes_entrees : " + str(val_nb_demandes_sorties))
	fenetre.after(temps,maj)

def init():
	info.set("entrées")
	fenetre.after(temps,maj)

init()

# On lance la boucle d'exécution
fenetre.mainloop()
