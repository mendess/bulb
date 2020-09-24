from yeelight import Bulb, BulbException
from time import sleep

bulb = Bulb("192.168.1.7")
bulb.turn_on()
for i in (range(0, 101)):
    try:
        bulb.set_brightness(i)
        print('good ', i)
    except BulbException as e:
        print('error', i, e)
    sleep(5)
