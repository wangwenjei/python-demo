#!/bin/python3

def inter_time():
    error_data = 0
    metadata = []
    with open(r'/Users/shaun/Healife/api_log.log', mode='rt', encoding='utf-8') as f:
        while True:
            res = f.readline().strip('\n')
            if len(res) == 0:
                break

            api_interface = res.split('|')[3].split(' ')[2].split('?')[0]
            api_interface_request_time = res.split('|')[11]

            try:
                api_interface_request_time = float(api_interface_request_time)
                metadata.append({
                    'api_interface': api_interface,
                    'api_interface_request_time': api_interface_request_time
                })
            except Exception as e:
                error_data += 1

    # 先按api_interface 排序, 再按api_interface_request_time 排序
    metadata = sorted(metadata, reverse=True, key=lambda i: (i['api_interface'], i['api_interface_request_time']))

    num = 0  # 元数据下标
    group_index = 0  # 同一类数据临时次数计数
    group_num = 0  # 组数
    min_index = 5  # 顺着数
    inter_time = []

    while num < len(metadata):
        # print(num)
        # 因数据降序处理过,故每组第一个数据就是改组最大数
        if group_index == 0:
            str_max = metadata[num].get('api_interface_request_time')
            inter_time.append({
                'inter_name': metadata[num].get('api_interface'),
                'max_time': str_max,
                'min_time': ''
            })
            group_num += 1

        if len(metadata) == num + 1:
            break
        elif metadata[num]['api_interface'] == metadata[num + 1]['api_interface']:
            group_index += 1
            if group_index == min_index:
                inter_time[group_num - 1].update({'min_time': metadata[num].get('api_interface_request_time')})
        else:
            if group_index < min_index:
                inter_time[group_num - 1].update({'min_time': metadata[num].get('api_interface_request_time')})
            group_index = 0

        num += 1

    with open(r'nginx_time11.txt', mode='wt', encoding='utf-8') as f:
        for i in inter_time:
            res = "{inter_name} | {max_time} | {min_time} \n".format(inter_name=i['inter_name'], max_time=i['max_time'], min_time=i['min_time'])
            f.write(res)


if __name__ == '__main__':
    inter_time()
