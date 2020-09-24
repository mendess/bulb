import bulb_ip
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

r = color[0:2]
g = color[2:4]
b = color[4:6]

bulb_ip.run(lambda bulb: bulb.set_rgb(int(r, 16), int(g, 16), int(b, 16)))
