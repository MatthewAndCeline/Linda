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

process_id=`ps aux | grep ./log_gaz_bas.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./log_gaz_haut.py | grep -v root | grep -v grep | awk '{print $2}'`
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

process_id=`ps aux | grep ./pompe.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./ventilateur.py | grep -v root | grep -v grep | awk '{print $2}'`
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

process_id=`ps aux | grep ./scrut_h2O_bas.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_h2O_haut.py | grep -v root | grep -v grep | awk '{print $2}'`
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

process_id=`ps aux | grep ./scrut_heure_pleine.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./scrut_heure_creuse.py | grep -v root | grep -v grep | awk '{print $2}'`
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

process_id=`ps aux | grep ./alarme.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./personnes.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi
