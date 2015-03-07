#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK logique gaz haut ")

from Tkinter import *
import linda
import time

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Configuration
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Logique Gaz Haut")
fenetre.geometry('600x100+700+400')

# Données affichées variant avec le temps
message = StringVar()
Label(fenetre,textvariable=message).pack(padx=10,pady=10)

def maj():
	message.set("attente niveau haut")
	ts._in(("Gaz_haut_detecté",))
	message.set("démarrage ventilo et detection_gaz_bas")
	ts._out(("Ordre_Ventilateur","En_Route",))
	fenetre.after(temps,maj)
maj()

# On lance la boucle d'exécution
fenetre.mainloop()

