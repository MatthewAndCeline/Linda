#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK alarme ")

from Tkinter import *
import time
import linda

linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

#Paramétrage du système
temps = ts._rd(("Temps_Rafraichissement",int))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Alarme")
fenetre.geometry('200x50+900+0')

# Données affichées variant avec le temps
etatAlarme = StringVar()
Label(fenetre,textvariable=etatAlarme).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj():
	etat_alarme = ts._rd(("etat_alarme",str))[1]
	etatAlarme.set(etat_alarme)
	if(etat_alarme == "desactivé"):
		ts._in(("Alarme_En_Route",))
		etat_alarme = "activé"
		etatAlarme.set(etat_alarme)
		ts._in(("etat_alarme","desactivé"))
		ts._out(("etat_alarme","activé"))
	else:
		ts._in(("Alarme_Arreté",))
		etat_alarme = "desactivé"
		etatAlarme.set(etat_alarme)
		ts._in(("etat_alarme","activé"))
		ts._out(("etat_alarme","desactivé"))
	fenetre.after(temps,maj)
maj()

# On lance la boucle d'exécution
fenetre.mainloop()


