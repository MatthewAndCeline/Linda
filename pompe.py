#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK pompe ")

from Tkinter import *
import time

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Pompe")
fenetre.geometry('150x50+400+0')

# Données affichées variant avec le temps
enroute = StringVar()
Label(fenetre,textvariable=enroute).pack(padx=10,pady=10)

# Fonction de mise à jour à réaliser en permanence
def maj():
    enroute.set("Je suis éteinte")
    fenetre.after(1000,maj)
maj()

# On lance la boucle d'exécution
fenetre.mainloop()
