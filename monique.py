#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Monique")

from Tkinter import *
import linda
import time
import random
import threading

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Monique")
fenetre.geometry('150x50+200+600')

# Données affichées variant avec le temps
ts._out(("Monique","etat_location","Dehors"))
location = StringVar()
location.set("Dehors")
Label(fenetre,textvariable=location).pack(padx=5,pady=5)
ts._out(("Monique","etat_action","Inactif"))
action = StringVar()
action.set("Inactif")
Label(fenetre,textvariable=action).pack(padx=5,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj():
	etat_action = ts._rd(("Monique","etat_action",str))[2]
	if (etat_action == "Inactif"):
		#Reçoit l'ordre de prendre son service
		ts._in(("Equipe_Entrer",2))
		#Appel Ascenseur
		ts._out(("appel_ascenseur","descendre","Monique"))
		etat_location = "veut descendre"
		print("Monique veut descendre")
		ts._in(("Monique","etat_location",str))
		ts._out(("Monique","etat_location",etat_location))
		location.set(etat_location)
		#Arrivé en bas
		print("Monique attend l'ascenseur")
		ts._in(("ascenseur_arrivé","Monique"))
		print("Monique entrée")
		etat_location = "mine"
		ts._in(("Monique","etat_location",str))
		ts._out(("Monique","etat_location",etat_location))
		location.set(etat_location)
		etat_action = "Travail"
		ts._in(("Monique","etat_action",str))
		ts._out(("Monique","etat_action",etat_action))
		action.set(etat_action)
		fenetre.update()
	if (etat_action == "Travail"):
		#Reçoit l'ordre de terminer son service
		ts._in(("Equipe_Sortir",2))
		#Appel Ascenseur
		ts._out(("appel_ascenseur","monter","Monique"))
		etat_location = "veut monter"
		ts._in(("Monique","etat_location",str))
		ts._out(("Monique","etat_location",etat_location))
		location.set(etat_location)
		#Arrivé en haut
		ts._in(("ascenseur_arrivé","Monique"))
		print("Monique sortie")
		etat_location = "Dehors"
		ts._in(("Monique","etat_location",str))
		ts._out(("Monique","etat_location",etat_location))
		location.set(etat_location)
		etat_action = "Inactif"
		ts._in(("Monique","etat_action",str))
		ts._out(("Monique","etat_action",etat_action))
		action.set(etat_action)
		fenetre.update()
	fenetre.after(temps,maj)

def init():
	ts._out(("Monique","etat_location","dehors"))
	fenetre.after(temps,maj)

init()

# On lance la boucle d'exécution
fenetre.mainloop()

