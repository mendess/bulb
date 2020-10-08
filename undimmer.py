#!/usr/bin/env python3
from time import sleep
from bulb_ip import B

B.turn_on()
for i in (range(0, 101)):
    try:
        B.set_brightness(i)
        print('good ', i)
    except BulbException as e:
        print('error', i, e)
    sleep(5)
