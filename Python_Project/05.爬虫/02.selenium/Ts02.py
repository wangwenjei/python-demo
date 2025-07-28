from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素

driver = webdriver.Firefox()
try:
    driver.get('https://www.baidu.com')

    input_tag = driver.find_element(By.ID, "kw")
    input_tag.send_keys('python')  # python2中输入中文错误，字符串前加个u
    input_tag.send_keys(Keys.ENTER)  # 输入回车

    wait = WebDriverWait(driver, 60)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))  # 等到id为content_left的元素加载完毕,最多等60秒

    # print(driver.page_source)
    # print(driver.current_url)
    # print(driver.get_cookies())

finally:
    driver.close()
