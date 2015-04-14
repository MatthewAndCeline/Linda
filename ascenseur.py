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
position = StringVar()
Label(fenetre,textvariable=position).pack(padx=5,pady=5)

def init():
	etat_autorisation = ts._rd(("autorisation_ascenseur",str))[1]
	autorisation.set(etat_autorisation)
	action.set("attend")
	position.set("haut")
	occupation.set("vide")
	fenetre.after(temps,maj)
	fenetre.after(temps / 60, ecouterAppel)

# Fonction de mise à jour à réaliser en permanence
def maj():
	etat_autorisation = ts._rd(("autorisation_ascenseur",str))[1]
	autorisation.set(etat_autorisation)
	if(etat_autorisation == "autorisé"):
		ts._in(("Interdire_Ascenseur",))
		print("Interdire Ascenseur")
		etat_autorisation = "interdit"
		autorisation.set(etat_autorisation)
		ts._in(("autorisation_ascenseur","autorisé"))
		ts._out(("autorisation_ascenseur","interdit"))
	else:
		ts._in(("Autoriser_Ascenseur",))
		print("Autoriser Ascenseur")
		etat_autorisation = "autorisé"
		autorisation.set(etat_autorisation)
		ts._in(("autorisation_ascenseur","interdit"))
		ts._out(("autorisation_ascenseur","autorisé"))
		fenetre.after(temps / 60, ecouterAppel)
	fenetre.after(temps,maj)

def ecouterAppel():
	etat_autorisation = ts._rd(("autorisation_ascenseur",str))[1]
	etat_action = ts._rd(("action_ascenseur",str))[1]
	if (etat_autorisation == "autorisé"):
		if (etat_action == "attend"):
			#Prendre des clients
			tpl = ts._in(("appel_ascenseur",str,str))
			nom = tpl[2]
			demande = tpl[1]
			print("ascenseur appel " + nom + " " + demande)
			#Descendre
			etat_action = demande
			ts._in(("action_ascenseur",str))
			ts._out(("action_ascenseur",etat_action))
			action.set(etat_action)
			etat_occupation = nom
			ts._in(("occupation_ascenseur",str))
			ts._out(("occupation_ascenseur",etat_occupation))
			occupation.set(etat_occupation)
			time.sleep(temps / 30000)
			#Vider
			ts._out(("ascenseur_arrivé",nom))
			print("ascenseur arrivé")
			etat_occupation = "vide"
			ts._in(("occupation_ascenseur",str))
			ts._out(("occupation_ascenseur",etat_occupation))
			occupation.set(etat_occupation)
			etat_action = "attend"
			ts._in(("action_ascenseur",str))
			ts._out(("action_ascenseur",etat_action))
			action.set(etat_action)
			fenetre.after(temps / 60, ecouterAppel)

init()

# On lance la boucle d'exécution
fenetre.mainloop()


