#!/usr/bin/env python3
from bulb_ip import B
from yeelight import Bulb, BulbException
from sys import argv, stderr
import random
import argparse

colors_dic = {
        "chill": { "rgb": "ff0000", "ct": 1700, "bright": 80 }
}

def change(arg):
    B.turn_on()

    color = colors_dic[arg]

    r = color["rgb"][0:2]
    g = color["rgb"][2:4]
    b = color["rgb"][4:6]

    if r == '00' and g == '00' and b == '00':
        r = g = b = '01'

    B.set_rgb(int(r, 16), int(g, 16), int(b, 16))
    B.set_brightness(color["bright"])
    B.set_color_temp(color["ct"])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('color')
    args = parser.parse_args(argv[1:])
    exit(change(args.color))
