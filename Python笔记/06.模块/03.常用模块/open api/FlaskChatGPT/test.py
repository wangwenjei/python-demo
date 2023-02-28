import requests
import json

url = 'http://127.0.0.1:5000/ChatGPT'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
# 将json类型的数据转换成字典类型的数据
# data = {"que": "豹子头林冲的外号"}

data = {"que": "林冲的外号"}

# 调用¬json.dumps()方法，将数据以json格式传递
# response = requests.post(url=url, headers=headers, data=json.dumps("\n\n你知道水浒传吗  \n\n  有哪些主要人物 \n\n 你最喜欢哪个人物 \n\n"))

# response = requests.post(url=url, headers=headers, data=json.dumps("\n\n开发工程师JD \n\n 高级的 \n\n 毕业三年以上 \n\n"))

response = requests.post(url=url, headers=headers, data=json.dumps(data))

# response = requests.post(url=url, headers=headers, data=json.dumps("开发工程师JD \n\n 高级的 \n\n 毕业三年以上 \n\n"))


page_text = response.text

print(page_text)
