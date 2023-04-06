from pyhive import hive

# import pandas as pd

"""
pip3 install pyhive
pip3 install thrift
pip3 install sasl
pip3 install thrift-compiler
pip3 install thrift-sasl

jdbc:hive2://172.xx.xx.96:22222/rawdata;auth=noSasl
47.xx.xx.44
"""

from pyhive import hive
import pandas as pd

from pyhive import hive
import pandas as pd

# 通过HIVE链接
cursor = hive.connect(host='47.xx.xx.44', port=22222, auth='NOSASL', database='rawdata').cursor()
cursor.execute("select user_id,distinct_id,time,date from events where distinct_id='26077' and date='2022-05-25' limit 100/*SA(production)*/;")

# fetchall()返回查询结果的余下的所有数据，使用此函数要评估数据量，可能会因为数据量太大，导致本地程序内存问题。
# cursor.description 查询结果集的元数据，返回结果集有多少列，每个列的列名，数据类型等数据。dataframe引用结果集为列名

data = cursor.fetchall()
columns = [col[0].split('.')[-1] for col in cursor.description]
data = pd.DataFrame(data=data, columns=columns)

print(columns)
# print(data)

# 读取数据

'''

def select_pyhive(sql):
    # 创建hive连接
    conn = hive.Connection(host='47.xx.xx.44', port=22222, auth='NOSASL', database='rawdata')
    cur = conn.cursor()
    try:
        # c = cur.fetchall()
        df = pd.read_sql(sql, conn)
        return df
    finally:
        if conn:
            conn.close()


sql = "select user_id,distinct_id,time from events where distinct_id='26077' limit 10/*SA*/;"
df = select_pyhive(sql)
'''
