#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK ascenseur ")

from Tkinter import *
import time
import linda

linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]
duree_une_heure = ts._rd(("Duree_une_heure",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Ascenseur")
fenetre.geometry('150x50+800+500')

# Données affichées variant avec le temps
action = StringVar()
Label(fenetre,textvariable=action).pack(padx=5,pady=5)
position = StringVar()
Label(fenetre,textvariable=position).pack(padx=5,pady=5)

def init():
	etat_action = "attend"
	action.set(etat_action)
	etat_position = "haut"
	position.set(etat_position)
	fenetre.after(temps,maj,"attend","haut")

# Fonction de mise à jour à réaliser en permanence
def maj(etat_action, etat_position):
	if (etat_action == "attend"):
		#Recevoir une demande client
		tpl = ts._in(("appel_ascenseur",str,str))
		nom = tpl[2]
		demande = tpl[1]
		print("ascenseur appel " + nom + " " + demande)
		#Eventuellement, se déplacer vers la personne
		if (etat_position == "haut"):
			# si l'ascenseur est en haut et la personne en bas, il faut d'abord descendre la chercher
			if (demande == "monter"):
				time.sleep(temps)
		if (etat_position == "bas"):
			# si l'ascenseur est en bas et la personne en haut, il faut d'abord monter la chercher
			if (demande == "descendre"):
				time.sleep(temps)
		#Emmener la personne
		etat_action = demande
		action.set(etat_action)
		time.sleep(temps)
		#Vider l'ascenseur à l'arrivée
		ts._out(("ascenseur_arrivé",nom))
		print("ascenseur arrivé")
		if (demande == "descendre"):
			etat_position = "haut"
		else:
			etat_position = "bas"
		position.set(etat_position)
		etat_action = "attend"
		action.set(etat_action)
		#Prévenir le compteur d'entrées sorties
		ts._out(("Entree/Sortie",demande))
		fenetre.after(temps, maj,etat_action,etat_position)
	else:
		fenetre.after(temps, maj,etat_action,etat_position)
			
init()

# On lance la boucle d'exécution
fenetre.mainloop()


