#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Capteur CH4")

import linda
import time
linda.connect()

var tab = []
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

for i in range(0,10):
	print ("Capteur CH4 boucle")
	ts._in(("Niveau_CH4",float))
	ts._out(("Niveau_CH4",12.2))
	time.sleep(1)

exit(0)
