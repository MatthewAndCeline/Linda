#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
##Import and connect to Linda Server
import linda 
linda.connect()
##Create TupleSpace
ts = linda.TupleSpace()
ts2 = linda.TupleSpace()

linda.universe._out(("My identifying string", ts))
linda.universe._out(("This is tuple 2", ts2))

##ts = linda.universe._rd(("My identifying string", linda.TupleSpace))[1]

ts._out((1, 2, 3))

print(ts._in((1, 2, int)))


##Capteur_H2O = ts._in(())
