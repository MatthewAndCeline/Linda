#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
##Import and connect to Linda Server
print("OK master ")
import linda
import time
linda.connect()
##Create TupleSpace
ts = linda.TupleSpace()

linda.universe._out(("TupleSpace drainage", ts))

ts._out(("Niveau_CH4",0.0))
ts._out(("Niveau_H2O",0.0))
ts._out(("Niveau_CO",0.0))

while True:
	print("MASTER")
	print(ts._in((str, float)))
