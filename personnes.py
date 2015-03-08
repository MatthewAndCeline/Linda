#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Personnes")

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

# Classe Personne
class Personne:
	def affiche(self):
		self.message.set(self.nom + " : " + self.loc)

isidor = Personne()
isidor.nom = "Isidor"
isidor.loc = "dehors"
isidor.message = StringVar()

isabelle = Personne()
isabelle.nom = "Isabelle"
isabelle.loc = "dehors"
isabelle.message = StringVar()

marcel = Personne()
marcel.nom = "Marcel"
marcel.loc = "dehors"
marcel.message = StringVar()

monique = Personne()
monique.nom = "Monique"
monique.loc = "dehors"
monique.message = StringVar()

marc = Personne()
marc.nom = "Marc"
marc.loc = "dehors"
marc.message = StringVar()

michel = Personne()
michel.nom = "Michel"
michel.loc = "dehors"
michel.message = StringVar()

marguerite = Personne()
marguerite.nom = "Marguerite"
marguerite.loc = "dehors"
marguerite.message = StringVar()

mathilde = Personne()
mathilde.nom = "Mathilde"
mathilde.loc = "dehors"
mathilde.message = StringVar()

# Données affichées variant avec le temps
Label(fenetre,textvariable=isidor.message).pack(padx=5,pady=5)
Label(fenetre,textvariable=isabelle.message).pack(padx=5,pady=5)
Label(fenetre,textvariable=marcel.message).pack(padx=5,pady=5)
Label(fenetre,textvariable=monique.message).pack(padx=5,pady=5)
Label(fenetre,textvariable=marc.message).pack(padx=5,pady=5)
Label(fenetre,textvariable=michel.message).pack(padx=5,pady=5)
Label(fenetre,textvariable=marguerite.message).pack(padx=5,pady=5)
Label(fenetre,textvariable=mathilde.message).pack(padx=5,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj():
	isidor.affiche()
	isabelle.affiche()
	marcel.affiche()
	monique.affiche()
	marc.affiche()
	michel.affiche()
	marguerite.affiche()
	mathilde.affiche()


maj()


# On lance la boucle d'exécution
fenetre.mainloop()

