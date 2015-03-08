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

# Définition des Personnes
class Personne:
	def affiche(self):
		self.message.set(self.nom + " : " + self.loc)

class Ingenieur(Personne):
	""

class Ouvrier(Personne):
	""

isidor = Ingenieur()
isidor.nom = "Isidor"
isidor.equipe = 1
isidor.loc = "dehors"
isidor.message = StringVar()

isabelle = Ingenieur()
isabelle.nom = "Isabelle"
isabelle.equipe = 2
isabelle.loc = "dehors"
isabelle.message = StringVar()

marcel = Ouvrier()
marcel.nom = "Marcel"
marcel.equipe = 1
marcel.loc = "dehors"
marcel.message = StringVar()

monique = Ouvrier()
monique.nom = "Monique"
monique.equipe = 1
monique.loc = "dehors"
monique.message = StringVar()

marc = Ouvrier()
marc.nom = "Marc"
marc.equipe = 1
marc.loc = "dehors"
marc.message = StringVar()

michel = Ouvrier()
michel.nom = "Michel"
michel.equipe = 2
michel.loc = "dehors"
michel.message = StringVar()

marguerite = Ouvrier()
marguerite.nom = "Marguerite"
marguerite.equipe = 2
marguerite.loc = "dehors"
marguerite.message = StringVar()

mathilde = Ouvrier()
mathilde.nom = "Mathilde"
mathilde.equipe = 2
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
	fenetre.after(0,surveillerDebutService)

def surveillerDebutService():
	equipe = ts._in(("Equipe_Entrer",int))[1]
	if (equipe == 1):
		isidor.loc = "veut entrer"
		isidor.affiche()
		marcel.loc = "veut entrer"
		marcel.affiche()
		monique.loc = "veut entrer"
		monique.affiche()
		marc.loc = "veut entrer"
		marc.affiche()
	else:
		isabelle.loc = "veut entrer"
		isabelle.affiche()
		michel.loc = "veut entrer"
		michel.affiche()
		marguerite.loc = "veut entrer"
		marguerite.affiche()
		mathilde.loc = "veut entrer"
		mathilde.affiche()
	fenetre.after(temps,surveillerDebutService)

maj()


# On lance la boucle d'exécution
fenetre.mainloop()

