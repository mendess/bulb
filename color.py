#!/usr/bin/env python3
from bulb_ip import B
from yeelight import Bulb, BulbException
from sys import argv, stderr

colors_dic = {

    "red": "ff0000",
    "blue": "0000ff",
    "green": "00ff00",
    "yellow": "ffff00",
    "pink": "ff1694",
    "purple": "800080",
    "fuxia": "ff00ff",
    "aqua": "00ffff",
    "orange": "FF5733"

}

if argv[1] in colors_dic:
    color = colors_dic[argv[1]]
else:
    color = argv[1].replace('#','')

def dbg(e):
    print(e)
    return e

if (len(argv) > 2
    and argv[2] == 'check_flow'
    and B.get_properties(['flowing'])['flowing'] == '1'):
    print('flowing, aborting')
    exit(0)

r = color[0:2]
g = color[2:4]
b = color[4:6]

B.set_rgb(int(r, 16), int(g, 16), int(b, 16))
# run(lambda bulb: bulb.set_rgb(int(r, 16), int(g, 16), int(b, 16)))
