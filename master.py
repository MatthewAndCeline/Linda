import linda()
linda.connect()

mts = linda.TupleSpace()

linda.universe._out(("Master-space", mts))
print linda.universe(("Masterspace", mts))
