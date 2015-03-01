#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Capteur H2O")

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
fenetre.title("Capteur H2O")
fenetre.geometry('200x50+500+100')

# Données affichées variant avec le temps
info = StringVar()
Label(fenetre,textvariable=info).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj(k):
	pompe_en_route = ts._rd(("etat_pompe",str))[1]
	randNum = random.random()
	randNum = round(randNum,2)
	if (pompe_en_route == "desactivé"):
		k += randNum
	else:
		k -= randNum
	k = round(k,4)
	info.set(k)
	ts._in(("Niveau_H2O",float))
	ts._out(("Niveau_H2O",k))
	fenetre.after(temps,maj,k)
maj(7.0)

# On lance la boucle d'exécution
fenetre.mainloop()

