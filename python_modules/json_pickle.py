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
# ensure_ascii=False  默认为True此时中文为字符编码, Flase则表示写入的中文
print(json.dumps([1,'aa',True,'哈哈哈'],ensure_ascii=False)) # [1, "aa", true, "哈哈哈"]

# 结合with open更简便的将反序列化内容写入磁盘
res_list = [1,'aa',True,'哈哈哈']
with open(r'./test.json',mode='wt',encoding='utf-8') as f:
    json.dump(res_list,f,ensure_ascii=False)

# 反序列化  反序列化的内容需要是 str类型
print(json.loads('[1, "aa", true]'))  # [1, 'aa', True]

# 将文件中的内容 反序列化
with open(r'test.json',mode='rt',encoding='utf-8') as f:
    json_res = f.read()
    l_loads = json.loads(json_res)
    print(l_loads) # [1, "aa", true]



import pickle
"""
    pickle 与 json 用法相似 但pickle序列化的字符串只能被Python使用
    pickle.dump()  pickle.load() 与json.dump() json.load() 用法相同
"""
#序列化
res_pickle_dumps = [1,'aa',True]
print(pickle.dumps(res_pickle_dumps))
# b'\x80\x04\x95\r\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01\x8c\x02aa\x94\x88e.'

# 反序列化
print(pickle.loads(pickle.dumps(res_pickle_dumps)))  # [1, 'aa', True]
