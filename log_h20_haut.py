#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK logique H2O haut ")

import linda
import time
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]
seuil_CH4 = 8.0
seuil_CO = 8.0

while True:
	ts._in(("H2O_haut_detecté",))
	ts._rd(("Niveau_H2O",float))[1]
	valeur_CH4 = ts._rd(("Niveau_CH4",float))[1]
	valeur_CO = ts._rd(("Niveau_CO",float))[1]
	print("LOGIQUE_H2O_HAUT : Le Niveau CH4 lu est :")
	print(valeur_CH4)
	print("LOGIQUE_H2O_HAUT : Le Niveau CO lu est :")
	print(valeur_CO)
	if (valeur_CH4 < seuil_CH4 and valeur_CO < seuil_CO):
		print("Les valeurs de CO et CH4 sont inférieur aux seuils, activationde la pompe")
		ts._out(("Pompe_En_Route",))
		ts._out(("detection_H2O_Bas",))
		ts._out(("detection_gaz_haut",))
	else:
		print("Les valeurs de CO et CH4 sont supérieurs aux seuils, activationde du ventilo")
		ts._out(("Ventilo_En_Route",))
		ts._out(("detection_gaz_bas",))
		
	time.sleep(1)
	
exit(0)
