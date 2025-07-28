# encoding=utf-8

from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd
import base64
import urllib
import requests
import ast
import time
import os


class JSCME:
    def __init__(self):
        self.CmeCode = [{"pcode": "01-", "code": "01-01-", "name": "组织胚胎学"},
                        {"pcode": "01-", "code": "01-02-", "name": "解剖学"},
                        {"pcode": "01-", "code": "01-03-", "name": "遗传学"},
                        {"pcode": "01-", "code": "01-04-", "name": "病理学"},
                        {"pcode": "01-", "code": "01-05-", "name": "寄生虫学"},
                        {"pcode": "01-", "code": "01-06-", "name": "微生物学"},
                        {"pcode": "02-", "code": "02-01-", "name": "生理学"},
                        {"pcode": "02-", "code": "02-02-", "name": "生物化学"},
                        {"pcode": "02-", "code": "02-03-", "name": "生物物理学"},
                        {"pcode": "02-", "code": "02-04-", "name": "药理学"},
                        {"pcode": "02-", "code": "02-05-", "name": "细胞生物学"},
                        {"pcode": "02-", "code": "02-06-", "name": "病生理学"},
                        {"pcode": "02-", "code": "02-07-", "name": "免疫学"},
                        {"pcode": "02-", "code": "02-08-", "name": "基础医学其他学科"},
                        {"pcode": "03-", "code": "03-01-", "name": "心血管病学"},
                        {"pcode": "03-", "code": "03-02-", "name": "呼吸病学"},
                        {"pcode": "03-", "code": "03-03-", "name": "胃肠病学"},
                        {"pcode": "03-", "code": "03-04-", "name": "血液病学"},
                        {"pcode": "03-", "code": "03-05-", "name": "肾脏病学"},
                        {"pcode": "03-", "code": "03-06-", "name": "内分泌学"},
                        {"pcode": "03-", "code": "03-07-", "name": "神经内科学"},
                        {"pcode": "03-", "code": "03-08-", "name": "感染病学"},
                        {"pcode": "03-", "code": "03-09-", "name": "精神卫生学"},
                        {"pcode": "03-", "code": "03-10-", "name": "老年医学"},
                        {"pcode": "03-", "code": "03-11-", "name": "内科学其他学科"},
                        {"pcode": "04-", "code": "04-01-", "name": "普通外科学"},
                        {"pcode": "04-", "code": "04-02-", "name": "心胸外科学"},
                        {"pcode": "04-", "code": "04-03-", "name": "烧伤外科学"},
                        {"pcode": "04-", "code": "04-04-", "name": "神经外科学"},
                        {"pcode": "04-", "code": "04-05-", "name": "泌尿外科学"},
                        {"pcode": "04-", "code": "04-06-", "name": "显微外科学"},
                        {"pcode": "04-", "code": "04-07-", "name": "骨外科学"},
                        {"pcode": "04-", "code": "04-08-", "name": "肿瘤外科学"},
                        {"pcode": "04-", "code": "04-09-", "name": "颅脑外科学"},
                        {"pcode": "04-", "code": "04-10-", "name": "整形、器官移植外科学"},
                        {"pcode": "04-", "code": "04-11-", "name": "外科学其他学科"},
                        {"pcode": "05-", "code": "05-01-", "name": "妇科学"},
                        {"pcode": "05-", "code": "05-02-", "name": "产科学"},
                        {"pcode": "05-", "code": "05-03", "name": "妇产科学其他学科"},
                        {"pcode": "06-", "code": "06-01-", "name": "儿科内科学"},
                        {"pcode": "06-", "code": "06-02-", "name": "儿科外科学"},
                        {"pcode": "06-", "code": "06-03-", "name": "新生儿科学"},
                        {"pcode": "06-", "code": "06-04-", "name": "儿科学其他学科"},
                        {"pcode": "07-", "code": "07-01-", "name": "耳鼻咽喉科学"},
                        {"pcode": "07-", "code": "07-02-", "name": "眼科学"},
                        {"pcode": "08-", "code": "08-01-", "name": "口腔内科学"},
                        {"pcode": "08-", "code": "08-02-", "name": "口腔外科学"},
                        {"pcode": "08-", "code": "08-03-", "name": "口腔正畸学"},
                        {"pcode": "08-", "code": "08-04-", "name": "口腔修复学"},
                        {"pcode": "08-", "code": "08-05-", "name": "口腔学其他学科"},
                        {"pcode": "09-", "code": "09-01-", "name": "放射诊断学"},
                        {"pcode": "09-", "code": "09-02-", "name": "超声诊断学"},
                        {"pcode": "09-", "code": "09-03-", "name": "放射肿瘤学"},
                        {"pcode": "09-", "code": "09-04-", "name": "影像医学其他学科"},
                        {"pcode": "12-", "code": "12-01-", "name": "劳动卫生与环境卫生学"},
                        {"pcode": "12-", "code": "12-02-", "name": "营养与食品卫生学"},
                        {"pcode": "12-", "code": "12-03-", "name": "儿少卫生与妇幼卫生学"},
                        {"pcode": "12-", "code": "12-04-", "name": "卫生毒理学"},
                        {"pcode": "12-", "code": "12-05-", "name": "统计流行病学"},
                        {"pcode": "12-", "code": "12-06-", "name": "卫生检验学"},
                        {"pcode": "12-", "code": "12-07-", "name": "公共卫生与预防医学其他学科"},
                        {"pcode": "13-", "code": "13-01-", "name": "临床药学和临床药理学"},
                        {"pcode": "13-", "code": "13-02-", "name": "药剂学"},
                        {"pcode": "13-", "code": "13-03-", "name": "药物分析学"},
                        {"pcode": "13-", "code": "13-04-", "name": "药事管理学"},
                        {"pcode": "13-", "code": "13-05-", "name": "药学其他学科"},
                        {"pcode": "14-", "code": "14-01-", "name": "内科护理学"},
                        {"pcode": "14-", "code": "14-02-", "name": "外科护理学"},
                        {"pcode": "14-", "code": "14-03-", "name": "妇产科护理学"},
                        {"pcode": "14-", "code": "14-04-", "name": "儿科护理学"},
                        {"pcode": "14-", "code": "14-05-", "name": "护理其他学科"},
                        {"pcode": "15-", "code": "15-01-", "name": "医学教育"},
                        {"pcode": "15-", "code": "15-02-", "name": "卫生管理"},
                        {"pcode": "23-", "code": "23-01-", "name": "医学心理学"},
                        {"pcode": "23-", "code": "23-02-", "name": "临床与咨询心理学"},
                        {"pcode": "23-", "code": "23-03-", "name": "心理学其他学科"},
                        {"pcode": "24-", "code": "24-01-", "name": "医学人文与医德医风"},
                        {"pcode": "24-", "code": "24-02-", "name": "医患沟通"},
                        {"pcode": "24-", "code": "24-03-", "name": "科研伦理"},
                        {"pcode": "24-", "code": "24-04-", "name": "卫生法规"}]

        self.CmeCode_test = [{"pcode": "01-", "code": "01-01-", "name": "组织胚胎学"},
                             {"pcode": "01-", "code": "01-02-", "name": "解剖学"},
                             {"pcode": "01-", "code": "01-03-", "name": "遗传学"},
                             {"pcode": "01-", "code": "01-04-", "name": "病理学"},
                             {"pcode": "01-", "code": "01-05-", "name": "寄生虫学"}, ]

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

    def get_cme_project(self, url, year, authcode, cookie, *args, **kwargs) -> list:
        """
        循环二级三级学科字典获取不同CME项目页
        :param url: 地址
        :param year: 年度
        :param authcode: 验证码
        :param cookie: 获取验证码返回的COOKIE
        :param args:
        :param kwargs:
        :return:
        """
        table_metadata_all = []
        table_metadata_header = ['项目编号', '项目名称', '举办日期', '举办地点', '主办单位', '负责人', '学分', '人数', '公布类型', '项目性质']
        table_metadata_all.append(table_metadata_header)
        for i in self.CmeCode:
            xk2 = i.get('pcode')
            xk3 = i.get('code')

            # print(i)
            print({"xk2": xk2, "xk3": xk3})

            # 循环获取不同参数的HTML页面表格
            html = cme._get_html(url=url, year=year, CMEScode2=xk2, CMEScode3=xk3, authcode=authcode, cookie=cookie)
            table_data = self._table_data(html)
            # print(table_data)

            for i in table_data:
                i.pop(0)
                table_metadata_all.append(i)
            time.sleep(5)

        return table_metadata_all

    def _get_html(self, url, year, CMEScode2, CMEScode3, authcode, cookie, *args, **kwargs) -> str:
        """
        返回查询到的项目页面
        :param url: 地址
        :param year: 年度
        :param CMEScode2: 二级学科
        :param CMEScode3: 三级学科
        :param authcode: 验证码
        :param cookie: 获取验证码返回的COOKIE
        :param args:
        :param kwargs:
        :return: HTML str
        """
        headers = {'User-Agent': 'Mozilla/5.0 (Windows',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                   'cookie': cookie,
                   'Referer': 'https://cme.jsma.net.cn/Web/ProjectSearch'}

        url = f"{url}?year={year}&CMEScode2={CMEScode2}&CMEScode3={CMEScode3}&authcode={authcode}"
        print(url)
        response = requests.get(url, headers=headers)

        # print(response.text)
        cme_html = response.text
        return cme_html

    def _table_data(self, html, *args, **kwargs) -> list:
        """
        对传入的HTML页面处理,返回页面中第一个表格中数据
        :param html: HTML页面
        :return: list
        """
        soup = BeautifulSoup(html, 'lxml')  # 使用BeautifulSoup解析HTML
        tables = soup.find_all('table')  # 查找所有的<table>标签
        table = tables[0]  # 这里我们只关心页面的第一个表格
        rows = table.find_all('tr')  # 提取表格的行和列
        table_data = []  # 初始化一个列表来存储表格数据
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip().replace('\xa0', '') for ele in cols]
            table_data.append([ele for ele in cols if ele])  # 过滤掉空值

        table_data.pop(0)
        # print(table_data)
        # 打印表格数据
        # for row in table_data:
        #     print(row)
        return table_data


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


