#!/usr/bin/env python3
from yeelight import Bulb, BulbException, Flow, RGBTransition
from time import sleep
from random import uniform
from bulb_ip import B
from sys import argv

B.turn_on()
if len(argv) > 1:
    flow = Flow(count=0, transitions= [RGBTransition(255, 0, 255, duration=1000)])
    B.start_flow(flow)
    sleep(400)
else:
    while True:
        c = int(uniform(1, 0xffffff))
        color = hex(c).replace('0x','').rjust(6,'0')
        r = color[0:2]
        g = color[2:4]
        b = color[4:6]
        try:
            B.set_rgb(int(r, 16), int(g, 16), int(b, 16))
            print('good ', r, g, b)
        except BulbException as e:
            print('error', r, g, b, e)
        sleep(2)
