#!/usr/bin/env python3

from yeelight import RGBTransition, Flow
from bulb_ip import B
from state import get_state

color = int(get_state(props=['rgb'])['rgb'])
b = color & 0xff
color >>= 8
g = color & 0xff
color >>= 8
r = color & 0xff


pink = RGBTransition(0xff, 0x16, 0x94, 500, 100)
pink = RGBTransition(0xff, 0x00, 0xff, 500, 100)
current = RGBTransition(r, g, b, 500, 100)
transitions = [pink if i % 2 == 0 else current for i in range(9)]

flow = Flow(
    count=1,
    transitions=transitions
)

B.start_flow(flow)

