#!/usr/bin/env python3
from bulb_ip import B
from subprocess import Popen, PIPE
import shutil

def get_state(props=['power', 'bright', 'ct', 'rgb', 'hue', 'sat', 'flowing', 'delayoff', 'flow_params' 'music_on']):
    return B.get_properties(requested_properties=props)

def print_props(props):
    for k in props.keys():
        if k == 'rgb':
            v = '#{:06x}'.format(int(props[k]))
            if shutil.which('color_picker') is not None:
                v = (
                        Popen(
                            ['color_picker'],
                            stdin=PIPE,
                            stdout=PIPE
                            )
                        .communicate(input=bytes(v, 'utf-8'))[0]
                        .decode('utf-8')
                        .strip()
                    )
        elif k == 'power':
            v = props[k]
            v = ('\x1b[31m{}\x1b[0m' if v == 'off' else '\x1b[32m{}\x1b[0m').format(v)
        else:
            v = props[k]
        print(f'{k}: {v}')

if __name__ == '__main__':
    print_props(get_state())
