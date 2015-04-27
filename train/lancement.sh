#!/bin/bash
#Lancement des différents agents
echo "Lancement de l'opérateur !"
./operateur.py&
echo "Lancement du capteur demandes entrées !"
./c_demandes_entrees.py&
echo "Lancement du capteur demandes de sorties !"
./c_demandes_sorties.py&

echo "Lancement des Trains !"
for n in $1
do
	numTrain= n * 50
	./train.py n&
done
echo "Fait."
