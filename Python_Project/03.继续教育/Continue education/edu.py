import time
from PIL import Image
import pytesseract
import requests
import os

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}


# 下载验证码图片
def input_img(image_url):
    image_url = image_url
    os.system('rm -rf ./images && mkdir ./images')  # 删除旧的图片文件
    session = requests.Session()  # 使用session是为了保证验证码的请求和登陆请求信息一致
    r = session.get(image_url, headers=headers)
    with open(r'./images/code.jpg', mode='wb') as f:
        f.write(r.content)
    print('=== 图片下载完成 ===')


# 进行二值处理
def erzhihua(image, threshold):
    image = image.convert('L')
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return image.point(table, '1')


input_img(image_url='https://cmegsb.cma.org.cn/national_project/CheckCodeImageServlet')
img = Image.open('./images/code.jpg')
img = erzhihua(img, 127)
img.show()
rc = input('输入验证码:')
rc = str(rc)

# post请求的发送（模拟登录）
login_url = 'https://www.xqb5200.com/login.php'
data = {
    "username": "2254964433",
    "password": "jason123.com",
    "checkcode": rc,
    "action": "login",
    # "submit": "%26%23160%3B%B5%C7%26%23160%3B%26%23160%3B%C2%BC%26%23160%3B"
}

# response = requests.post(url=login_url, headers=headers, data=data)
# print(response.text)
# print(response.status_code)  # 响应代码：如果返回的是200就是模拟登陆成功了
