#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK logique gaz haut ")

import linda
import time
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

while True:
	ts._in(("Gaz_Haut_detecté",))
	print("Logique GAZ HAUT --> Activation Ventilo")
	ts._out(("Ventilo_En_Route",))
	time.sleep(1)
	
exit(0)
