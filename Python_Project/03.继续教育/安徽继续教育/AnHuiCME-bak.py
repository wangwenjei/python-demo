import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd
import time


class AnHuiCme:
    def get_cme_project(self, page_max_id: int, page_size: int, *args, **kwargs) -> list:
        table_metadata_all = []
        table_metadata_header = ['项目编号', '项目名称', '申办单位', '项目负责人', '举办期限起止日期',
                                 '举办地点', '授予学分', '教学对象', '拟招生人数', '备注']
        table_metadata_all.append(table_metadata_header)

        for i in range(1, page_max_id + 1):

            print({'当前页:': i, '每页最大条数:': page_size})

            html = self._get_html(page_id=i, page_size=page_size)
            table_data = self._table_data(html=html)
            print(table_data)

            for d in table_data:
                table_metadata_all.append(d)
            time.sleep(5)
        return table_metadata_all

    def _get_html(self, page_id: int, page_size: int, *args, **kwargs) -> str:
        """
        获取安徽CME页面数据
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

            # print('-' * 30)
            # bt = row.find_all('button')
            # print(bt)
            # print('-' * 30)

            cols = [ele.text.strip().replace('\xa0', '') for ele in cols]

            print(cols)

            if len(cols) != 0:  # 判断列表是否为空值
                cols.pop(-1)  # 去除最后一列表格数据(查看)
                table_data.append([ele for ele in cols if ele])  # 过滤掉空值

        # print(table_data)
        # 打印表格数据
        # for row in table_data:
        #     print(row)
        return table_data


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
    """1.获取表格数据"""
    cme_data_obj = AnHuiCme()
    table_all = cme_data_obj.get_cme_project(page_size=2, page_max_id=1)

    # """2.导入Excel"""
    # to_excel_obj = metadataToFile()
    # to_excel_obj.toExcel(tabledata=table_all)
