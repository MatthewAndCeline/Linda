#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK scrutateur H2O bas ")

from Tkinter import *
import linda
import time

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
seuil = 4.0

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Scrutateur H2O Bas")
fenetre.geometry('200x100+250+200')

# Données affichées variant avec le temps
jedetecte = StringVar()
Label(fenetre,textvariable=jedetecte).pack(padx=10,pady=10)

valeur = StringVar()
Label(fenetre,textvariable=valeur).pack(padx=10,pady=20)


# Fonction de mise à jour à réaliser en permanence
def maj():
	print("maj H2O bas")
	jedetecte.set("Je ne dois pas détecter")
	ts._rd(("detection_H2O_bas",))
	jedetecte.set("Je dois detecter")
	valeur_H2O = ts._rd(("Niveau_H2O",float))[1]
	valeur.set(valeur_H2O)
	if (valeur_H2O < seuil):
		ts._out(("H2O_bas_detecté",))
		ts._in(("detection_H2O_bas",))
	fenetre.after(1000,maj)

maj()

# On lance la boucle d'exécution
fenetre.mainloop()
