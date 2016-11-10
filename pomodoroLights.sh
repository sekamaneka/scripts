#!/bin/bash
while true; do
	
	gatttool -b 68:9E:19:16:64:33 --char-write-req -a 0x002d -n 00000000;
	gatttool -b 68:9E:19:16:64:33 --char-write-req -a 0x002d -n ff000000;

	sleep 1500;

	gatttool -b 68:9E:19:16:64:33 --char-write-req -a 0x002d -n 000000ff;
	sleep 300;
done
