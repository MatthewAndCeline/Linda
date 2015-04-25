#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Scrut Personnes Nul")

from Tkinter import *
import linda
import time
import random

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Scrut.Pers.Nul")
fenetre.geometry('150x50+1200+100')

# Données affichées variant avec le temps
info = StringVar()
Label(fenetre,textvariable=info).pack(padx=5,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj():
	fenetre.after(temps,maj)

def init():
	fenetre.after(temps,maj)

init()

# On lance la boucle d'exécution
fenetre.mainloop()

