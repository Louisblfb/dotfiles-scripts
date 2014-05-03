
#!/bin/bash 

while [ 1 ] 
    do 
        grep closed /proc/acpi/button/lid/LID0/state &&
        i3lock -c 000000 &&
        xbacklight -set 0
        sleep 2
    done
