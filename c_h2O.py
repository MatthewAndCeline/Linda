#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Capteur H2O")

from Tkinter import *
import linda
import time

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Initialisation du système de génération de valeurs "aléatoires"
t = [0.0, 2.3, 4.7, 5.3, 7.2, 8.1, 9.6, 10.0]
k = 0

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Capteur H2O")
fenetre.geometry('150x50+400+100')

# Données affichées variant avec le temps
info = StringVar()
Label(fenetre,textvariable=info).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj(t,k):
	if (k == 7):
		k = 0
	else:
		k += 1
	info.set(t[k])
	ts._in(("Niveau_H2O",float))
	ts._out(("Niveau_H2O",t[k]))
	fenetre.after(1000,maj,t,k)
maj(t,0)

# On lance la boucle d'exécution
fenetre.mainloop()

