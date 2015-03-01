#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK logique H2O bas ")

from Tkinter import *
import linda
import time

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Configuration
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Logique H2O Bas")
fenetre.geometry('600x100+0+600')

# Données affichées variant avec le temps
message = StringVar()
Label(fenetre,textvariable=message).pack(padx=10,pady=10)

def maj():
	message.set("en attente niveau bas")
	ts._in(("H2O_bas_detecté",))
	etat_ventilo = ts._rd(("etat_ventilateur",str))[1]
	if (etat_ventilo == "activé"):
		message.set("arrêt ventilo, arrêt pompe, arrêt detection_gaz_haut, demarrage detection_H2O_haut")
		ts._out(("Ventilo_Arreté",))
	else:
		message.set("arrêt pompe, arrêt detection_gaz_haut, demarrage detection_H2O_haut")
	ts._out(("Pompe_Arreté",))
	ts._out(("detection_H2O_haut",))
	ts._inp(("detection_gaz_haut",))
	fenetre.after(temps,maj)
maj()

# On lance la boucle d'exécution
fenetre.mainloop()


#import linda
#import time
#linda.connect()
#ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#while True:
#	ts._in(("H2O_bas_detecté",))
#	print("Le niveau H2O est bas !")
#	ts._out(("Ventilo_Arreté",))
#	ts._out(("Pompe_Arreté",))
#	#ts._out(("etat_systeme","init"))
#	ts._in(("detection_gaz_haut",))
#	time.sleep(1)
#exit(0)
