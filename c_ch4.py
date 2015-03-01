#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Capteur CH4")

from Tkinter import *
import linda
import time
import random

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Initialisation du système de génération de valeurs "aléatoires"
#t = [0.0, 2.3, 4.7, 5.3, 7.2, 8.1, 9.6, 10.0]
#k = 0

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Capteur CH4")
fenetre.geometry('200x50+250+100')

# Données affichées variant avec le temps
info = StringVar()
Label(fenetre,textvariable=info).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj(k):
	pompe_en_route = ts._rd(("etat_pompe",str))[1]
	ventilo_en_route = ts._rd(("etat_ventilateur",str))[1]
	randNum = random.random()
	if (ventilo_en_route == "desactivé"):
		if (pompe_en_route == "desactivé"):
			k += 0.1*randNum
		else:
			k += randNum
	else:
		if (pompe_en_route == "desactivé"):
			k -= randNum
		else:
			k -= 0.3*randNum
	k = round(k,4)
	info.set(k)
	ts._in(("Niveau_CH4",float))
	ts._out(("Niveau_CH4",k))
	fenetre.after(1000,maj,k)
maj(0.0)


# On lance la boucle d'exécution
fenetre.mainloop()

