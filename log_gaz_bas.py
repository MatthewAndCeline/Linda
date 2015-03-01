#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK logique gaz bas ")

from Tkinter import *
import linda
import time

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Logique Gaz Bas")
fenetre.geometry('600x100+0+400')

message = StringVar()
Label(fenetre,textvariable=message).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj():
	message.set("En attente gaz bas")
	ts._in(("Gaz_bas_detecté",))
	etat_pompe = ts._rd(("etat_pompe",str))[1]
	if (etat_pompe == "desactivé"):
		message.set("activation pompe & detection_H2O_bas")
		ts._out(("Pompe_En_Route",))
	else:
		message.set("demarrage detection_H2O_bas")
	ts._out(("detection_H2O_bas",)) 
	fenetre.after(1000,maj)
	
maj()

# On lance la boucle d'exécution
fenetre.mainloop()

