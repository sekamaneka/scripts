import sys
import os
import subprocess

brightness = int(sys.argv[1])#0-255
brightness = hex(brightness)[2:4]
color = int(sys.argv[2])#its int(BBGGRR)
color = hex(color)[2:]
address = sys.argv[3]

a = "success" 
for i in range(10):
  return_v = (subprocess.Popen(["sudo", "gatttool", "-b", address, "--char-write-req", "-a", "0x002d", "-n",(color+brightness) ], stdout=subprocess.PIPE).stdout.read())
  if a in return_v:
    print("success")
    break
