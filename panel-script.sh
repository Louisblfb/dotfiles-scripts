#!/bin/bash

while [ 1 ]
    do
        xsetroot -name "[Music: $(playback.py | grep "Title: " | sed -e 's/Title: //')] [$(cat /sys/class/power_supply/BAT0/status): $(( `cat /sys/class/power_supply/BAT0/energy_now` * 100 / `cat /sys/class/power_supply/BAT0/energy_full` ))%] [$(date +%X)] "
        sleep 1
    done
