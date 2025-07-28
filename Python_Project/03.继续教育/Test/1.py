import requests

url = 'https://cmegsb.cma.org.cn/national_project/listBaseProjectGongbu.jsp'

# r = requests.get(url)
#
# print(r.text)

ll = ('https://cmegsb.cma.org.cn/national_project/projectGongbuList.do?'
      'gongbu=3&gongbuCode=&name=&xmanager=&sdanwei=&checkCode=8&'
      'pageSize=100'
      '&year=2024&scode=&parentSubjectId=&subjectId=&orderBy=subject&type=&beian=&pici=&requestType=PRINT_GONGBU')

cc = ('https://cmegsb.cma.org.cn/national_project/projectGongbuList.do?'
      'gongbu=3&gongbuCode=&name=&xmanager=&sdanwei=&'
      'checkCode=5&'
      'pageSize=10'
      '&year=2024&scode=&parentSubjectId=&subjectId=&orderBy=subject&type=&beian=&pici=&requestType=PRINT_GONGBU')

ee = 'https://cmegsb.cma.org.cn/national_project/projectGongbuList.do?gongbu=3&gongbuCode=&name=&xmanager=&sdanwei=&checkCode=5&pageSize=10&year=2024&scode=&parentSubjectId=&subjectId=&orderBy=subject&type=&beian=&pici=&requestType=PRINT_GONGBU'

r = requests.get(ee)
print(r.text)

