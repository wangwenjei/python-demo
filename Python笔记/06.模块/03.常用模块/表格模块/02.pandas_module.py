import pandas as pd
import time

metadata = {
    'studentName': ['jason', 'jack', 'vivi', 'tony', 'lucy', 'bob'],
    'chineseScore': [99, 88, 77, 66, 55, 44],
    'mathScore': [99, 88, 77, 66, 55, 44],
    'englishScore': [99, 88, 77, 66, 55, 44]
}


def to_excel(metadata):
    file_name = '%s.xlsx' % (time.strftime('%Y-%m-%d'))

    confirm_execl_data = {
        '姓名': metadata.get('studentName'),
        '语文成绩': metadata.get('chineseScore'),
        '数学成绩': metadata.get('mathScore'),
        '英语成绩': metadata.get('englishScore')
    }

    writer = pd.ExcelWriter(file_name)
    df_confirm = pd.DataFrame(confirm_execl_data)
    df_confirm.to_excel(excel_writer=writer, sheet_name='学生成绩单')
    writer.close()


to_excel(metadata=metadata)
