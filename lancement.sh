#!/bin/bash
#Lancement des différents agents
echo "Lancement du master !"
./master.py&
echo "Lancement du capteur CH4 !"
./c_ch4.py&
echo "Lancement du capteur CO !"
./c_co.py&
echo "Lancement du capteur H2O !"
./c_h2O.py&
echo "Lancement du capteur de personnes !"
./c_personnes.py&

echo "Lancement de la Pompe !"
./pompe.py&
echo "Lancement du ventilateur !"
./ventilateur.py&
echo "Lancement de l'horloge !"
./horloge.py&
echo "Lancement de la lampe !"
./lampe.py&
echo "Lancement de l'ascenseur !"
./ascenseur.py&

echo "Lancement du scrutateur gaz bas !"
./scrut_gaz_bas.py&
echo "Lancement du scrutateur gaz haut !"
./scrut_gaz_haut.py&
echo "Lancement du scrutateur H2O bas !"
./scrut_h2O_bas.py&
echo "Lancement du scrutateur H2O haut !"
./scrut_h2O_haut.py&
echo "Lancement du scrutateur heure pleine !"
./scrut_heure_pleine.py&
echo "Lancement du scrutateur heure creuse !"
./scrut_heure_creuse.py&

echo "Lancement du logique heure pleine !"
./log_heure_pleine.py&
echo "Lancement du logique heure creuse !"
./log_heure_creuse.py&
echo "Lancement du logique gaz bas !"
./log_gaz_bas.py&
echo "Lancement du logique gaz haut !"
./log_gaz_haut.py&
echo "Lancement du logique H2O bas !"
./log_h2O_bas.py&
echo "Lancement du logique H2O haut !"
./log_h2O_haut.py&

echo "Lancement des personnes !"
./isidor.py&
./isabelle.py&
./marc.py&
./marcel.py&
./michel.py&
./mathilde.py&
./marguerite.py&
./monique.py&

