import copy
import pdfplumber
import pandas as pd
import time
from docx import Document

""" 继续教育数据治理导出Excel """


class GetMetaData:
    # 元数据格式
    metadata_format_list = {
        'projectId': [],
        'project_num': [],  # 项目编号
        'project_name': [],  # 项目名称
        'company': [],  # 申办单位
        'leading_name': [],  # 项目负责人
        'tel': [],  # 负责人电话
        'startdate': [],  # 举办开始时间
        'enddate': [],  # 举办结束时间
        'date_num': [],  # 举办天数
        'address': [],  # 举办地点
        'credit': [],  # 学分
        'crowd': [],  # 教学对象
        'person_num': [],  # 招生人数
        'remark': []  # 备注
    }

    def __init__(self):
        ...

    def get_meta_data(self, file, page=None, *args, **kwargs) -> dict:
        """
        获取文件内元数据
        :param file: 文件
        :param page: 页码数
        :param args:
        :param kwargs:
        :return:
        """
        if file.endswith('.docx'):
            meta = self._read_tables_from_docx(world_file_path=file, *args, **kwargs)
            return meta

        if file.endswith('pdf'):
            meta = self._read_tables_from_pdf(pdf_file_path=file, pdf_page=page, *args, **kwargs)
            return meta

    def _read_tables_from_pdf(self, pdf_file_path, pdf_page=None, *args, **kwargs) -> dict:
        """
        获取PDF内表格数据并将其数据格式化返回
        :param pdf_file_path: PDF路径
        :param pdf_page: PDF页数
        :param args:
        :param kwargs:
        :return: dict 格式化后表格数据
        """

        data_list = []
        pdf = pdfplumber.open(pdf_file_path)
        if pdf_page is None:
            pdf_page = len(pdf.pages)

        for i in range(0, pdf_page):  # 循环PDF读取每页
            first_page = pdf.pages[i]
            table = first_page.extract_table()
            table.pop(0)  # 删除每页第一行的头文件

            for row_data in table:
                row_data = [item.replace("\n", "").replace(" ", "") for item in row_data]
                data_list.append(row_data)

                # print(row_data)  # 打印每行数据
        # 数据格式化为元数据格式
        metadata = self.__format_metadata(data_list=data_list)

        return metadata

    def _read_tables_from_docx(self, world_file_path, *args, **kwargs) -> dict:
        """
        获取world内表格数据并将其数据格式化返回
        :param world_file_path: world路径
        :return: dict 格式化后表格数据
        """

        doc = Document(world_file_path)
        data_list = []
        for table in doc.tables:  # 遍历文档中的所有表格
            row_number = len(table.rows)  # 行数
            cells_number = len(table.rows[0].cells)  # 列数

            for i in range(1, row_number):  # # 遍历表格中的所有行,并过滤第一行表头数据
                row = table.rows[i]
                row_data = []  # 每行列表的数据

                for cell in row.cells:  # 遍历行中的所有单元格
                    data = cell.text.replace('\n', '').replace(' ', '')  # 读取单元格的文本并将文本中的换行和空格替换为空

                    if data:
                        row_data.append(data)

                    if not data:  # 若是字段为空赋于NULL值
                        row_data.append('NULL')
                    # print(data)
                # print(row_data)  # 打印每行数据
                data_list.append(row_data)

        # 数据格式化为元数据格式
        metadata = self.__format_metadata(data_list=data_list)
        return metadata

    def __format_metadata(self, data_list, *args, **kwargs) -> dict:
        """
        :param data_list: 需要格式化的元数据 [[单行数据],[],[]]
        :return: dict 格式化后表格数据
        """
        metadata = copy.deepcopy(self.metadata_format_list)

        for i in data_list:
            metadata['projectId'].append('null')
            metadata['project_num'].append(i[0])
            metadata['project_name'].append(i[1])
            metadata['company'].append(i[2])
            metadata['leading_name'].append(i[3])
            metadata['tel'].append(i[4])
            metadata['address'].append(i[6])
            metadata['credit'].append(i[7].split('分')[0])
            metadata['crowd'].append(i[8])
            if i[9].split('/')[0]:
                metadata['person_num'].append(i[9].split('/')[0].replace('NULL', '0'))
            else:
                metadata['person_num'].append(0)
            metadata['remark'].append(i[10].replace('NULL', ' ')) if i[10] else metadata['remark'].append(" ")
            metadata['startdate'].append(i[5][0:10])
            metadata['enddate'].append(i[5].split('-')[1][:10])
            metadata['date_num'].append(i[5].split('-')[1][10:].split('天')[0])

        return metadata


