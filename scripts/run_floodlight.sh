#!/usr/bin/env bash

progname=floodlight

logfile=/var/log/$progname.log
pidfile=/var/run/$progname.pid

cd /floodlight/
nohup java -Dpidfile=$pidfile -jar target/floodlight.jar </dev/null > $logfile 2>&1 &
