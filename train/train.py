#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK train ")

from Tkinter import *
import time
import linda
import random
import sys

#Initialisation de Linda
linda.connect()
ts = linda.universe._rd(("TupleSpace drainage", linda.TupleSpace))[1]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Train")

fenetre.geometry('150x50+200+' + str(sys.argv[1]))
Label(fenetre,text="Train").pack(padx=5,pady=5)

# On lance la boucle d'exécution
fenetre.mainloop()
