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
fenetre.geometry('200x100+750+500')

# Données affichées variant avec le temps
message = StringVar()
Label(fenetre,textvariable=message).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj():
	print("maj Log Gaz bas")
	ts._in(("Gaz_bas_detecté",))
	message.set("Gaz Bas détécté, activation de la pompe")
	ts._out(("Pompe_En_Route",))
	#Force H2O bas détécté
	ts._out(("detection_H2O_bas",)) 
	fenetre.after(1000,maj)
	
maj()

# On lance la boucle d'exécution
fenetre.mainloop()

