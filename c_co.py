#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Capteur CO")

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
fenetre.title("Capt.CO")
fenetre.geometry('150x50+400+0')

# Données affichées variant avec le temps
info = StringVar()
Label(fenetre,textvariable=info).pack(padx=5,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj(niveau_co):
	pompe_en_route = ts._rd(("etat_pompe",str))[1]
	ventilo_en_route = ts._rd(("etat_ventilateur",str))[1]
	randNum = random.random()
	randNum = round(randNum,2)
	if (ventilo_en_route == "desactivé"):
		if (pompe_en_route == "desactivé"):
			niveau_co += 0.2*randNum
		else:
			niveau_co += randNum
	else:
		if (pompe_en_route == "desactivé"):
			niveau_co -= randNum
		else:
			niveau_co -= 0.3*randNum
	niveau_co = round(k,4)
	info.set(k)
	ts._in(("Niveau_CO",float))
	ts._out(("Niveau_CO",k))
	fenetre.after(temps,maj,k)

def init():
	pompe_en_route = ts._rd(("etat_pompe",str))[1]
	ventilo_en_route = ts._rd(("etat_ventilateur",str))[1]
	fenetre.after(temps,maj,0.0)

init()

# On lance la boucle d'exécution
fenetre.mainloop()

