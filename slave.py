#!/usr/bin/env python
# -*- coding: utf-8-unix -*-

import linda
linda.connect()

#ts = linda.TupleSpace()
#print(linda.universe._rd(("Mon TS Préféré", ts))[1])
print("Avant rd")
ts = linda.universe._rd(("Mon TS Préféré", linda.TupleSpace))[1]
ts2 = linda.universe._rd(("Second Tuple", linda.TupleSpace))[1]
print("Après rd")

print(ts2._in((1, str, 2)))
while True:
	print("coucou")
	print(ts._in((1, 2, int)))


