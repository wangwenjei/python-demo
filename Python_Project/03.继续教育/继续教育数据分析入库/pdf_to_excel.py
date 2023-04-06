import pdfplumber
import pandas as pd
import time

""" 继续教育数据治理导出Excel """

# 元数据格式
metadata = {
    'projectId': [], 'project_num': [], 'project_name': [], 'company': [], 'leading_name': [],
    'tel': [], 'startdate': [], 'enddate': [], 'date_num': [],
    'address': [], 'credit': [], 'crowd': [], 'person_num': [], 'remark': []
}

# 读取pdf文件，保存为pdf实例
pdf = pdfplumber.open('./2023-02.pdf')
for i in range(509):  # 循环PDF读取每页
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

        metadata['startdate'].append(i[5][0:10])
        metadata['enddate'].append(i[5][11:21])
        metadata['date_num'].append(i[5][21::])


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

    # writer.save()
    # FutureWarning: save is not part of the public API, usage can give unexpected results and will be removed in a future version
    # 在新的版本中 save 方法已私有化 直接调用close 即可

    writer.close()


to_excel(metadata=metadata)

# print(metadata['project_num'])
