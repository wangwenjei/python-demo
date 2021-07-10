import json
#     ujson模块与json模块用法相同,但是ujson.dumps 与 ujson.loads功能更快
"""
    什么是序列化与反序列化
        内存中的数据类型 ---> 序列化   ---> 特定的格式(json格式 或 pickle格式)
        内存中的数据类型 <--- 反序列化 <--- 特定的格式(json格式 或 pickle格式)
    
    为何要序列化
        序列化得到的结果是特定的格式内容
        用途:	1.可用于存储
                    可以是一种专用的格式: pickle 只能被Python 识别
                    也可以是通用数据类型,但不推荐
                2.传输给其他平台使用
                    应该是一种通用,能搞被所有语言识别的格式: json
"""
# json 序列化   序列化后的内容是 str类型
print(json.dumps([1,'aa',True])) # [1, "aa", true]

# 结合with open更简便的将反序列化内容写入磁盘
res_dumps = json.dumps([1,'aa',True])
with open(r'./test.json',mode='wt',encoding='utf-8') as f:
    json.dump(res_dumps,f)

# 反序列化  反序列化的内容需要是 str类型
print(json.loads('[1, "aa", true]'))  # [1, 'aa', True]

# 将文件中的内容 反序列化
with open(r'test.json',mode='rt',encoding='utf-8') as f:
    json_res = f.read()
    l_loads = json.loads(json_res)
    print(l_loads) # [1, "aa", true]


"""
    ===== pickle ===== 与json 模块使用方法类似
    序列化
        pickle.dumps()
    
        pickle.dump()
    
    反序列化
        pickle.loads()
    
        pickle.load()
"""