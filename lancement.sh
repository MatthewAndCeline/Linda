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

echo "Lancement de la Pompe !"
./pompe.py&
echo "Lancement du ventilateur !"
./ventilateur.py&
echo "Lancement de l'horloge !"
./horloge.py&
echo "Lancement de la lampe !"
./lampe.py&
echo "Lancement de l'alarme !"
./alarme.py&
echo "Lancement de l'ascenseur !"
./ascenseur.py&

echo "Lancement du scrutateur gaz bas !"
./scrut_gaz_bas.py&
echo "Lancement du scrutateur gaz haut !"
./scrut_gaz_haut.py&
echo "Lancement du scrutateur gaz critique !"
./scrut_gaz_critique.py&
echo "Lancement du scrutateur H2O bas !"
./scrut_h2O_bas.py&
echo "Lancement du scrutateur H2O haut !"
./scrut_h2O_haut.py&
echo "Lancement du scrutateur H2O critique !"
./scrut_h2O_critique.py&
echo "Lancement du scrutateur heure pleine !"
./scrut_heure_pleine.py&
echo "Lancement du scrutateur heure creuse !"
./scrut_heure_creuse.py&
echo "Lancement du scrutateur fumée bas !"
./scrut_fumee_bas.py&
echo "Lancement du scrutateur fumée haut !"
./scrut_fumee_haut.py&
echo "Lancement du scrutateur personnes nul !"
./scrut_personnes_nul.py&

echo "Lancement du logique heure pleine !"
./log_heure_pleine.py&
echo "Lancement du logique heure creuse !"
./log_heure_creuse.py&
echo "Lancement du logique gaz bas !"
./log_gaz_bas.py&
echo "Lancement du logique gaz haut !"
./log_gaz_haut.py&
echo "Lancement du logique gaz critique !"
./log_gaz_critique.py&
echo "Lancement du logique H2O bas !"
./log_h20_bas.py&
echo "Lancement du logique H2O haut !"
./log_h20_haut.py&
echo "Lancement du logique H2O critique !"
./log_h20_critique.py&
echo "Lancement du logique fumée bas !"
./log_fumee_bas.py&
echo "Lancement du logique fumée haut !"
./log_fumee_haut.py&
echo "Lancement du logique personnes nul !"
./log_personnes_nul.py&

echo "Lancement des personnes !"
./isidor.py&
./isabelle.py&
./marcel.py&
./michel.py&
./mathilde.py&
./marguerite.py&
./monique.py&

