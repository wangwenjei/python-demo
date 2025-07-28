import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd
import time
import pymysql
import os


class AnHuiCme:

    def get_cme_project(self, page_max_id: int, page_size: int, *args, **kwargs) -> list:
        """

        :param page_max_id: 每页最大数据
        :param page_size: 页数
        :param args:
        :param kwargs:
        :return:
        """
        table_metadata_all = []
        table_metadata_header = ['项目编号', '项目名称', '申办单位', '项目负责人', '举办开始时间', '举办结束时间', '举办天数', '举办地点', '授予学分', '教学对象', '拟招生人数', '备注', '主要教师列表']
        table_metadata_all.append(table_metadata_header)

        for i in range(1, page_max_id + 1):

            print({'当前页:': i, '每页最大条数:': page_size})

            html = self._get_html(page_id=i, page_size=page_size)
            table_data = self._table_data(html=html)
            # print(table_data)

            for d in table_data:
                table_metadata_all.append(d)
            time.sleep(5)
        return table_metadata_all

    # 获取安徽CME页面数据
    def _get_html(self, page_id: int, page_size: int, *args, **kwargs) -> str:
        """
        :param PageID: 页码ID
        :param PageSize: 每页展示条数
        :param args:
        :param kwargs:
        :return:
        """

        headers = {'User-Agent': 'Mozilla/5.0 (Windows',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                   'Referer': 'https://cme.jsma.net.cn/Web/ProjectSearch'}

        # url = f"http://ahcme.haoyisheng.com/hefei_project/projectGongbuList.do?d-1342871-p={page_id}&beian=&orderBy=subject&pici=&parentSubjectId=&pageSize={page_size}&sdanwei=&type=&orgId=9&gongbuCode=&gongbu=3&projectLevel=2&xmanager=&name=&subjectId=&scode=&year=2024"
        url = f"http://ahcme.haoyisheng.com/hefei_project/projectGongbuList.do?d-1342871-p={page_id}&beian=&orderBy=subject&pici=&parentSubjectId=&pageSize={page_size}&sdanwei=&type=&orgId=9&gongbuCode=&gongbu=3&projectLevel=2&xmanager=&name=&subjectId=&scode=&year=2025"

        print(url)
        response = requests.get(url, headers=headers)

        # print(response.text)
        cme_html = response.text
        return cme_html

    # 对传入的HTML页面中,返回页面中第一个表格数据进行处理
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

            bt = row.find_all('button')
            cols = [ele.text.strip().replace('\xa0', '') for ele in cols]

            if len(cols) != 0:  # 判断列表是否为空值

                cols.pop(-1)  # 去除最后一列表格数据(查看)

                "1.获取项目对应讲师列表"
                bt_projectid = bt[0].get('projectid')  # 获取查看按钮 projectid 值
                teacher_table_data = str(self.__get_project_teachers(bt_projectid))
                cols.append(teacher_table_data)

                "2.拆分起始日期与举办天数"
                startdate = cols[4].rsplit('\r')[0].rsplit('-', 3)[0]
                enddate = cols[4].rsplit('\r')[0].split('-', 3)[-1]
                date_num = cols[4].rsplit('\r\n\t\t')[1]

                cols.pop(4)
                cols.insert(4, startdate)
                cols.insert(5, enddate)
                cols.insert(6, date_num)

                "3.查询负责人手机号"

                print(cols)
                "写入列表 并 过滤掉空值,给默认字符null"
                default_string = 'null'
                table_data.append([ele if ele else default_string for ele in cols])

        # 打印表格数据
        # for row in table_data:
        #     print(row)
        # print(table_data)
        return table_data

    # 获取项目讲师信息
    def __get_project_teachers(self, bt_projectid, *args, **kwargs):
        """
        bt_projectid: 查看button projectId
        :return:
        """
        URL = f'http://ahcme.haoyisheng.com/hefei_project/projectTeacherList.do?requestType=PRINT&id={bt_projectid}'
        response = requests.get(URL)
        teacher_html = response.text
        soup = BeautifulSoup(teacher_html, 'lxml')
        rows = soup.find_all('tr')
        rows.pop(0)
        teacher_table_data = []
        for row in rows:
            "1.获取列表信息"
            cols = row.find_all('td')
            cols = [ele.text.strip().replace('\xa0', '') for ele in cols]

            "2.通过讲师信息,查询对应教师手机号"
            # if bt_projectid is not None:
            #     teacher_name = cols[0]
            #     teacher_phone = self.__get_teacher_phone(teacher_name)
            #     cols.append(teacher_phone)
            #     teacher_table_data.append(cols)

        return teacher_table_data

    # 依据讲师姓名于现有库查询手机号
    def __get_teacher_phone(self, teacherName, *args, **kwargs):
        """
        teacherName: 讲师姓名
        :return: phone
        """
        ip = os.getenv('prod_project_MySQLIP')
        pwd = os.getenv('prod_project_PWD')
        conn = pymysql.connect(host=ip, port=3306, user='root', passwd=pwd, db='prod_project', charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = conn.cursor()

        sql = f"SELECT `tel`  FROM `edu_record` WHERE  `leading_name`='{teacherName}'  ORDER BY edu_project_id desc LIMIT 1"
        cursor.execute(sql)
        data = cursor.fetchone()

        if data is None:
            teacher_phone = 'null'

        if data is not None:
            teacher_phone = data[0]

        return teacher_phone


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
        file_name = '安徽CME_%s.xlsx' % (time.strftime('%Y-%m-%d'))
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
            excel_file = '安徽CME_%s.xlsx' % (time.strftime('%Y-%m-%d'))

        if sql_file_name is None:
            sql_file_name = '安徽CME_INSERT_%s.sql' % (time.strftime('%Y-%m-%d'))

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

        print('数据写入到SQL')
        return sql_file_name


if __name__ == '__main__':
    # """1.获取表格数据"""
    cme_data_obj = AnHuiCme()
    # # table_all = cme_data_obj.get_cme_project(page_size=365, page_max_id=1)
    table_all = cme_data_obj.get_cme_project(page_size=10, page_max_id=5)

    """2.导入Excel"""
    # to_excel_obj = metadataToFile()
    # to_excel_obj.toExcel(tabledata=table_all)
    # to_excel_obj.to_inster_sql2(excel_file='安徽CME_2025-07-23.xlsx', sql_file_name='安徽CME_INSERT_2025-07-23.sql')
