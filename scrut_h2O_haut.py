#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK scrutateur H2O haut ")

import linda
import time
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

while True:
	ts._rd(("detection_H2O_haut",))
	a = ts._rd(("Niveau_H2O",float))
	print("Le Niveau H2O lu est :")
	print(a[1])
	time.sleep(1)
