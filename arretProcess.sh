#!/bin/bash
process_id=`ps aux | grep ./master.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./c_ch4.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./c_co.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./c_h2O.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./c_fumee.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./c_personnes.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./log_gaz_bas.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./log_gaz_haut.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./log_gaz_critique.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./log_h20_bas.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./log_h20_haut.py| grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./log_h20_critique.py| grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./log_heure_pleine.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./log_heure_creuse.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./log_fumee_bas.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./log_fumee_haut.py| grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./log_personnes_nul.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./pompe.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./ventilateur.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./horloge.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./lampe.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./alarme.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./ascenseur.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_gaz_bas.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_gaz_haut.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_gaz_critique.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_h2O_bas.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_h2O_haut.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_h2O_critique.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_heure_pleine.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_heure_creuse.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_personnes_nul.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_fumee_bas.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_fumee_haut.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi


process_id=`ps aux | grep ./isidor.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./isabelle.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./marcel.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./michel.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./marguerite.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id

fiprocess_id=`ps aux | grep ./monique.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./marc.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./mathilde.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi
