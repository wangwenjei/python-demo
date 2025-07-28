from openpyxl import Workbook
import pandas as pd
import time
import requests
import os
import base64

from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd
import base64
import urllib
import requests
import ast
import time
import os


class GDCME:
    def __init__(self):
        ...

    def save_captcha(self, url, file_path=None) -> dict:
        """
        从指定URL下载验证码图片并保存到本地文件

        :param url: 验证码图片的URL
        :param file_path: 保存验证码图片的本地文件路径
        :return: {验证码图片路径,此次验证码cookie}
        """

        if file_path is None:
            file_path = 'captcha.jpg'

        try:
            # 发送GET请求
            response = requests.get(url)

            # 确保请求成功
            response.raise_for_status()

            # 将响应内容（二进制数据）写入文件
            with open(file_path, 'wb') as file:
                file.write(response.content)

            print(f"验证码图片已保存到 {file_path}")
            print(f"cookie: {response.headers.get('Set-Cookie')}")

            return {"captcha_file_path": file_path, "cookie": response.headers.get('Set-Cookie')}

        except requests.RequestException as e:
            print(f"请求验证码图片时发生错误: {e}")

    def get_cme_project(self, url, cookie) -> str:
        """
        返回查询到的项目页面
        """

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Referer': 'https://gdcme.wsglw.net/PROJECT/publiced_list1.aspx',
                   'cookie': cookie
                   }

        #  'cookie': 'ASP.NET_SessionId=iepyoyucjgzslp1kzddhkgxk; correctCheckCode=32129'
        data = {
            "ActionName": "GetPublicProjectList",
            "regionId": "ec0c96da-9104-4edd-aeed-a95901004666",
            "subjectType": 1,
            "projectyear": 2025,
            "iiSubjectCode": "01",
            "iiiSubjectCode": "0101",
            "public_batch": -1,
            "PageSize": 50,
            "PageIndex": 1,

        }

        # print(url)

        response = requests.post(url, headers=headers, data=data)

        print(response.text)
        # cme_html = response.text
        # return cme_html


class OcrCode:
    def __init__(self):
        self.API_KEY = os.getenv('wyBaiDuAK')
        self.SECRET_KEY = os.getenv('wyBaiDuSK')

    def get_access_token(self):
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        """
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": self.API_KEY, "client_secret": self.SECRET_KEY}
        return str(requests.post(url, params=params).json().get("access_token"))

    def _get_file_content_as_base64(self, path, urlencoded=False):
        """
        获取文件base64编码
        :param path: 文件路径
        :param urlencoded: 是否对结果进行urlencoded
        :return: base64编码信息
        """
        with open(path, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf8")
            if urlencoded:
                content = urllib.parse.quote_plus(content)
        return content

    def get_captcha_code(self, captcha_code_path):
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + self.get_access_token()
        # 获取图片base64后格式
        image_base64 = self._get_file_content_as_base64(path=captcha_code_path, urlencoded=True)

        payload = (
            f'image={image_base64}'
            '&detect_direction=false'
            '&paragraph=false'
            '&probability=false'
            '&multidirectional_recognize=false')

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # print(response.text)
        c = response.text

        # 将返回的str结果转为dict
        # 如果使用JSON格式字符串，需要先转换为Python字典字面量格式，例如使用双引号替换单引号
        dict_str_py = c.replace("'", '"')
        # 使用ast.literal_eval()转换
        code_obj = ast.literal_eval(dict_str_py)

        return code_obj


if __name__ == '__main__':
    cme = GDCME()

    """1.得到验证码和对应cookie"""
    # 下载验证码图片和获取对应验证码cookie
    captcha_obj = cme.save_captcha(url='http://gdcme.wsglw.net/CheckCode.aspx')
    cookie = captcha_obj.get('cookie')  # 获取验证码cookie

    """2.百度OCR获取验证码字符串"""
    code_obj = OcrCode()
    code_obj = code_obj.get_captcha_code(captcha_code_path='captcha.jpg')
    code = code_obj.get('words_result')[0].get('words')  # 百度OCR获取验证码字符串
    print(f'code:{code}')

    """3.获取表格数据"""
    # url = "http://gdcme.wsglw.net/do/Sys/Login.do"
    url = "http://gdcme.wsglw.net/PROJECT/publiced_list1.aspx"
    url = "http://gdcme.wsglw.net/GetPublicProjectList"
    table_all = cme.get_cme_project(url=url, cookie=cookie)

    # r = requests.get('https://gdcme.wsglw.net/CheckCode.aspx')
    # print(r)