class metadataToFile:

    def toExcel(self, tabledata):
        """

        :param tabledata:
        :return:
        """
        # 创建一个新的工作簿
        wb = Workbook()

        # # 选择默认的工作表
        ws = wb.active

        # 遍历列表，将数据写入工作表
        for row in tabledata:
            ws.append(row)  # append()方法会直接将一行数据添加到工作表的末尾

        # 保存工作簿到文件
        file_name = '江苏CME_%s.xlsx' % (time.strftime('%Y-%m-%d'))
        wb.save(file_name)
        print("数据已成功写入Excel文件。")
        return file_name

    def to_inster_sql2(self, excel_file=None, sql_file_name=None, *args, **kwargs):
        """
        将Excel内数据格式化为INSERT SQL
        :param excel_file: Excel file path
        :param sql_file_name: SQL file path
        :param args:
        :param kwargs:
        :return: SQL file path
        """

        if excel_file is None:
            excel_file = '非基地_%s.xlsx' % (time.strftime('%Y-%m-%d'))

        if sql_file_name is None:
            sql_file_name = '非基地_IN SERT_%s.sql' % (time.strftime('%Y-%m-%d'))

        df = pd.read_excel(excel_file)
        now_rows = df.shape[0]  # 获取行数
        df.fillna("null", inplace=True)  # 将空字符给赋指定默认值NULL

        table_head = list(df.columns.values)  # 获取表头

        with open(sql_file_name, mode='a', encoding='utf-8') as f:
            # sql = "insert into edu_record (projectId, project_num, project_name, company,leading_name, tel, startdate, enddate, date_num, address, credit, crowd, person_num, remark ) values"

            # 依据Excel表头依次添加需要插入数据的表字段
            # table_head.pop(0)
            # insert_fields = str(tuple(table_head))  #
            insert_fields = str(tuple(table_head)).replace('\'', '')  #

            sql = "insert into js_cme {insert_fields} values".format(insert_fields=insert_fields)
            f.write(sql)

            for i in range(now_rows):
                # 去除索引列
                data = list(df.loc[i].values)
                # data.pop(0)

                data = str(tuple(data)) + ','
                # print(data)
                f.write(data)

        return sql_file_name


