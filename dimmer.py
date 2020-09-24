from time import sleep
from sys import argv
from bulb_ip import run

sleep(float(argv[1]))
for i in reversed(range(0, 101, 2)):
    try:
        run(lambda bulb: bulb.set_brightness(i))
        print('good ', i)
    except BulbException as e:
        print('error', i, e)
    sleep(5)

while True:
    try:
        run(lambda bulb: bulb.turn_off())
        break
    except:
        pass
