#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK scrutateur heure pleine ")

from Tkinter import *
import linda
import time

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Scrutateur HP")
fenetre.geometry('200x100+900+200')

# Données affichées variant avec le temps
str_heure = StringVar()
Label(fenetre,textvariable=str_heure).pack(padx=10,pady=20)

# Fonction de mise à jour à réaliser en permanence
def maj():
	ts._rd(("detection_heure_pleine",))
	valeur_heure = ts._rd(("heure",int))[1]
	str_heure.set(valeur_heure)
	if ((valeur_heure == 5) or (valeur_heure == 15)):
		ts._in(("detection_heure_pleine",))
		ts._out(("Heure_pleine_detecté",))
	fenetre.after(temps,maj)

maj()

# On lance la boucle d'exécution
fenetre.mainloop()

