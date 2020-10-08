from yeelight import Bulb, BulbException, discover_bulbs
from os import remove, environ as env

IP_PATH = env['HOME'] + '/.cache/bulb_ip'

class Cache:
    @staticmethod
    def refresh_ip():
        try:
            ip = map(lambda x: x['ip'], discover_bulbs()).__next__()
        except StopIteration:
            print('No bulbs found')
            return None
        print(f'Found ip {ip}')
        with open(IP_PATH, 'w') as f:
            f.write(ip)

        return ip

    @staticmethod
    def get_ip():
        try:
            with open(IP_PATH, 'r') as f:
                ip = f.read().strip()
                print(f'Trying ip \'{ip}\'')
                return ip if ip else Cache.refresh_ip()
        except FileNotFoundError as e:
            return Cache.refresh_ip()

    @staticmethod
    def invalidate_cache():
        print("cache not invalidated because trash api")
        #remove(IP_PATH)


class BulbIp:
    def __init__(self):
        self.bulb = None

    def run(self, func, retry=True):
        bulb = self.load_bulb()
        try:
            return func(bulb)
        except BulbException as e:
            print('Failed with', e)
            if retry:
                print('Retrying...')
                Cache.invalidate_cache()
                self.bulb = None
                return self.run(func, retry=False)

    def load_bulb(self):
        if self.bulb is None:
            ip = Cache.get_ip()
            if not ip:
                ip = Cache.refresh_ip()
                if not ip:
                    print('Giving up...')
                    return None
            self.bulb = Bulb(ip)
        return self.bulb


instance = BulbIp()
def run(func):
    global instance
    try:
        return instance.run(func)
    except Exception as e:
        print('Failed with', e)

class BulbProxy:
    def __getattribute__(self, name):
        global instance
        attr = Bulb.__getattribute__(instance.load_bulb(), name)
        if hasattr(attr, '__call__'):
            def f(*args, **kwargs):
                return instance.run(lambda _: attr(*args, **kwargs))
            return f
        else:
            return attr

B = BulbProxy()
