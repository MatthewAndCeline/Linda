#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK logique gaz bas ")

import linda
import time
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

while True:
	ts._in(("gaz_bas_detecté",))
	print("Gaz Bas détécté, activation de la pompe")
	ts._out(("Pompe_En_Route",))
	#Force H2O bas détécté
	ts._out(("detection_H2O_bas",)) 
	time.sleep(1)
	
exit(0)
