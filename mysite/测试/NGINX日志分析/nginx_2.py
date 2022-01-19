#!/bin/python3
from threading import Thread
import time

# def inter_time():
#     api_list = []
#     api_interface_unique = []
#
#     with open(r'/Users/shaun/Healife/api_log.log', mode='rt', encoding='utf-8') as f:
#         while True:
#             res = f.readline().strip('\n')
#             if len(res) == 0:
#                 break
#
#             api_interface = res.split('|')[3].split(' ')[2].split('?')[0]
#             api_interface_request_time = res.split('|')[11]
#             api_interface_response_time = res.split('|')[12]
#
#             api_interface_unique.append(api_interface)
#
#             api_list.append({
#                 'api_interface': api_interface,
#                 'api_interface_request_time': api_interface_request_time,
#                 'api_interface_response_time': api_interface_response_time
#             })
#
#     api_interface_unique = list(set(api_interface_unique))
#
#     interface_time = []
#     for interface in api_interface_unique:
#         t = []
#         for i in api_list:
#             if interface == i['api_interface']:
#                 t.append(i['api_interface_request_time'])
#
#         t.sort(reverse=True)
#
#         if len(t) == 1:
#             interface_time.append({
#                 'interface_name': interface,
#                 'max_time': t[0],
#                 'min_time': ' '
#             })
#         elif 1 < len(t) <= 100:
#             interface_time.append({
#                 'interface_name': interface,
#                 'max_time': t[0],
#                 'min_time': t[-1]
#             })
#         else:
#             interface_time.append({
#                 'interface_name': interface,
#                 'max_time': t[0],
#                 'min_time': t[99]
#             })
#
#     print(interface_time)
#
#
# if __name__ == '__main__':
# inter_time()


a = [
    {'api_interface': '/v1/open/series/page', 'api_interface_request_time': ' 0.219 ',
     'api_interface_response_time': ' 0.171 '},
    {'api_interface': '/v1/liveProgram/page', 'api_interface_request_time': ' 0.228 ',
     'api_interface_response_time': ' 0.084 '},
    {'api_interface': '/v1/open/video/search/page', 'api_interface_request_time': ' 0.431 ',
     'api_interface_response_time': ' 0.360 '},
    {'api_interface': '/v1/open/series/page', 'api_interface_request_time': ' 0.219 ',
     'api_interface_response_time': ' 0.171 '},
    {'api_interface': '/v1/liveProgram/page', 'api_interface_request_time': ' 0.228 ',
     'api_interface_response_time': ' 0.084 '},
    {'api_interface': '/v1/open/video/search/page', 'api_interface_request_time': ' 0.431 ',
     'api_interface_response_time': ' 0.360 '}
]

lis = [
    {"name": "a", "age": 100},
    {"name": "b", "age": 101},
    {"name": "c", "age": 102},
    {"name": "d", "age": 103},

    {"name": "a", "age": 104},
    {"name": "b", "age": 105},
    {"name": "c", "age": 106},
    {"name": "d", "age": 107},

    {"name": "a", "age": 100},
    {"name": "a", "age": 100},
    {"name": "a", "age": 100},
]

# 通过 age 升序排序
print("列表通过 age 升序排序: ")
print(sorted(lis, reverse=True, key=lambda i: (i['name'], i['age'])))

"""

[
{'api_interface': '/v1/liveProgram/page', 'api_interface_request_time': 0.228},
{'api_interface': '/v1/liveProgram/page', 'api_interface_request_time': 0.228}, 
{'api_interface': '/v1/liveProgram/page', 'api_interface_request_time': 1.228}, 
{'api_interface': '/v1/liveProgram/page', 'api_interface_request_time': 1.228},

{'api_interface': '/v1/open/series/page', 'api_interface_request_time': 0.219},
{'api_interface': '/v1/open/series/page', 'api_interface_request_time': 0.219}, 
{'api_interface': '/v1/open/series/page', 'api_interface_request_time': 1.219}, 
{'api_interface': '/v1/open/series/page', 'api_interface_request_time': 1.219}, 

{'api_interface': '/v1/open/video/search/page', 'api_interface_request_time': 0.431}, 
{'api_interface': '/v1/open/video/search/page', 'api_interface_request_time': 0.431}, 
{'api_interface': '/v1/open/video/search/page', 'api_interface_request_time': 1.431}, 
{'api_interface': '/v1/open/video/search/page', 'api_interface_request_time': 1.431}]



"""

"""

    num = 1  # 元数据下标
    o = 0  # 组下标

    while num < len(metadata):
        if o == 0:
            str_start = metadata[num - 1]['api_interface_request_time']
            print('str_start: '+str(str_start))

        str_temp = metadata[num - 1]['api_interface_request_time']
        if str_temp == metadata[num]['api_interface']:
            o += 1

        else:
            o = 0
            str_end = metadata[num - 1]['api_interface_request_time']
            print('str_end:  '+ str(str_end))

        num += 1
"""
