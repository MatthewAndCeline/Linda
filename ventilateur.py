#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK ventaliteur ")

from Tkinter import *
import time
import linda

linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Ventilateur")
fenetre.geometry('150x50+200+500')

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]
duree_une_heure = ts._rd(("Duree_une_heure",int))[1]

# Données affichées variant avec le temps
etatVentilateur = StringVar()
Label(fenetre,textvariable=etatVentilateur).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj():
	etat_ventilateur = ts._rd(("etat_ventilateur",str))[1]
	etatVentilateur.set(etat_ventilateur)
	ordre_recu = ts._in(("Ordre_Ventilateur",str))[1]
	if (ordre_recu == "En_Route"):
		etat_ventilateur = "activé"
		etatVentilateur.set(etat_ventilateur)
		ts._in(("etat_ventilateur","desactivé"))
		ts._out(("etat_ventilateur","activé"))
	elif (ordre_recu == "En_Route_Manuel"):
		etat_force = "activé"
		etatVentilateur.set(etat_force + " forcé")
		ts._in("etat_ventilateur_force",str)
		ts._out("etat_ventilateur_force","activé")
		sleep(duree_une_heure / 6)
		ts._in("etat_ventilateur_force","activé")
		ts._out("etat_ventilateur_force","none")
		etatVentilateur.set(etat_ventilateur)	
	elif (ordre_recu == "Arret"):
		etat_ventilateur = "desactivé"
		etatVentilateur.set(etat_ventilateur)
		ts._in(("etat_ventilateur","activé"))
		ts._out(("etat_ventilateur","desactivé"))
	elif (ordre_recu == "Arret_Manuel"):
		etat_force = "activé"
		etatVentilateur.set(etat_force + " forcé")
		ts._in("etat_ventilateur_force",str)
		ts._out("etat_ventilateur_force","desactivé")
		sleep(duree_une_heure / 6)
		ts._in("etat_ventilateur_force","desactivé")
		ts._out("etat_ventilateur_force","none")
		etatVentilateur.set(etat_ventilateur)		
	fenetre.after(temps,maj)

def init():
	fenetre.after(temps,maj)

init()

# On lance la boucle d'exécution
fenetre.mainloop()

