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
etat_autorisation = ""
autorisation = StringVar()
Label(fenetre,textvariable=autorisation).pack(padx=5,pady=5)
etat_action = ""
action = StringVar()
Label(fenetre,textvariable=action).pack(padx=5,pady=5)
etat_occupation = ""
occupation = StringVar()
Label(fenetre,textvariable=occupation).pack(padx=5,pady=5)
etat_position = ""
position = StringVar()
Label(fenetre,textvariable=position).pack(padx=5,pady=5)

def init():
	print("J'AI MODIfIE L'ASCENSEUR !!!")
	etat_autorisation = ts._rd(("autorisation_ascenseur",str))[1]
	print("Je suis un ascenseur, je connais mon état : " + etat_autorisation)
	autorisation.set(etat_autorisation)
	etat_action = "attend"
	action.set(etat_action)
	etat_position = "haut"
	position.set(etat_position)
	etat_occupation = "vide"
	occupation.set(etat_occupation)
	fenetre.after(temps,maj)
	fenetre.after(temps / 2, ecouterAppel)

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
	fenetre.after(temps,maj)
 
def ecouterAppel():
	print("Je suis un ascenseur qui écoute")
	if (etat_autorisation == "autorisé"):
		print("Je suis un ascenseur autorisé qui écoute")
		if (etat_action == "attend"):
			print("Je suis en train d'attendre un client")
			#Recevoir une demande client
			tpl = ts._in(("appel_ascenseur",str,str))
			nom = tpl[2]
			demande = tpl[1]
			print("ascenseur appel " + nom + " " + demande)
			#Eventuellement, se déplacer vers la personne
			if (etat_position == "haut"):
				# si l'ascenseur est en haut et la personne en bas, il faut d'abord descendre la chercher
				if (demande == "monter"):
					print("avant sleep")
					time.sleep(temps / 1800)
					print("après sleep")
			if (etat_position == "bas"):
				# si l'ascenseur est en bas et la personne en haut, il faut d'abord monter la chercher
				if (demande == "descendre"):
					print("avant sleep")
					time.sleep(temps / 1800)
					print("après sleep")
			print("après le if etat_position")
			#Emmener la personne
			etat_action = demande
			action.set(etat_action)
			print("après modif etat_action")
			etat_occupation = nom
			occupation.set(etat_occupation)
			print("avant sleep")
			time.sleep(temps / 1800)
			print("après sleep")
			#Vider l'ascenseur à l'arrivée
			ts._out(("ascenseur_arrivé",nom))
			print("ascenseur arrivé")
			etat_occupation = "vide"
			occupation.set(etat_occupation)
			if (demande == "descendre"):
				etat_position = "haut"
			else:
				etat_position = "bas"
			position.set(etat_position)
			etat_action = "attend"
			action.set(etat_action)
			#Prévenir le compteur d'entrées sorties
			ts._out(("Entree/Sortie",demande))
			fenetre.after(temps, ecouterAppel)
		else:
			print("Je suis un ascenseur pas en train d'attendre : " + etat_action + " qui écoutera peut être encore")
			fenetre.after(temps, ecouterAppel)
	else:
		print("Je suis un ascenseur pas autorisé : " + etat_autorisation + " qui écoutera peut être encore")
		fenetre.after(temps, ecouterAppel)
			
init()

# On lance la boucle d'exécution
fenetre.mainloop()


