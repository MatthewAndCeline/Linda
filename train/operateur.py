#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK opérateur ")
from Tkinter import *
import time
import linda

#Initialisation de Linda
linda.connect()
ts = linda.TupleSpace()
linda.universe._out(("TupleSpace train", ts))

#Paramétrage du système
temps = 500
ts._out(("Temps_Rafraichissement",temps))
ts._out(("nombre_demandes_sorties",0))
ts._out(("nombre_demandes_sorties",0))

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Opérateur")
fenetre.geometry('150x50+0+0')
Label(fenetre,text="Opérateur").pack(padx=5,pady=5)
info = StringVar()
Label(fenetre,textvariable=info).pack(padx=5,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj(nbPlacesLibres):
	fenetre.after(temps,maj,nbPlacesLibres)

def init():
	info.set("3 places")
	fenetre.after(temps,maj,3)

init()

# On lance la boucle d'exécution
fenetre.mainloop()