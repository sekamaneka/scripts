#!/bin/bash
for pid in $(pidof -x bedR_ON.sh); do
    if [ $pid != $$ ]; then
        kill -9 $pid
    fi 
done
i=0
while [ $i -lt 15 ] ; do
	var=$(gatttool -b E0:E5:CF:A0:06:4F --char-write-req -a 0x002d -n 000000ff);

	var2='Characteristic value was written successfully';
	if [ "$var" == "$var2" ]
	then
		break
	fi
i=$[$i+1]
done