class MetadataToFile:
    """
        将格式化的metadata数据输出到不同格式的文件

        输出到Excel
            to_excel 手动指定表头
            to_excel2 根据元数据键值对自动设置表头

        将EXCEL内容输出到SQL文件
            to_inster_sql 手动指定列字段
            to_inster_sql2


    """

    def __init__(self, metadata):
        self.metadata = metadata

    def to_excel(self, file_name=None, *args, **kwargs):
        """
        将格式化后数据写入Excel
        :param file_name: 输出Excel文件名
        :param args:
        :param kwargs:
        :return: Excel文件名
        """

        if file_name is None:
            file_name = '非基地_%s.xlsx' % (time.strftime('%Y-%m-%d'))
        else:
            file_name = '非基地_' + file_name + '.xlsx'

        confirm_execl_data = {
            'projectId': self.metadata['projectId'],
            'project_num': self.metadata['project_num'],
            'project_name': self.metadata['project_name'],
            'company': self.metadata['company'],
            'leading_name': self.metadata['leading_name'],
            'tel': self.metadata['tel'],
            'startdate': self.metadata['startdate'],
            'enddate': self.metadata['enddate'],
            'date_num': self.metadata['date_num'],
            'address': self.metadata['address'],
            'credit': self.metadata['credit'],
            'crowd': self.metadata['crowd'],
            'person_num': self.metadata['person_num'],
            'remark': self.metadata['remark']
        }
        writer = pd.ExcelWriter(file_name)
        df_confirm = pd.DataFrame(confirm_execl_data)
        df_confirm.to_excel(excel_writer=writer, sheet_name='继续教育')

        # writer.save()
        # FutureWarning: save is not part of the public API, usage can give unexpected results and will be removed in a future version
        # 在新的版本中 save 方法已私有化 直接调用close 即可
        writer.close()

        return file_name

    def to_excel2(self, file_name=None, *args, **kwargs):
        """
        将格式化后数据写入Excel,自动识别字典内键值对,以dict key为EXCEL列名,dict value为EXCEL 列值
        :param file_name: 输出Excel文件名
        :param args:
        :param kwargs:
        :return: Excel文件名
        """

        if file_name is None:
            file_name = '非基地_%s.xlsx' % (time.strftime('%Y-%m-%d'))
        else:
            file_name = '非基地_' + file_name + '.xlsx'

        confirm_execl_data = {}
        for k in self.metadata:  # 循环字典,对每个KEY生产EXCEL列数据
            row_data = {k: self.metadata.get(k)}
            confirm_execl_data.update(row_data)

        writer = pd.ExcelWriter(file_name)
        df_confirm = pd.DataFrame(confirm_execl_data)
        df_confirm.to_excel(excel_writer=writer, sheet_name='继续教育')

        # writer.save()
        # FutureWarning: save is not part of the public API, usage can give unexpected results and will be removed in a future version
        # 在新的版本中 save 方法已私有化 直接调用close 即可
        writer.close()

        return file_name

    def to_inster_sql(self, excel_file=None, sql_file_name=None, *args, **kwargs):
        """
        指定列名
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

        with open(sql_file_name, mode='a', encoding='utf-8') as f:
            sql = "insert into edu_record (projectId, project_num, project_name, company,leading_name, tel, startdate, enddate, date_num, address, credit, crowd, person_num, remark ) values"
            f.write(sql)

            for i in range(now_rows):
                # 去除索引列
                data = list(df.loc[i].values)
                data.pop(0)

                data = str(tuple(data)) + ','
                # print(data)
                f.write(data)

        return sql_file_name

    def to_inster_sql2(self, excel_file=None, sql_file_name=None, *args, **kwargs):
        """
        自动获取EXCEL表头为列名
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
            """
            sql = "insert into edu_record 
                (projectId, ... ) 
                values
            """

            # 依据Excel表头依次添加需要插入数据的表字段
            table_head.pop(0)
            insert_fields = str(tuple(table_head)).replace("'", '')  #
            sql = "insert into edu_record {insert_fields} values".format(insert_fields=insert_fields)
            f.write(sql)

            for i in range(now_rows):
                # 去除索引列
                data = list(df.loc[i].values)
                data.pop(0)

                data = str(tuple(data)) + ','
                # print(data)
                f.write(data)

        return sql_file_name


if __name__ == '__main__':
    # "2024"
    # file = input("请输入文件PATH==>:")
    file = './2024-0902.pdf'
    # file = './2024-09-02.docx'
    md = GetMetaData()
    metadata = md.get_meta_data(file=file, page=2)

    tofile = MetadataToFile(metadata=metadata)
    a = tofile.to_excel()
    # a = tofile.to_excel2()
    # b = tofile.to_inster_sql()

    # p = md.get_meta_date(file='./2024-0902.pdf', page=1)
    # d = md.get_meta_date(file='./2024-09-02.docx')

    "2025"
    file = './2025年已批准项目表_非基地.pdf'
    md = GetMetaData()
    metadata = md.get_meta_data(file=file, page=1)
    tofile = MetadataToFile(metadata=metadata)
    tofile.to_excel2()
    tofile.to_inster_sql2()
