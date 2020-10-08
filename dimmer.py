#!/usr/bin/env python3
from time import sleep
from sys import argv
from bulb_ip import B

sleep(float(argv[1]))
for i in reversed(range(0, 101, 2)):
    try:
        B.set_brightness(i)
        print('good ', i)
    except BulbException as e:
        print('error', i, e)
    sleep(5)

while True:
    try:
        B.turn_off()
        break
    except:
        pass
