#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
##Import and connect to Linda Server
import linda
linda.connect()
##Create TupleSpace
ts = linda.TupleSpace()
ts2 = linda.TupleSpace()


linda.universe._out(("Mon TS Préféré", ts))
linda.universe._out(("Second Tuple", ts2))


ts2._out((1,"gjwxgjxgwj",2))
for i in range(0,10):
	print(i)
	ts._out((1, 2, i))
	

##Capteur_H2O = ts._in(())
