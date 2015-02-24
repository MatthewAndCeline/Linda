#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Capteur CO")
import linda
import time

linda.connect()

ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

for i in range(0,10):
	ts._out(("Niveau_CO",12.2))
	time.sleep(1)

exit(0)
