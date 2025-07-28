from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import time

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
wait = WebDriverWait(driver, 30)

try:

    """ 
        find_element 查找单个元素
            driver.find_element(By.ID, 'kw')
            driver.find_element(LINK_TEXT, '..')
            driver.find_element(PARTIAL_LINK_TEXT, '..')
            driver.find_element(TAG_NAME, '..')
            driver.find_element(CLASS_NAME, '..')
            driver.find_element(NAME, '..')
            driver.find_element(CSS_SELECTOR, '..')
            driver.find_element(XPATH, '..')

        find_elements() 查找到多个元素，结果为列表

    """

    "1. 通过id属性查找元素"
    # print(driver.find_element(By.ID, 'kw'))

    "2. 超链接元素"
    # login = driver.find_element(By.LINK_TEXT, '登录')
    # login.click()

    "3. 超链接元素"
    # login = driver.find_elements(By.PARTIAL_LINK_TEXT, '录')[0]
    # login.click()

    "4. 标签"
    # print(driver.find_element(By.TAG_NAME, 'a'))

    "4. CLASS元素 bg s_btn"
    # button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 's-top-login-btn')))
    # button.click()
    # print(but.text)

    "5. 登录百度"
    """
    #1. 点击登录
    #2. 阅读协议并同意
    isAgree = wait.until(EC.element_to_be_clickable((By.ID, 'TANGRAM__PSP_11__isAgree')))
    isAgree.click()

    #3. 输入用户名
    input_user = wait.until(EC.presence_of_element_located((By.NAME, 'userName')))
    input_user.send_keys('182xxx431')

    #4. 输入密码,baidu现在无法通过自动输入密码,此处可以暂停10S手动输入密码
    # input_pwd = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    # input_pwd.send_keys('PWD')
    time.sleep(10)

    #5. 提交登录
    commit = wait.until(EC.element_to_be_clickable((By.ID, 'TANGRAM__PSP_11__submit')))
    commit.click()

    #6. 短信验证
    """

    print(driver.find_element(By.CSS_SELECTOR, '#kw'))

    time.sleep(5)

finally:
    driver.close()
