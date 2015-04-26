#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Capteur Personnes")

from Tkinter import *
import linda
import time
import random

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Capt.Pers")
fenetre.geometry('350x50+1000+0')

# Données affichées variant avec le temps
info = StringVar()
Label(fenetre,textvariable=info).pack(padx=5,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj(nbPersonnes):
	action = ts._in(("Entree/Sortie",str))[1]
	if (action == "monter"):
		nbPersonnes = nbPersonnes - 1
	else:
		nbPersonnes = nbPersonnes + 1
	info.set(nbPersonnes)
	fenetre.after(temps,maj,nbPersonnes)

def init():
	fenetre.after(temps,maj,0)

init()

# On lance la boucle d'exécution
fenetre.mainloop()

