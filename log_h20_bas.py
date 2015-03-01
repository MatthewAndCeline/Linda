#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK logique H2O bas ")

import linda
import time
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

while True:
	ts._in(("H2O_bas_detecté",))
	print("Le niveau H2O est bas !")
	ts._out(("Ventilo_Arreté",))
	ts._out(("Pompe_Arreté",))
	ts._out(("etat_systeme","init"))
	ts._in(("detection_gaz_haut",))
	time.sleep(1)
exit(0)
