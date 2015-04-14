#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Isabelle")

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
fenetre.title("Isabelle")
fenetre.geometry('150x50+1200+500')

# Données affichées variant avec le temps
ts._out(("Isabelle","etat_location","Dehors"))
location = StringVar()
location.set("Dehors")
Label(fenetre,textvariable=location).pack(padx=5,pady=5)
ts._out(("Isabelle","etat_action","Inactif"))
action = StringVar()
action.set("Inactif")
Label(fenetre,textvariable=action).pack(padx=5,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj():
	etat_action = ts._rd(("Isabelle","etat_action",str))[2]
	if (etat_action == "Inactif"):
		#Reçoit l'ordre de prendre son service
		ts._in(("Equipe_Entrer",1))
		#Appel Ascenseur
		ts._out(("appel_ascenseur","descendre","isabelle"))
		etat_location = "veut descendre"
		print("Isabelle veut descendre")
		ts._in(("Isabelle","etat_location",str))
		ts._out(("Isabelle","etat_location",etat_location))
		location.set(etat_location)
		#Arrivé en bas
		print("Isabelle attend l'ascenseur")
		ts._in(("ascenseur_arrivé","isabelle"))
		print("Isabelle entrée")
		etat_location = "mine"
		ts._in(("Isabelle","etat_location",str))
		ts._out(("Isabelle","etat_location",etat_location))
		location.set(etat_location)
		etat_action = "Travail"
		ts._in(("Isabelle","etat_action",str))
		ts._out(("Isabelle","etat_action",etat_action))
		action.set(etat_action)
		fenetre.update()
	if (etat_action == "Travail"):
		#Reçoit l'ordre de terminer son service
		ts._in(("Equipe_Sortir",1))
		#Appel Ascenseur
		ts._out(("appel_ascenseur","monter","isabelle"))
		etat_location = "veut monter"
		ts._in(("Isabelle","etat_location",str))
		ts._out(("Isabelle","etat_location",etat_location))
		location.set(etat_location)
		#Arrivé en haut
		ts._in(("ascenseur_arrivé","isabelle"))
		print("Isabelle sortie")
		etat_location = "Dehors"
		ts._in(("Isabelle","etat_location",str))
		ts._out(("Isabelle","etat_location",etat_location))
		location.set(etat_location)
		etat_action = "Inactif"
		ts._in(("Isabelle","etat_action",str))
		ts._out(("Isabelle","etat_action",etat_action))
		action.set(etat_action)
		fenetre.update()
	fenetre.after(temps,maj)

def init():
	ts._out(("Isabelle","etat_location","dehors"))
	fenetre.after(temps,maj)

init()

# On lance la boucle d'exécution
fenetre.mainloop()

