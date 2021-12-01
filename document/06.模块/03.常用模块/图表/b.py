# -*- coding: utf-8 -*-
"""
project_name:pyecharts
@author: 帅帅de三叔
Created on Wed Mar  4 10:59:13 2020
https://blog.csdn.net/zengbowengood/article/details/104695205
"""
import pandas as pd  # 导入数据分析模块pip
from pyecharts.charts import Geo  # 导入地理信息处理模块
from pyecharts import options as opts  # 配置
from pyecharts.render import make_snapshot  # 快照
from snapshot_selenium import snapshot
from pyecharts.globals import ChartType, SymbolType  # 全局配置

data = pd.read_excel("D:\数有引力\魔都商圈\办公项目.xlsx")  # 读取数据
geo_sight_coord = {data['项目名称'][i].strip(): [data['经度'][i], data['纬度'][i]] for i in range(len(data))}  # 构造位置字典数据
data_pair = [(data['项目名称'][i].strip(), data['日租金'][i]) for i in range(len(data))]  # 构造项目租金数据

g = Geo()  # 地理初始化
g.add_schema(maptype="上海")  # 限定上海市范围
for key, value in geo_sight_coord.items():  # 对地理点循环
    g.add_coordinate(key, value[0], value[1])  # 追加点位置

g.add("", data_pair, symbol_size=2)  # 追加项目名称和租金
g.set_series_opts(label_opts=opts.LabelOpts(is_show=False), type='scatter')  # 星散点图scatter

pieces = [
    {'max': 3, 'label': '<3', 'color': '#00B2EE'},
    {'min': 3, 'max': 6, '3~6': 'love', 'color': '#71C671'},
    {'min': 6, 'max': 10, '6~10': 'always', 'color': '#CD4F39'},
    {'min': 10, 'label': '10+', 'color': '#FF0000'}  # 有下限无上限
]

g.set_global_opts(visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=pieces),
                  title_opts=opts.TitleOpts(title="办公项目分布"))  # 办公项目分布图

make_snapshot(snapshot, g.render("上海市办公项目.html"), "上海市办公项目.png")  # 渲染成html格式和png格式
