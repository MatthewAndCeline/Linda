#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK pompe ")


#import linda
#import time
#linda.connect()
#ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]
##Aout d'un tuple pour la gestion de l'etat de la pompe
##etat_pompe = "desactivé"
#while True:
#	etat_pompe = ts._in(("etat_pompe",str))[1]
##	print etat_pompe
#	if(etat_pompe == "desactivé"):
#		ts._in(("Pompe_En_Route",))
#		print("Activation de la pompe");
##		etat_pompe = "activé"
#		ts._out(("etat_pompe","activé"))
#	else:
#		ts._in(("Pompe_Arreté",))
#		print("Desactivation de la pompe");
##		etat_pompe = "desactivé"
#		ts._out(("etat_pompe","desactivé"))
#		
#	time.sleep(1)
#	
#exit(0)

from Tkinter import *
import time
import linda

linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Pompe")
fenetre.geometry('200x50+500+0')

# Données affichées variant avec le temps
etatPompe = StringVar()
Label(fenetre,textvariable=etatPompe).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj():
	etat_pompe = ts._rd(("etat_pompe",str))[1]
	etatPompe.set(etat_pompe)
	if(etat_pompe == "desactivé"):
		ts._in(("Pompe_En_Route",))
		etat_pompe = "activé"
		etatPompe.set(etat_pompe)
		ts._in(("etat_pompe","desactivé"))
		ts._out(("etat_pompe","activé"))
	else:
		ts._in(("Pompe_Arreté",))
		etat_pompe = "desactivé"
		etatPompe.set(etat_pompe)
		ts._in(("etat_pompe","activé"))
		ts._out(("etat_pompe","desactivé"))
	fenetre.after(1000,maj)
maj()

# On lance la boucle d'exécution
fenetre.mainloop()


