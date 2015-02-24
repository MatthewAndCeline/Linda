#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
##Import and connect to Linda Server
from linda import *
connect()
##Create TupleSpace
ts = TupleSpace()
##ts = linda.universe._rd(("My identifying string", linda.TupleSpace))[1]
ts._out((1, 2, 3))
print(ts._in((1, 2, int)))

##Capteur_H2O = ts._in(())
