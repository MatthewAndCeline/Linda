#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK lampe ")

from Tkinter import *
import time
import linda

linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Lampe")
fenetre.geometry('200x50+750+0')

# Données affichées variant avec le temps
etatLampe = StringVar()
Label(fenetre,textvariable=etatLampe).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj():
	etat_lampe = ts._rd(("etat_lampe",str))[1]
	etatLampe.set(etat_lampe)
	if(etat_lampe == "desactivé"):
		ts._in(("Lampe_En_Route",))
		etat_lampe = "activé"
		etatLampe.set(etat_lampe)
		ts._in(("etat_lampe","desactivé"))
		ts._out(("etat_lampe","activé"))
	else:
		ts._in(("Lampe_Arreté",))
		etat_lampe = "desactivé"
		etatLampe.set(etat_lampe)
		ts._in(("etat_lampe","activé"))
		ts._out(("etat_lampe","desactivé"))
	fenetre.after(temps,maj)
maj()

# On lance la boucle d'exécution
fenetre.mainloop()


