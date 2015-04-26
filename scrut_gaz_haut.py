#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK scrutateur gaz haut ")

from Tkinter import *
import linda
import time

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]
seuil_CH4 = ts._rd(("Seuil_CH4",float))[1]
seuil_CO = ts._rd(("Seuil_CO",float))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Scrutateur Gaz Haut")
fenetre.geometry('200x200+500+200')

# Données affichées variant avec le temps
str_valeur_CH4 = StringVar()
Label(fenetre,textvariable=str_valeur_CH4).pack(padx=10,pady=20)
str_valeur_CO = StringVar()
Label(fenetre,textvariable=str_valeur_CO).pack(padx=10,pady=10)


# Fonction de mise à jour à réaliser en permanence
def maj():
	ts._rd(("detection_gaz_haut",))
	valeur_CH4 = ts._rd(("Niveau_CH4",float))[1]
	valeur_CO = ts._rd(("Niveau_CO",float))[1]
	str_valeur_CH4.set(valeur_CH4)
	str_valeur_CO.set(valeur_CO)
	if (valeur_CH4 > seuil_CH4 or valeur_CO > seuil_CO):
		ts._in(("detection_gaz_haut",))
		ts._out(("Gaz_haut_detecté",))
	fenetre.after(temps,maj)

maj()

# On lance la boucle d'exécution
fenetre.mainloop()
