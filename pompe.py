#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK pompe ")


import linda
import time
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]
#Aout d'un tuple pour la gestion de l'etat de la pompe
#etat_pompe = "desactivé"
while True:
	etat_pompe = ts._in(("etat_pompe",str))[1]
#	print etat_pompe
	if(etat_pompe == "desactivé"):
		ts._in(("Pompe_En_Route",))
		print("Activation de la pompe");
#		etat_pompe = "activé"
		ts._out(("etat_pompe","activé"))
	else:
		ts._in(("Pompe_Arreté",))
		print("Desactivation de la pompe");
#		etat_pompe = "desactivé"
		ts._out(("etat_pompe","desactivé"))
		
	time.sleep(1)
	
exit(0)
