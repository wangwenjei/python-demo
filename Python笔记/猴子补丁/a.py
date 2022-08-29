import json
import ujson

def func():
    print(json.dumps)
    print(ujson.dumps)

    print(json.__name__)
    print(ujson.__name__)