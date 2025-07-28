from openpyxl import Workbook
import pandas as pd
import time


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
            insert_fields = str(tuple(table_head)).replace('\'', '')  #
            sql = "insert into edu_record_2023_0314 {insert_fields} values".format(insert_fields=insert_fields)
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
    """4.将数据写入文件"""
    to_excel_obj = metadataToFile()

    # EXCEL转化为INSERT SQL
    to_excel_obj.to_inster_sql2(excel_file='./广东_20250723.xlsx', sql_file_name='广东_20250723.sql')
