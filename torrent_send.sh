#!/bin/bash
source config.sh
sshpass -p $rpi_pass scp *.torrent pi@$rpi_ip:/home/pi/newmoviescrapeanddownload
