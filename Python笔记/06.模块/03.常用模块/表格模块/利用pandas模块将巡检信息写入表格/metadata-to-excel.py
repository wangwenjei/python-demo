import os, time
import pandas as pd
from email_file import SendEmail


# 格式化巡检数据
def xunjian_metadata(metadata_path):
    """
    格式化每台主机的元数据
    :param metadata_path: 巡检脚本获取的主机元数据
    :return: 元数据字典 metadata_dict  {HOST: HostInfoData}
    """
    file_name_list = os.listdir(metadata_path)
    metadata_dict = {}
    for file_name in file_name_list:
        file_path = './metadata/%s' % file_name
        hosts_data = []
        with open(file_path, mode='rt', encoding='utf-8') as f:
            for i in f:
                hosts_data.append(i.rstrip('\n'))

        meta = {
            hosts_data[2].split(':')[1]: hosts_data
        }

        metadata_dict.update(meta)

    return metadata_dict


# 将巡检数据整理到Excel表格
def to_excel(metadata_dict):
    file_name = '%s.xlsx' % (time.strftime('%Y-%m-%d'))

    # Excel数据格式
    execl_data = {
        '主机名': [], '网卡名': [], '内网地址': [], '内核版本': [], '根目录可用率': [], 'CPU使用率': [], '总内存': [],
        '已用内存': [], '内存使用率': []
    }
    for i in metadata_dict:
        execl_data.get('主机名').append(metadata_dict.get(i)[0].split(':')[1])
        execl_data.get('网卡名').append(metadata_dict.get(i)[1].split(':')[1])
        execl_data.get('内网地址').append(metadata_dict.get(i)[2].split(':')[1])
        execl_data.get('内核版本').append(metadata_dict.get(i)[3].split(':')[1])
        execl_data.get('根目录可用率').append(metadata_dict.get(i)[4].split(':')[1])
        execl_data.get('CPU使用率').append(metadata_dict.get(i)[5].split(':')[1])
        execl_data.get('总内存').append(metadata_dict.get(i)[6].split(',')[0].split(':')[1])
        execl_data.get('已用内存').append(metadata_dict.get(i)[6].split(',')[1].split(':')[1])
        execl_data.get('内存使用率').append(metadata_dict.get(i)[6].split(',')[2].split(':')[1])

    writer = pd.ExcelWriter(file_name)
    df_confirm = pd.DataFrame(execl_data)
    df_confirm.to_excel(excel_writer=writer, sheet_name='主机巡检数据')
    writer.close()

    return file_name


# 发送邮件
def to_emial(file_name):
    send_xujian_file = SendEmail(
        mail_host="smtpdm.aliyun.com",
        mail_user="summer_wwj@email.wangwenjie520.com",
        mail_pass="0S03z1nzRVodB57qRY30",
        from_user='summer_wwj@email.wangwenjie520.com',
        to_user="wwj2254964433@163.com,2254964433@qq.com"
    )
    send_xujian_file.add_file(
        file_path=file_name,
        email_header='巡检信息',
        email_body='巡检信息推送'
    )


if __name__ == '__main__':
    metadata_dict = xunjian_metadata(metadata_path='./metadata')
    file_name = to_excel(metadata_dict=metadata_dict)
    to_emial(file_name=file_name)
