#!/usr/bin/env python3

from yeelight import RGBTransition, Flow
from bulb_ip import B
from state import get_state

color = get_state(props=['rgb'])['rgb']

r = color[0:2]
g = color[2:4]
b = color[4:6]

pink = RGBTransition(0xff, 0x16, 0x94, 500, 100)
pink = RGBTransition(0xff, 0x00, 0xff, 500, 100)
current = RGBTransition(int(r, 16), int(g, 16), int(b, 16), 500, 100)
transitions = [pink if i % 2 == 0 else current for i in range(9)]

flow = Flow(
    count=1,
    transitions=transitions
)

B.start_flow(flow)

