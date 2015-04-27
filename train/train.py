#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK train ")

from Tkinter import *
import time
import linda
import random
import sys

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace train", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Train")

fenetre.geometry('150x50+200+' + str(sys.argv[1]))
Label(fenetre,text="Train").pack(padx=5,pady=5)

info = StringVar()
Label(fenetre,textvariable=info).pack(padx=5,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj():
	fenetre.after(temps,maj)

def init():
	randNum = random.random()
	sleep(randNum)
	fenetre.after(temps,maj)

init()

# On lance la boucle d'exécution
fenetre.mainloop()
