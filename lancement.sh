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
echo "Lancement du logique gaz bas !"
./log_gaz_bas.py&
echo "Lancement du logique gaz haut !"
./log_gaz_haut.py&
echo "Lancement du logique H2O bas !"
./log_h20_bas.py&
echo "Lancement du logique H2O haut !"
./log_h20_haut.py&
echo "Lancement de la Pompe !"
./pompe.py&
echo "Lancement du ventilateur !"
./ventilateur.py&
echo "Lancement du scrutateur gaz bas !"
./scrut_gaz_bas.py&
echo "Lancement du scrutateur gaz haut !"
./scrut_gaz_haut.py&
echo "Lancement du scrutateur H2O bas !"
./scrut_h2O_bas.py&
echo "Lancement du scrutateur H2O haut !"
./scrut_h2O_haut.py&
