#!/bin/bash
process_id=`ps aux | grep ./operateur.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./c_demandes_entrees.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./c_demandes_sorties.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./c_acquittement_entrees.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./c_acquittement_sorties.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi


process_id=`ps aux | grep ./train.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./train.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./train.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./train.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./train.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./train.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./train.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./train.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./train.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi

process_id=`ps aux | grep ./train.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi


