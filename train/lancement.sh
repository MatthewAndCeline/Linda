#!/bin/bash
#Lancement des différents agents
echo "Lancement de l'opérateur !"
./operateur.py&
echo "Lancement du capteur demandes entrées !"
./c_demandes_entrees.py&
echo "Lancement du capteur demandes de sorties !"
./c_demandes_sorties.py&
echo "Lancement du capteur acquittement entrées !"
./c_acquittement_entrees.py&
echo "Lancement du capteur acquittement sorties !"
./c_acquittement_sorties.py&

echo "Lancement des Trains !"
#for n in $1
#do
#	numTrain= n * 50
#	./train.py numTrain&
#done
./train.py 0&
./train.py 100&
#./train.py 200&
#./train.py 300&
#./train.py 400&
echo "Fait."
