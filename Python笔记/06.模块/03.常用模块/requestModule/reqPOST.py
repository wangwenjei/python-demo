import requests
import json

# 请求链接
url = "http://127.0.0.1:5000/ai/ask"

# 请求参数
data = {"que": "水浒传说的怎样的一个故事"}

# 请求头
headers = {'Content-Type': 'application/json;charset=UTF-8'}

res = requests.post(url=url, json=data, headers=headers)
print(res.text)

"""

POST请求参数：
    url：请求URL，必填；
    data：请求参数，选填；
    json：请求参数，选填；
    **kwargs：可以传入headers，cookies等


何时用json,何时用data
    不管JSON是str还是dict，如果不指定headers种的 Content-Type，默认为application/json；
    dict为dict时，如果不指定Content-Type，默认为application/x-www-form-urlencoded，相当于普通form表单提交的形式；
    data为str时，如果不指定Content-Type，默认为application/json
    
    故POST请求具体传data还是JSON类型数据，需要根据请求头中Content-Type类型
"""
