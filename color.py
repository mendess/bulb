#!/usr/bin/env python3
from bulb_ip import B
from yeelight import Bulb, BulbException
from sys import argv, stderr
import random
import argparse

colors_dic = {
    "red": "ff0000",
    "blue": "0000ff",
    "green": "00ff00",
    "yellow": "ffff00",
    "pink": "ff1694",
    "purple": "800080",
    "fuxia": "ff00ff",
    "aqua": "00ffff",
    "orange": "FF5733",
    "turquoise": "43C6DB",
    "olive":"808000",
    "whaleblue": "342D7E",
    "forest":"43C6DB",
    "mustard":"FFDB58",
}

def change(arg, check_flow='', sleep=False):
    if (not sleep):
        B.turn_on()

    if arg in colors_dic:
        color = colors_dic[arg]
    elif arg == "random":
        color = random.choice(list(colors_dic.values()))
    else:
        color = arg.replace('#','')

    def dbg(e):
        print(e)
        return e

    if (check_flow
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
    parser = argparse.ArgumentParser()
    parser.add_argument('color')
    parser.add_argument('--sleep',action='store_true')
    parser.add_argument('--flow',action='store_true')
    args = parser.parse_args(argv[1:])
    exit(change(args.color, check_flow=(args.flow if args.flow else ''), sleep=args.sleep))
