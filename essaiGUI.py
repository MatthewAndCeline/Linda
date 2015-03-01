#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK essaiGUI")

# On importe Tkinter
from Tkinter import *
import time

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

def maj():
    # on arrive ici toutes les 1000 ms
    heure.set(time.strftime('%H:%M:%S'))
    fenetre.after(1000,maj)

heure = StringVar()
Label(fenetre,textvariable=heure).pack(padx=10,pady=10)

maj()
# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()

