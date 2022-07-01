# -*- coding:utf-8 -*-
import time

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Chrome_action import Chrome_automation
import pandas as pd




if __name__ == '__main__':
    driver = Chrome_automation('https://cmegsb.cma.org.cn/national_project/listProjectGongbu.jsp',10)
    df = pd.DataFrame()
    for page in range(1,15): #翻页
        chrome_df = driver.verification(page)
        # df = pd.concat([df, chrome_df])
        if page >= 14:
            chrome_df.to_excel('result2022-%s.xlsx'%page)


