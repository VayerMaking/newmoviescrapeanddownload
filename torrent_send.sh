#!/bin/bash
source config.sh
sshpass -p $rpi_pass scp *.txt pi@$rpi_ip:/home/pi
