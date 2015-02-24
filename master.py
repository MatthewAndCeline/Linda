#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
##Import and connect to Linda Server
print("OK master ")
import linda
linda.connect()
##Create TupleSpace
ts = linda.TupleSpace()

linda.universe._out(("TupleSpace drainage", ts))


for i in range(0,10):
	print("MASTER")
	print(ts._in((str, float)))

exit(0)
