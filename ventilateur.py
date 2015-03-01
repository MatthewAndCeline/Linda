#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK ventaliteur ")

import linda
import time
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]
#etat_ventilateur = "desactivé"

while True:
	etat_ventilateur = ts._in(("etat_ventilateur",str))[1]
	if(etat_ventilateur == "desactivé"):
		ts._in(("Ventilo_En_Route",))
		print("Activation du ventilateur");
#		etat_ventilateur = "activé"
		ts._out(("etat_ventilateur","activé"))
	else:
		ts._in(("Ventilo_Arreté",))
		print("Desactivation du ventilateur");
#		etat_ventilateur = "desactivé"
		ts._out(("etat_ventilateur","desactivé"))
		
	time.sleep(1)
	
exit(0)
