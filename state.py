#!/usr/bin/env python3
from bulb_ip import B
from subprocess import Popen, PIPE

props = [
    'power',
    'bright',
    'ct',
    'rgb',
    'hue',
    'sat',
    # 'color_mode',
    'flowing',
    'delayoff',
    # 'flow_params'
    'music_on'
]
prop = B.get_properties(requested_properties=props)
for k in prop.keys():
    if k == 'rgb':
        v = (
                Popen(
                    ['color_picker'],
                    stdin=PIPE,
                    stdout=PIPE
                    )
                .communicate(input=bytes('#{:06x}'.format(int(prop[k])), 'utf-8'))[0]
                .decode('utf-8')
                .strip()
            )
    elif k == 'power':
        v = prop[k]
        v = ('\x1b[31m{}\x1b[0m' if v == 'off' else '\x1b[32m{}\x1b[0m').format(v)
    else:
        v = prop[k]
    print(f'{k}: {v}')
