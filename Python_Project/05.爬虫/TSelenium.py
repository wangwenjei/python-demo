import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    word = input("请输入你要爬取的关键字：")
    page_size = int(input("请输入你要爬取的页数："))
    # 创建一个浏览器的启动对象
    driver = webdriver.Firefox()
    # 通过浏览器的驱动器对象打开京东的首页
    driver.get("https://www.jd.com/")
    # 找到搜索框
    input_box = driver.find_element(By.ID, "key")
    # 将要搜索的关键字输入到搜索框里面
    input_box.send_keys(word)
    # 按了enter键
    input_box.send_keys(Keys.ENTER)

    # range(page_size)  ---> 3页就是[0,1,2]
    for i in range(page_size):

        # 将下拉框拖到最下面 JS代码
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        # 确保在滚动的过程中，数据全部加载出来
        time.sleep(20)
        # 获取到所有的li   右键li复制Xpath  得到  //*[@id="J_goodsList"]/ul/li
        good_lists = driver.find_elements(By.XPATH, '//*[@id="J_goodsList"]/ul/li')
        # 把找到的数据放到列表
        prices, names, commits, shops = [], [], [], []
        for item in good_lists:
            # 产品价格  p-price 在网页class里面
            price = item.find_element(By.CLASS_NAME, "p-price").text
            # 产品名称
            name = item.find_element(By.CLASS_NAME, "p-name").text
            # 评论数
            commit = item.find_element(By.CLASS_NAME, "p-commit").text
            # 商家
            shop = item.find_element(By.CLASS_NAME, "p-shop").text
            prices.append(price)
            names.append(name)
            commits.append(commit)
            shops.append(shop)

            # 点击下一页，找到class等于pn-next 点击：click
        driver.find_element(By.CLASS_NAME, "pn-next").click()
        time.sleep(10)

        df = pd.DataFrame({
            "价格": prices,
            "名称": names,
            "评论": commits,
            "商家": shops
        })

        # 将数据保存到excel中
        df.to_excel("1.xlsx")
