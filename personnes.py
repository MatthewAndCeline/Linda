#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Capteur CH4")

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
fenetre.title("Personnes")
fenetre.geometry('500x250+0+500')

# Données affichées variant avec le temps
isidor = StringVar()
Label(fenetre,textvariable=isidor).pack(padx=5,pady=5)
isabelle = StringVar()
Label(fenetre,textvariable=isabelle).pack(padx=5,pady=5)
marcel = StringVar()
Label(fenetre,textvariable=marcel).pack(padx=5,pady=5)
monique = StringVar()
Label(fenetre,textvariable=monique).pack(padx=5,pady=5)
marc = StringVar()
Label(fenetre,textvariable=marc).pack(padx=5,pady=5)
michel = StringVar()
Label(fenetre,textvariable=michel).pack(padx=5,pady=5)
marguerite = StringVar()
Label(fenetre,textvariable=marguerite).pack(padx=5,pady=5)
mathilde = StringVar()
Label(fenetre,textvariable=mathilde).pack(padx=5,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj():
	isidor.set("Isidor")
	isabelle.set("Isabelle")
	marcel.set("Marcel")
	monique.set("Monique")
	marc.set("Marc")
	michel.set("Michel")
	marguerite.set("Marguerite")
	mathilde.set("Mathilde")

maj()


# On lance la boucle d'exécution
fenetre.mainloop()