if __name__ == '__main__':
    cme = JSCME()

    # """1.得到验证码和对应cookie"""
    # # 下载验证码图片和获取对应验证码cookie
    # captcha_obj = cme.save_captcha(url='https://cme.jsma.net.cn/Home/ValidateCode')
    # cookie = captcha_obj.get('cookie')  # 获取验证码cookie
    #
    # """2.百度OCR获取验证码字符串"""
    # code_obj = OcrCode()
    # code_obj = code_obj.get_captcha_code(captcha_code_path='captcha.jpg')
    # code = code_obj.get('words_result')[0].get('words')  # 百度OCR获取验证码字符串
    #
    # """3.获取表格数据"""
    # url = 'https://cme.jsma.net.cn/Web/ProjectSearch'
    # print(f'cookie>>>>:{cookie}')
    # table_all = cme.get_cme_project(url=url, year=2025, authcode=code, cookie=cookie)

    """4.将数据写入文件"""
    to_excel_obj = metadataToFile()
    # 写入Excel
    # to_excel_obj.toExcel(tabledata=table_all)

    # EXCEL转化为INSERT SQL
    # to_excel_obj.to_inster_sql2(excel_file='./江苏CME_2025-07-23.xlsx', sql_file_name='江苏CME_2025-07-23.sql')
    to_excel_obj.to_inster_sql2(excel_file='20250227162729_66612.xlsx', sql_file_name='江苏_20250227162729_6661.sql')
    # to_excel_obj.to_inster_sql2(excel_file='./江苏CME去重后 2.xlsx', sql_file_name='江苏去重CME_2024-09-23.sql')
