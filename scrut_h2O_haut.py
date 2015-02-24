#!/usr/bin/env python
# -*- coding: utf-8-unix -*-
print("OK scrutateur H2O haut ")

#Scrutateur_H2O_Haut(seuil) =
#	Read(ts, <| "detection_H2O_Haut", string |>)
#	. Read(ts, <| "Niveau_H2O", string ;; ?valeur_H2O, float |>) // ? = lecture
#	. (
#			[ valeur_H2O > seuil ]
#				Out(ts, <| "H2O_haut_detecté", string |>)
#				. In(ts, <| "detection_H2O_Haut", string |>
#				. Scrutateur_H2O_Haut(seuil)
#			+
#			[ else ]
#				Scrutateur_H2O_Haut(seuil)
#	)	
