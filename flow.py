from yeelight import Flow, Bulb, transitions
from bulb_ip import run
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("flow", nargs='?', help="the flow method", default="lsd")
group.add_argument("-s", "--stop", help="stop flowing", action="store_true")
group.add_argument("-l", "--list", help="list all flows", action="store_true")
parser.add_argument("-c", "--count", help="the loop count, 0 for forever, default 1", type=int, default=1)
args = parser.parse_args()

if args.list:
    for f in filter(lambda x: '_' not in x and x.islower(), dir(transitions)):
        print(f)
elif args.stop:
    run(lambda b: b.stop_flow())
else:
    run(lambda b: b.turn_on())
    try:
        method = getattr(transitions, args.flow)
        print(method())
        f = Flow(count=args.count, transitions=method())
        run(lambda b: b.start_flow(f))
    except AttributeError as e:
        print(e)

