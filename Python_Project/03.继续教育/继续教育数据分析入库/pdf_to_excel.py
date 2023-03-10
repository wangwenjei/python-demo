# 解析PDF文件并分析有用数据写入Excel文件
import pdfplumber
import pandas as pd
import xlwt
import time

# 元数据格式
metadata = {
    'projectId': [],
    'project_num': [],
    'project_name': [],
    'company': [],
    'leading_name': [],
    'tel': [],
    'startdate': [],
    'enddate': [],
    'date_num': [],
    'address': [],
    'credit': [],
    'crowd': [],
    'person_num': [],
    'remark': []
}

# 读取pdf文件，保存为pdf实例
pdf = pdfplumber.open('./2023-01.pdf')
# for i in range(342):  # 循环PDF读取每页
# for i in range(2):  # 循环PDF读取每页
for i in range(509): 
    first_page = pdf.pages[i]
    table = first_page.extract_table()

    table.pop(0)  # 删除每页第一行的头文件
    for i in table:  # 构造数据
        metadata['projectId'].append('null')
        metadata['project_num'].append('%s%s' % (i[0].split('\n')[0], i[0].split('\n')[1]))
        metadata['project_name'].append(i[1])
        metadata['company'].append(i[2])
        metadata['leading_name'].append(i[3])
        metadata['tel'].append(i[4])
        metadata['address'].append(i[6])
        metadata['credit'].append(i[7].split('分')[0])
        metadata['crowd'].append(i[8])
        metadata['person_num'].append(i[9].split('/')[0])
        metadata['remark'].append(i[10])

        date = i[5].split('\n')
        metadata['startdate'].append(date[0].rstrip('-'))
        metadata['enddate'].append(date[1])
        metadata['date_num'].append(date[2].split('天')[0])


# 写入Excel
def to_excel(metadata):
    file_name = '%s.xlsx' % (time.strftime('%Y-%m-%d'))

    confirm_execl_data = {
        'projectId': metadata['projectId'],
        'project_num': metadata['project_num'],
        'project_name': metadata['project_name'],
        'company': metadata['company'],
        'leading_name': metadata['leading_name'],
        'tel': metadata['tel'],
        'startdate': metadata['startdate'],
        'enddate': metadata['enddate'],
        'date_num': metadata['date_num'],
        'address': metadata['address'],
        'credit': metadata['credit'],
        'crowd': metadata['crowd'],
        'person_num': metadata['person_num'],
        'remark': metadata['remark']

    }

    writer = pd.ExcelWriter(file_name)

    df_confirm = pd.DataFrame(confirm_execl_data)
    df_confirm.to_excel(excel_writer=writer, sheet_name='继续教育')

    writer.save()
    writer.close()


to_excel(metadata=metadata)

# print(metadata['project_num'])
