import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd
import time
import pymysql
import os
import math


class ShangHaiCME:
    def __init__(self):
        """
        projectNumber: 项目编号
        name: 项目名称
        projectTypeStr 项目类型
        organizationName 主办单位
        managerName  负责人
        otherApplyOrganizationPhone  负责人电话

        otherHoldStarDate 举办开始日期
        otherHoldEndDate  举办结束日期
        otherHoldDayNumber 举办天数
        otherHoldAddress  举办地点
        otherTeachObject  教学对象
        otherPlanCredit  授予学分
        otherPlanStudentNumber  招生人数

        id  查看授课教师ID
        """

    def get_shanghai_cme(self, year, total, rows=20):
        # Excel 标题
        table_metadata_header = ['项目编号', '项目名称', '项目类型', '主办单位', '负责人', '负责人电话',
                                 '举办开始日期', '举办结束日期', '举办天数', '举办地点',
                                 '教学对象', '授予学分', '招生人数', '授课教师信息']

        # 全数据
        table_metadata_data_all = []
        table_metadata_data_all.append(table_metadata_header)

        page = math.ceil(total / rows)  # 向上取整

        for page in range(1, page + 1):
            data = {"year": year, "page": page, "rows": rows}
            print(data)

            url = 'https://pro.shanghaicme.com/cme/Project/pageQueryStatic'
            res = requests.post(url, data=data)
            res = res.json().get('rows')

            "构建每列数据"
            for i in res:
                table_metadata_data = []
                table_metadata_data.append(i.get('projectNumber'))
                table_metadata_data.append(i.get('name'))
                table_metadata_data.append(i.get('projectTypeStr'))
                table_metadata_data.append(i.get('organizationName'))
                table_metadata_data.append(i.get('managerName'))
                table_metadata_data.append(i.get('otherApplyOrganizationPhone'))
                table_metadata_data.append(i.get('otherHoldStarDate'))
                table_metadata_data.append(i.get('otherHoldEndDate'))
                table_metadata_data.append(i.get('otherHoldDayNumber'))
                table_metadata_data.append(i.get('otherHoldAddress'))
                table_metadata_data.append(i.get('otherTeachObject'))
                table_metadata_data.append(i.get('otherPlanCredit'))
                table_metadata_data.append(i.get('otherPlanStudentNumber'))

                "获取授课讲师信息"
                id = i.get('id')
                if id is not None:
                    project_teacher = self.__get_teacher_info(id)
                    table_metadata_data.append(project_teacher)

                table_metadata_data_all.append(table_metadata_data)

            time.sleep(5)
        return table_metadata_data_all

    def __get_teacher_info(self, id):
        url = 'https://pro.shanghaicme.com/cme/ProjectCourseTeacher/pageQuery'
        data = {
            "projectId": id
        }
        r = requests.post(url=url, data=data)
        rows = r.json().get('rows')

        tearch_data_all = []
        for i in rows:
            """
            name: 姓名
            organization: 单位
            title: 讲授题目
            teacherContact: 讲师联系方式
            """
            t_data = []
            t_data.append(i.get('name'))
            t_data.append(i.get('organization'))
            t_data.append(i.get('teacherContact'))
            tearch_data_all.append(t_data)

        # print(tearch_data_all)
        return str(tearch_data_all)


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

        print('>>> 开始写入Excel <<< ')
        # 遍历列表，将数据写入工作表
        for row in tabledata:
            ws.append(row)  # append()方法会直接将一行数据添加到工作表的末尾

        # 保存工作簿到文件
        file_name = '上海CME_%s.xlsx' % (time.strftime('%Y-%m-%d'))
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
            excel_file = '上海CME_%s.xlsx' % (time.strftime('%Y-%m-%d'))

        if sql_file_name is None:
            sql_file_name = '上海CME_INSERT_%s.sql' % (time.strftime('%Y-%m-%d'))

        df = pd.read_excel(excel_file)
        now_rows = df.shape[0]  # 获取行数
        df.fillna("null", inplace=True)  # 将空字符给赋指定默认值NULL

        table_head = list(df.columns.values)  # 获取表头

        print(table_head)
        print('>>> 开始写入SQL <<< ')

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

        print('>>> SQL 转化完成 <<<')
        return sql_file_name


if __name__ == '__main__':
    # """1.获取表格数据"""
    # cme_data_obj = ShangHaiCME()
    # table_all = cme_data_obj.get_shanghai_cme(year=2025, total=611, rows=20)
    # print(f'总计条目数: {len(table_all)}')
    # print(table_all)

    # """2.导入Excel"""
    to_excel_obj = metadataToFile()
    # to_excel_obj.toExcel(tabledata=table_all)

    # to_excel_obj.to_inster_sql2()

    to_excel_obj.to_inster_sql2(excel_file_name='上海CME_2025-07-23.xlsx')
    # to_excel_obj.to_inster_sql2(excel_file='SH2025.xlsx', sql_file_name='SH2025.sql')
