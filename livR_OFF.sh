#!/bin/bash
for pid in $(pidof -x livR_OFF.sh); do
    if [ $pid != $$ ]; then
        kill -9 $pid
    fi 
done
i=0
while [ $i -lt 15 ] ; do
	var=$(gatttool -b 68:9E:19:16:64:33 --char-write-req -a 0x002d -n 00000000);
	var2='Characteristic value was written successfully';
	if [ "$var" == "$var2" ]
	then
		break
	fi
i=$[$i+1]
done

