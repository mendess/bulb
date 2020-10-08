#!/usr/bin/env python3
import bulb_ip

print(''.join(
    map(chr, [116, 104, 97, 110, 107, 115, 32, 108, 111, 118, 101, 32, 60, 51]))
)
bulb_ip.B.turn_off()
