#!/bin/python3

import bulb_ip

bulb_ip.run(lambda b: b.turn_on())
bulb_ip.run(lambda b: (b.set_hsv(0,0), b.set_brightness(100), b.set_color_temp(4700)))
