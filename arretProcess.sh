#!/bin/bash
process_id=`ps aux | grep ./master.py | grep -v root | grep -v grep | awk '{print $2}'`
if [ $? -eq "0" ]; then
kill -9 $process_id
fi
