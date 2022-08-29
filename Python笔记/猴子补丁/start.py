import json
import ujson


# 为功能打补丁,此时将json功能,替换为 ujson
def monkey_path_json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps


import a

if __name__ == '__main__':
    monkey_path_json()   # 不想要补丁功能,注释函数即可
    a.func()
