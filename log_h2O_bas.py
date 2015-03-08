#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK logique H2O bas ")

from Tkinter import *
import linda
import time
import threading

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Configuration
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Logique H2O Bas")
fenetre.geometry('150x50+800+300')

# Données affichées variant avec le temps
message = StringVar()
Label(fenetre,textvariable=message).pack(padx=10,pady=10)

def maj():
	message.set("en attente niveau bas")
	ts._in(("H2O_bas_detecté",))
	etat_ventilo = ts._rd(("etat_ventilateur",str))[1]
	if (etat_ventilo == "activé"):
		message.set("arrêt ventilo, arrêt pompe, demarrage detection_H2O_haut")
		ts._out(("Ordre_Ventilateur","Arret"))
	else:
		message.set("arrêt pompe, arrêt detection_gaz_haut, demarrage detection_H2O_haut")
		ts._in(("detection_gaz_haut",))
	ts._out(("Pompe_Arreté",))
	ts._out(("detection_H2O_haut",))
	fenetre.after(temps,maj)

T = threading.Thread(None,maj)
T.start()

# On lance la boucle d'exécution
fenetre.mainloop()

