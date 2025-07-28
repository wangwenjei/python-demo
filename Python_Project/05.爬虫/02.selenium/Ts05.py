from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import time

# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

# Firefox
chrome_options = Options()
chrome_options.add_argument("--headless")  # 设置为无头模式
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Firefox(firefox_binary="firefox_options")
driver.get("http://www.example.com")
# 你的测试代码
driver.quit()

#
# driver = webdriver.PhantomJS()
#
# driver.get('https://doc.scrapy.org/en/latest/_static/selectors-sample1.html')
# # wait=WebDriverWait(driver,3)
# driver.implicitly_wait(3)  # 使用隐式等待
