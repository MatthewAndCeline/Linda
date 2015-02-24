#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK scrutateur H2O bas ")

import linda
import time
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]
seuil = 4.0

while True:
	ts._rd(("detection_H2O_bas",))
	valeur_H2O = ts._rd(("Niveau_H2O",float))[1]
	print("SCRUT_H2O_BAS : Le Niveau H2O lu est :")
	print(valeur_H2O)
	if (valeur_H2O < seuil):
		ts._out(("H2O_bas_detecté",))
		ts._in(("detection_H2O_bas",))
		
	time.sleep(1)

exit(0)
