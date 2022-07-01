# coding:utf-8
import requests
import re
import pandas as pd
import time

url = 'http://www.nhc.gov.cn/xcs/yqtb/202203/e642fa60e7ca40938e029cbdbd49f62b.shtml'
# url = 'http://www.nhc.gov.cn/xcs/yqtb/202203/9e682bf6b5cc48749ae7a1a6247cc1dd.shtml'
# url = 'http://www.nhc.gov.cn/xcs/yqtb/202203/5cec89d7d07140f69d81a5d3b543005f.shtml'
req = requests.get(url).text

data = []  # 0 确诊病例元数据， 1 无症状病例元数据


# 获取所有p标签
def p_label():
    label_data = []
    re_div = re.findall('<[^>]*>+.*', req)
    for label in re_div:
        if 'p' in label:
            re_div_text = re.compile('<[^>]+>')
            s = re_div_text.sub('', label).split()
            for i in s:
                label_data.append(i)

    data.append(label_data[13])
    data.append(label_data[17])


p_label()
confirm = re.findall('\w*例', data[0])  # 地区确诊病例元数据
slight = re.findall('\w*例', data[1])  # 地区无症状病例元数据


# 判断是否以数字结尾
def end_num(string):
    text = re.compile(r'.*[0-9]$')
    if text.match(string):
        return True
    else:
        return False


city_confirm_number = {}  # 地区确诊病例数  cityName: number
city_slight_number = {}  # 地区无症状病例数 cityName: number

# 结构化确诊病例数据
for i in confirm:
    data = i.rstrip('例').lstrip('其中').lstrip('和')
    if end_num(data):
        name = re.findall('\D*', i.rstrip('例'))[0]
        number = re.findall('\d+', i.rstrip('例'))[0]
        city_confirm_number.update({name: number})

# 结构化无症状病例数据
for i in slight:
    data = i.rstrip('例').lstrip('其中').lstrip('和')
    if end_num(data):
        name = re.findall('\D*', i.rstrip('例'))[0]
        number = re.findall('\d+', i.rstrip('例'))[0]
        city_slight_number.update({name: number})


# 生成Excel文件
def to_excel(confirm, slight):
    file_name = '%s.xlsx' % (time.strftime('%Y-%m-%d'))
    confirm_city = confirm.keys()
    confirm_number = confirm.values()
    slight_city = slight.keys()
    slight_number = slight.values()

    confirm_execl_data = {
        'city': list(confirm_city),
        'number': list(confirm_number)
    }

    slight_execl_data = {
        'city': list(slight_city),
        'number': list(slight_number)
    }

    writer = pd.ExcelWriter(file_name)

    df_confirm = pd.DataFrame(confirm_execl_data)
    df_slight = pd.DataFrame(slight_execl_data)
    df_confirm.to_excel(excel_writer=writer, sheet_name='确诊病例')
    df_slight.to_excel(excel_writer=writer, sheet_name='无症状病例')

    writer.save()
    writer.close()

    # df_confirm = pd.DataFrame(confirm_execl_data)
    # df_confirm.to_excel(file_name, sheet_name='确诊病例')
    # df_slight = pd.DataFrame(slight_execl_data)
    # df_slight.to_excel(file_name, sheet_name='无症状病例')
    #

    # df = pd.DataFrame(confirm_execl_data)
    # df.to_csv(file_name)


if __name__ == '__main__':
    to_excel(confirm=city_confirm_number, slight=city_slight_number)