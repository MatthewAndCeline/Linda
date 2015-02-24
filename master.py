#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
##Import and connect to Linda Server
print("OK master ")
import linda
linda.connect()
##Create TupleSpace
ts = linda.TupleSpace()

linda.universe._out(("Mon TS Préféré", ts))

for i in range(0,10):
	print(i)
	ts._out((1, 2, i))
	

##Capteur_H2O = ts._in(())
