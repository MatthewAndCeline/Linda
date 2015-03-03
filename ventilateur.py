#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK ventaliteur ")


#import linda
#import time
#linda.connect()
#ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]
##etat_ventilateur = "desactivé"

#while True:
#	etat_ventilateur = ts._in(("etat_ventilateur",str))[1]
#	if(etat_ventilateur == "desactivé"):
#		ts._in(("Ventilo_En_Route",))
#		print("Activation du ventilateur");
##		etat_ventilateur = "activé"
#		ts._out(("etat_ventilateur","activé"))
#	else:
#		ts._in(("Ventilo_Arreté",))
#		print("Desactivation du ventilateur");
##		etat_ventilateur = "desactivé"
#		ts._out(("etat_ventilateur","desactivé"))
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
fenetre.title("Ventilateur")
fenetre.geometry('200x50+250+0')

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# Données affichées variant avec le temps
etatVentilateur = StringVar()
Label(fenetre,textvariable=etatVentilateur).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj():
	etat_ventilateur = ts._rd(("etat_ventilateur",str))[1]
	etatVentilateur.set(etat_ventilateur)
	if(etat_ventilateur == "desactivé"):
		ts._in(("Ventilo_En_Route",))
		etat_ventilateur = "activé"
		etatVentilateur.set(etat_ventilateur)
		ts._in(("etat_ventilateur","desactivé"))
		ts._out(("etat_ventilateur","activé"))
	else:
		ts._in(("Ventilo_Arreté",))
		etat_ventilateur = "desactivé"
		etatVentilateur.set(etat_ventilateur)
		ts._in(("etat_ventilateur","activé"))
		ts._out(("etat_ventilateur","desactivé"))
	fenetre.after(temps,maj)
maj()

# On lance la boucle d'exécution
fenetre.mainloop()

