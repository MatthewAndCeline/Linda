#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Capteur H2O")

import linda
import time
linda.connect()

ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

for i in range (0,10):
	ts._in(("Niveau_H2O",float))
	ts._out(("Niveau_H2O", 60.6))	
	time.sleep(1)

exit(0)
