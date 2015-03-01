#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
##Import and connect to Linda Server
print("OK master ")
import linda
import time
linda.connect()
##Create TupleSpace
ts = linda.TupleSpace()
linda.universe._out(("TupleSpace drainage", ts))

#Initialisation du systéme
#Valeurs des seuils
ts._out(("Niveau_CH4",0.0))
ts._out(("Niveau_H2O",0.0))
ts._out(("Niveau_CO",0.0))
#Etat de la pompe et du ventilateur
ts._out(("etat_pompe","desactivé"))
ts._out(("etat_ventilateur","desactivé"))


ts._out(("detection_H2O_haut",))
ts._out(("detection_gaz_haut",))

while True:

#	print("MASTER : ------ Gestion du Cycle ------ ")
	
	#print(ts._rd(("H2O_haut_detecté",)))
	#print("MASTER : Le scrutateur H2O Haut a signalé une montée dangereuse du niveau")
	#print(ts._rd(("Niveau_CH4", float)))
	#print(ts._rd(("Niveau_H2O", float)))
	#print(ts._rd(("Niveau_CO", float)))

	time.sleep(1)

