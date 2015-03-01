#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK scrutateur H2O haut ")

from Tkinter import *
import linda
import time

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
seuil = 8.0

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Scrutateur H2O Haut")
fenetre.geometry('150x100+0+200')

# Données affichées variant avec le temps
jedetecte = StringVar()
Label(fenetre,textvariable=jedetecte).pack(padx=10,pady=10)

valeur = StringVar()
Label(fenetre,textvariable=valeur).pack(padx=10,pady=20)


# Fonction de mise à jour à réaliser en permanence
def maj():
	print("maj H2O haut")
	jedetecte.set("Je ne dois pas détecter")
	ts._rd(("detection_H2O_haut",))
	jedetecte.set("Je dois detecter")
	valeur_H2O = ts._rd(("Niveau_H2O",float))[1]
	valeur.set(valeur_H2O)
	if (valeur_H2O > seuil):
		ts._out(("H2O_haut_detecté",))
		ts._in(("detection_H2O_haut",))
		ts._out(("detection_H2O_bas",))
	fenetre.after(1000,maj)

maj()

# On lance la boucle d'exécution
fenetre.mainloop()
