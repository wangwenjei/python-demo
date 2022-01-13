import configparser
"""
ini文件解析器  可以用于定义读取配置文件
"""

# 将配置文件内容读取到内存
config = configparser.ConfigParser()
config.read(r'test.ini')

# 获取有哪些 section
print(config.sections())  # ==> ['section1', 'section2']

# 获取指定section下的配置的key
print(config.options(section='section1'))  # ==> ['name', 'age']

# 获取指定section下配置的 key value
print(config.items(section='section1'))   # ==> [('name', "'wwj'"), ('age', '18')]

# 获取指定 section 下某个option 对应的值 值得类型为str
res = config.get(section='section1',option='name')
print(res,type(res))  # ==> 'wwj' <class 'str'>

# 获取指定 section 下某个option 对应的值  值的类型为int
res = config.getint(section='section1',option='age')
print(res,type(res)) # ==> 18 <class 'int'>


