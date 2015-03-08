#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK logique H2O Critique ")

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
fenetre.title("Logique H2O Critique")
fenetre.geometry('150x50+600+400')

# Données affichées variant avec le temps
message = StringVar()
Label(fenetre,textvariable=message).pack(padx=10,pady=10)

def maj():
	message.set("en attente niveau Critique")
	fenetre.after(temps,maj)
maj()

# On lance la boucle d'exécution
fenetre.mainloop()

