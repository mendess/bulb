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

def change(arg, check_flow=''):
    B.turn_on();
    if arg in colors_dic:
        color = colors_dic[arg]
    else:
        color = arg.replace('#','')

    def dbg(e):
        print(e)
        return e

    if (check_flow == 'check_flow'
        and B.get_properties(['flowing'])['flowing'] == '1'):
        print('flowing, aborting')
        return 0

    r = color[0:2]
    g = color[2:4]
    b = color[4:6]

    if r == '00' and g == '00' and b == '00':
        r = g = b = '01'

    B.set_rgb(int(r, 16), int(g, 16), int(b, 16))

if __name__ == '__main__':
    exit(change(argv[1], check_flow=(argv[2] if len(argv) > 2 else '')))
