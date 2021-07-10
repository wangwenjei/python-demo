import time

# 时间戳,用于时间间隔的计算
print(time.time())   #  1625903782.577814

# 按照某种格式显示时间,用于展示时间
print(time.strftime('%Y-%m-%d %H:%M:%S')) # 2021-07-10 15:58:29

# 结构化的时间,用于单独获取时间的某一部分
print(time.localtime())
# time.struct_time(tm_year=2021, tm_mon=7, tm_mday=10, tm_hour=15, tm_min=58, tm_sec=29, tm_wday=5, tm_yday=191, tm_isdst=0)

# 睡眠时间
time.sleep(0.3)


# time.strptime 将某一格式字符串转化为 结构化时间
struct_time=time.strptime('1997-11-11 11:11:11','%Y-%m-%d %H:%M:%S')
# time.mktime 将结构话时间转换为 时间戳 并计算添加七天的时间戳
timestamp = time.mktime(struct_time)+7*86400

# time.localtime 将时间戳转换为 结构化时间
# time.strftime 将结构化时间转化为 按照某一时间格式展示
res = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp))
print(res) #  1997-11-18 11:11:11

################
print("="*50)
################

import  datetime
# 获取规定格式的时间
print(datetime.datetime.now())  # 2021-07-10 16:11:27.564866

# 计算时间,获取三天后的时间
print( datetime.datetime.now() + datetime.timedelta(days=3) )  # 2021-07-13 16:11:27.564884

# 将时间戳转化为格式化为格式化字符的展示
print( datetime.datetime.fromtimestamp(879217871.0) ) # 1997-11-11 11:11:11