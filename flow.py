#!/usr/bin/env python3
from bulb_ip import B
from yeelight import Flow, Bulb, flows
import argparse

def flow(flow, *args):
    B.turn_on()
    print('flowing', flow)
    try:
        method = getattr(flows, flow)
        flow = method(*args)
    except AttributeError as e:
        print(e)
        exit(1)

    B.start_flow(flow)

def list_flows():
    l = {}
    f_check = lambda x: (
            not x.startswith('_')
            and x.islower()
            and hasattr(getattr(flows, x), '__call__')
        )
    for f in filter(f_check, dir(flows)):
        l[f] = None
    return '\n'.join(l.keys())

def show_description(flow):
    return '\n'.join(
        filter(lambda x: not (':returns' in x or ':rtype' in x),
            getattr(flows, flow).__doc__.split('\n')
            )
        ).strip()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("flow", nargs='*', help="the flow method", default="random_loop")
    group.add_argument("-s", "--stop", help="stop flowing", action="store_true")
    group.add_argument("-l", "--list", help="list all flows", action="store_true")
    group.add_argument("-d", "--description",
            help="show the description of a flow", type=str)
    args = parser.parse_args()
    if args.list:
        print(list_flows())
    elif args.stop:
        B.stop_flow()
    elif args.description:
        print(show_description(args.description))
    else:
        if type(args.flow) == list:
            flow_name, args = (args.flow[0], list(map(int, args.flow[1:])))
        else:
            flow_name, args = (args.flow, [])
        flow(flow_name, *args)
