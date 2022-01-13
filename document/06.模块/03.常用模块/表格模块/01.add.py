import xlwt

names = ['jason', 'vivi', 'tom', 'marry', 'jack']
ages = [18, 18, 18, 18, 18]
adds = ['安徽', '安徽', '安徽', '安徽', '安徽']

book = xlwt.Workbook()
sheet = book.add_sheet('sheet1')
col_names = ['姓名', '年龄', '家庭住址']

for index, title in enumerate(col_names):
    sheet.write(0, index, title)

for index, name in enumerate(names):
    sheet.write(index + 1, 0, name)

for index, age in enumerate(ages):
    sheet.write(index + 1, 1, age)

for index, add in enumerate(adds):
    sheet.write(index + 1, 2, add)

book.save('test.xls')


