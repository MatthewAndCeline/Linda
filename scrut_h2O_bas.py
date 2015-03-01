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
valeur = StringVar()
Label(fenetre,textvariable=valeur).pack(padx=10,pady=20)


# Fonction de mise à jour à réaliser en permanence
def maj():
	ts._rd(("detection_H2O_bas",))
	valeur_H2O = ts._rd(("Niveau_H2O",float))[1]
	valeur.set(valeur_H2O)
	if (valeur_H2O < seuil):
		ts._in(("detection_H2O_bas",))
		ts._out(("H2O_bas_detecté",))
	fenetre.after(1000,maj)

maj()

# On lance la boucle d'exécution
fenetre.mainloop()
