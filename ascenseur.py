#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK ascenseur ")

from Tkinter import *
import time
import linda
import threading

linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Ascenseur")
fenetre.geometry('150x50+800+500')

# Données affichées variant avec le temps
autorisation = StringVar()
Label(fenetre,textvariable=autorisation).pack(padx=5,pady=5)
action = StringVar()
Label(fenetre,textvariable=action).pack(padx=5,pady=5)
occupation = StringVar()
Label(fenetre,textvariable=occupation).pack(padx=5,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj(TEcouter):
	etat_autorisation = ts._rd(("autorisation_ascenseur",str))[1]
	autorisation.set(etat_autorisation)
	etat_action = ts._rd(("action_ascenseur",str))[1]
	action.set(etat_action)
	etat_occupation = ts._rd(("occupation_ascenseur",str))[1]
	occupation.set(etat_occupation)
	if(etat_autorisation == "autorisé"):
		ts._in(("Interdire_Ascenseur",))
		etat_autorisation = "interdit"
		autorisation.set(etat_autorisation)
		ts._in(("autorisation_ascenseur","autorisé"))
		ts._out(("autorisation_ascenseur","interdit"))
		TEcouter._Thread__stop()
	else:
		ts._in(("Autoriser_Ascenseur",))
		etat_autorisation = "autorisé"
		autorisation.set(etat_autorisation)
		ts._in(("autorisation_ascenseur","interdit"))
		ts._out(("autorisation_ascenseur","autorisé"))
		TEcouter = threading.Thread(None,ecouterAppel)
		TEcouter.start()
		#fenetre.after(temps / 60, ecouterAppel)
	fenetre.after(temps,maj,TEcouter)

def ecouterAppel():
	etat_autorisation = ts._rd(("autorisation_ascenseur",str))[1]
	etat_action = ts._rd(("action_ascenseur",str))[1]
	if (etat_autorisation == "autorisé"):
		if (etat_action == "attendEnHaut"):
			#Prendre des clients
			nom = ts._in(("veut_descendre",str))[1]
			#Descendre
			etat_action = "Descent"
			ts._in(("action_ascenseur",str))
			ts._out(("action_ascenseur",etat_action))
			action.set(etat_action)
			etat_occupation = nom #+ " " + nom2 + " " + nom3
			ts._in(("occupation_ascenseur",str))
			ts._out(("occupation_ascenseur",etat_occupation))
			occupation.set(etat_occupation)
			time.sleep(temps / 30000.0)
			#Vider
			ts._out(("descendu",nom))
			etat_occupation = "vide"
			ts._in(("occupation_ascenseur",str))
			ts._out(("occupation_ascenseur",etat_occupation))
			occupation.set(etat_occupation)
			etat_action = "AttendEnBas"
			ts._in(("action_ascenseur",str))
			ts._out(("action_ascenseur",etat_action))
			action.set(etat_action)
			fenetre.after(temps / 60, ecouterAppel)

TEcouter = threading.Thread(None,ecouterAppel)
T = threading.Thread(None,maj,None,(TEcouter,))
T.start()

# On lance la boucle d'exécution
fenetre.mainloop()


