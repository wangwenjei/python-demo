import json
import ujson


def monkey_path_json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps


import a

if __name__ == '__main__':
    monkey_path_json()
    a.func()
