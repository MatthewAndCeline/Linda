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

while True:
	print("MASTER")
	print(ts._in((str,float)))

exit(0)
