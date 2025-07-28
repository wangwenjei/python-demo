from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素

browser = webdriver.Firefox()
browser.get('https://www.amazon.cn/')

wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID, 'mainPageWrapper')))
tag = browser.find_elements(By.CSS_SELECTOR, '#nav-logo-link nav-progressive-attribute ')

# 获取标签属性
print(wait)
print(tag)

# 获取标签id, 位置, 名称, 大小
# print(tag.extend(id))

browser.close()
