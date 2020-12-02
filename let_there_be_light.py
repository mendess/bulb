#!/usr/bin/env python3

from bulb_ip import B
from sys import argv

if len(argv) > 1:
    temp=3400
    brig=77
else:
    temp=4700
    brig=100

B.turn_on()
B.set_hsv(0,0)
B.set_brightness(brig)
B.set_color_temp(temp)
