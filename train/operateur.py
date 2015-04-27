#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK opérateur ")
from Tkinter import *
import time
import linda

#Initialisation de Linda
linda.connect()
ts = linda.TupleSpace()
linda.universe._out(("TupleSpace train", ts))

#Paramétrage du système
temps = 500
ts._out(("Temps_Rafraichissement",temps))
ts._out(("nombre_demandes_sorties",0))
ts._out(("nombre_demandes_entrees",0))

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Opérateur")
fenetre.geometry('150x100+0+0')
info = StringVar()
Label(fenetre,textvariable=info).pack(padx=5,pady=5)
nbPlacesVar = StringVar()
Label(fenetre,textvariable=nbPlacesVar).pack(padx=5,pady=5)

# Fonction de mise à jour à réaliser en permanence
def maj(nbPlacesLibres):
	print("maj opérateur")
	nb_demandes_sorties = ts._rd(("nombre_demandes_sorties",int))[1]
	nb_demandes_entrees = ts._rd(("nombre_demandes_entrees",int))[1]
	if (nb_demandes_sorties > 0 and nb_demandes_entrees == 0):
		ts._out(("accord_sortie",))
		info.set("sortie ok")
		ts._in(("je_suis_sorti",))
		ts._out(("sortie_acquittement",))
		nbPlacesLibres = nbPlacesLibres + 1
	if (nb_demandes_entrees > 0 and nbPlacesLibres > 0):
		ts._out(("accord_entree",))
		info.set("entrée ok")
		ts._in(("je_suis_entre",))
		ts._out(("entree_acquittement",))
		nbPlacesLibres = nbPlacesLibres - 1
	if (nb_demandes_sorties > 0 and nbPlacesLibres == 0):
		ts._out(("accord_sortie",))
		info.set("sortie ok")
		ts._in(("je_suis_sorti",))
		ts._out(("sortie_acquittement",))
		nbPlacesLibres = nbPlacesLibres + 1
	nbPlacesVar.set(nbPlacesLibres)
	fenetre.after(3*temps,maj,nbPlacesLibres)

def init():
	info.set("Opérateur")
	nbPlacesVar.set(3)
	fenetre.after(3*temps,maj,3)

init()

# On lance la boucle d'exécution
fenetre.mainloop()
