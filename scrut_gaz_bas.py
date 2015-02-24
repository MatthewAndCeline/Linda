#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK scrutateur gaz bas ")


import linda
import time
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]
seuil_CH4 = 3.0
seuil_CO = 3.0

while True:
	ts._rd(("detection_gaz_bas",))
	valeur_CH4 = ts._rd(("Niveau_CH4",float))[1]
	valeur_CO = ts._rd(("Niveau_CO",float))[1]
	print("SCRUT_GAZ_BAS : Les Niveau CH4 et CO lus sont :")
	print(valeur_CH4)
	print(valeur_CO)
	if (valeur_CH4 < seuil_CH4 and valeur_CO < seuil_CO):
		print("Gaz bas détecté")
		ts._out(("gaz_bas_detecté",))
		ts._in(("detection_gaz_bas",))
		
	time.sleep(1)

exit(0)
