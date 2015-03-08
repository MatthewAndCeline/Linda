#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK ascenseur ")

from Tkinter import *
import time
import linda

linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Ascenseur")
fenetre.geometry('200x50+900+0')

# Données affichées variant avec le temps
autorisation = StringVar()
Label(fenetre,textvariable=autorisation).pack(padx=10,pady=5)
action = StringVar()
Label(fenetre,textvariable=action).pack(padx=10,pady=5)
occupation = StringVar()
Label(fenetre,textvariable=occupation).pack(padx=10,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj():
	etat_autorisation = ts._rd(("autorisation_ascenseur",str))[1]
	autorisation.set(etat_autorisation)
	etat_action = ts._rd(("action_ascenseur",str))[1]
	action.set(etat_action)
	etat_occupation = ts._rd(("occupation_ascenseur",str))[1]
	occupation.set(etat_occupation)
	if(etat_autorisation == "autorisé"):
		ts._in(("Interdire_Ascenseur",))
		etat_autorisation = "interdit"
		autorisation.set(etat_autorisation)
		ts._in(("autorisation_ascenseur","autorisé"))
		ts._out(("autorisation_ascenseur","interdit"))
	else:
		ts._in(("Autoriser_Ascenseur",))
		etat_autorisation = "autorisé"
		autorisation.set(etat_autorisation)
		ts._in(("autorisation_ascenseur","interdit"))
		ts._out(("autorisation_ascenseur","autorisé"))
	fenetre.after(temps,maj)
maj()

# On lance la boucle d'exécution
fenetre.mainloop()


