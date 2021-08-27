import re

# html = """ <h2>多云</h2>  """
# print(re.findall('<[^>]+>', html))


# a = "项目:appserver"
# print(re.findall('[^\w+]:\w+', a))
# print(re.findall(':.*', a)[0])


# cc = re.findall(':.*', a)[0].split(':')[1]
# print(cc)

print(re.findall(':.*', "项目:appserver")[0].split(':')[1])  # ==> appserver


