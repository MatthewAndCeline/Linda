#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK logique H2O haut ")

from Tkinter import *
import linda
import time

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Configuration
temps = ts._rd(("Temps_Rafraichissement",int))[1]
seuil_CH4 = ts._rd(("Seuil_CH4",float))[1]
seuil_CO = ts._rd(("Seuil_CO",float))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Logique H2O Haut")
fenetre.geometry('600x100+700+600')

message = StringVar()
Label(fenetre,textvariable=message).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj():
	message.set("attente niveau haut")
	ts._in(("H2O_haut_detecté",))
	valeur_CH4 = ts._rd(("Niveau_CH4",float))[1]
	valeur_CO = ts._rd(("Niveau_CO",float))[1]
	if (valeur_CH4 < seuil_CH4 and valeur_CO < seuil_CO):
		message.set("Gaz < seuil => activation Pompe, detection_H2O_bas, detection_gaz_haut")
		ts._out(("Pompe_En_Route",))
		ts._out(("detection_H2O_bas",))
		ts._out(("detection_gaz_haut",))
	else:
		message.set("Gaz > seuil => activation Ventilo, detection_gaz_bas")
		ts._out(("Ventilo_En_Route",))
		ts._out(("detection_gaz_bas",))
	fenetre.after(temps,maj)
maj()

# On lance la boucle d'exécution
fenetre.mainloop()

