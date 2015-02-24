#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK Capteur CH4")

import linda
import time
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

t = [0.0, 2.3, 4.7, 5.3, 7.2, 8.1, 9.6, 10.0]
k = 0

for i in range(0,10):
	ts._in(("Niveau_CH4",float))
	if (k == 7):
		k = 0
	else:
		k += 1
	ts._out(("Niveau_CH4",t[k]))
	time.sleep(1)

exit(0)
