#!/usr/bin/env python3
from bulb_ip import B

if __name__ == '__main__':
    state = B.get_properties(requested_properties=['power'])["power"]
    if state == "on":
        B.turn_off();
    else:
        B.turn_on();
