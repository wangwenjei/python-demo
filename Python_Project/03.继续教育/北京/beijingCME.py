import time
import requests
from bs4 import BeautifulSoup

from Python_Project.utils.project_utils.toExcelSQL import metadataToFile


class Cme:
    def __init__(self):
        ...

    def get_cme_project(self, page_max_id: int, page_size: int, *args, **kwargs) -> list:
        """
        :param page_max_id: 每页最大数据
        :param page_size: 页数
        :param args:
        :param kwargs:
        :return:
        """
        table_metadata_all = []
        table_metadata_header = ['项目编号', '项目名称', '申办单位', '项目负责人', '负责人电话', '举办开始时间', '举办结束时间', '举办天数', '举办地点', '授予学分', '教学对象', '拟招生人数', '备注', 'batch_number']
        table_metadata_all.append(table_metadata_header)

        for i in range(1, page_max_id + 1):
            print({'当前页:': i, '每页最大条数:': page_size})

            html = self._get_html(page_id=i, page_size=page_size)
            table_data = self._table_data(html=html)
            print(table_data)

            for d in table_data:
                table_metadata_all.append(d)

            time.sleep(20)
        return table_metadata_all

    # 获取CME页面原始HTML
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
                   'Referer': 'http://www.xm.cqwsjsw.com/chongqing_project/projectGongbuList.do'}

        year = 2025
        url = (f'https://bjcme.haoyisheng.com/beijing_project/projectGongbuList.do?'
               f'd-1342871-p={page_id}&beian=&orderBy=subject&pici=&pageSize={page_size}&'
               f'parentSubjectId=&infectious=&sdanwei=&type=1&projectCategory=&gongbuCode=&gongbu=3&'
               f'xmanager=&mutual=&name=&subjectId=&scode=&year={year}')

        print(url)
        response = requests.get(url, headers=headers)
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
            cols = [ele.text.strip().replace('\xa0', '') for ele in cols]

            if len(cols) != 0:  # 判断列表是否为空值

                "1. 去除最后一列表格数据(查看)"
                cols.pop(-1)

                "2.去除学分字段分字"
                credit = cols[7].rsplit('分')[0]
                cols.pop(7)
                cols.insert(7, credit)

                "3.拆分起始日期与举办天数"
                startdate = cols[5].rsplit('\r')[0].rsplit('-', 3)[0]
                enddate = cols[5].rsplit('\r')[0].split('-', 3)[-1]
                date_num = cols[5].rsplit('\r\n\t\t')[1].rsplit('天')[0]

                cols.pop(5)
                cols.insert(5, startdate)
                cols.insert(6, enddate)
                cols.insert(7, date_num)

                "4. 批次号"
                cols.append('2025-01（京）')

                "5.写入列表 并 过滤掉空值,给默认字符null"
                default_string = 'null'
                table_data.append([ele if ele else default_string for ele in cols])

                # print(cols)

        return table_data


if __name__ == '__main__':
    """1.获取表格数据"""
    cme_data_obj = Cme()
    table_all = cme_data_obj.get_cme_project(page_size=100, page_max_id=19)
    # table_all = cme_data_obj.get_cme_project(page_size=10, page_max_id=1)

    """2.导入Excel"""
    to_excel_obj = metadataToFile()
    excel_filename = '北京CME_%s.xlsx' % (time.strftime('%Y-%m-%d'))
    sql_filename = '北京CME_INSERT_%s.sql' % (time.strftime('%Y-%m-%d'))

    """2.1 写入EXCEL"""
    to_excel_obj.toExcel(tabledata=table_all, filename=excel_filename)

    """2.2将EXCEL数据转为可执行SQL"""
    to_excel_obj.to_inster_sql2(excel_file=excel_filename, sql_file_name=sql_filename)
