#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Horloge")

from Tkinter import *
import linda
import time

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]
duree_une_heure = ts._rd(("Duree_une_heure",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Horloge")
fenetre.geometry('150x50+200+0')

# Données affichées variant avec le temps
info = StringVar()
Label(fenetre,textvariable=info).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj(k,m):
	ts._in(("heure",int))
	ts._out(("heure",k))
	info.set(str(k) + " h " + str(m))
	if (m != 50):
		m += 10
	else:
		if (k != 23):
			k += 1
		else:
			k = 0
		m = 0
	fenetre.after(duree_une_heure / 6,maj,k,m)

def init():
	maj(0,0)

init()

# On lance la boucle d'exécution
fenetre.mainloop()
