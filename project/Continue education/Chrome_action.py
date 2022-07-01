# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import cv2 as cv
from PIL import Image
# import pytesseract
import re
import pandas as pd
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By



dcap = dict(DesiredCapabilities.CHROME)
print(dcap)
dcap["Chrome.page.settings.userAgent"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
)
Tertiary_discipline_dic = {'20220101': '组织胚胎学', '20220102': '解剖学', '20220103': '遗传学', '20220104': '病理学', '20220105': '寄生虫学', '20220106': '微生物学', '20220201': '生理学', '20220202': '生物化学', '20220203': '生物物理学', '20220204': '药理学', '20220205': '细胞生物学', '20220206': '病生理学', '20220207': '免疫学', '20220208': '基础医学其他学科', '20220301': '心血管病学', '20220302': '呼吸病学', '20220303': '消化病学', '20220304': '血液病学', '20220305': '肾脏病学', '20220306': '内分泌学', '20220307': '神经内科学', '20220308': '感染病学', '20220309': '精神卫生学', '20220310': '老年医学', '20220311': '内科学其他学科', '20220401': '普通外科学', '20220402': '心胸外科学 ', '20220403': '烧伤外科学', '20220404': '神经外科学', '20220405': '泌尿外科学', '20220406': '显微外科学', '20220407': '骨外科学', '20220408': '肿瘤外科学', '20220409': '颅脑外科学', '20220410': '整形、器官移植外科学', '20220411': '外科学其他学科', '20220501': '妇科学', '20220502': '产科学', '20220503': '妇产科学其他学科', '20220601': '儿科内科学', '20220602': '儿科外科学', '20220603': '新生儿科学', '20220604': '儿科学其他学科', '20220701': '耳鼻咽喉科学', '20220702': '眼科学', '20220801': '口腔内科学', '20220802': '口腔外科学', '20220803': '口腔正畸学', '20220804': '口腔修复学', '20220805': '口腔学其他学科', '20220901': '放射诊断学', '20220902': '超声诊断学', '20220903': '放射肿瘤学', '20220904': '影像医学其他学科', '20221001': '急诊学', '20221101': '医学检验', '20221201': '劳动卫生与环境卫生学', '20221202': '营养与食品卫生学', '20221203': '儿少卫生与妇幼卫生学', '20221204': '卫生毒理学', '20221205': '统计流行病学', '20221206': '卫生检验学', '20221207': '公共卫生与预防医学其他学科', '20221301': '临床药学和临床药理学', '20221302': '药剂学', '20221303': '药物分析学', '20221304': '药事管理学', '20221305': '药学其他学科', '20221401': '内科护理学', '20221402': '外科护理学', '20221403': '妇产科护理学', '20221404': '儿科护理学', '20221405': '护理其他学科', '20221501': '医学教育', '20221502': '卫生管理', '20221601': '康复医学', '20221701': '全科医学', '20221801': '麻醉学', '20221901': '重症医学', '20222001': '皮肤病学与性病学', '20222101': '核医学', '20222201': '医院感染（管理）学', '20222301': '医学心理学', '20222302': '临床与咨询心理学', '20222303': '心理学其他学科', '20222401': '医学人文与医德医风', '20222402': '医患沟通', '20222403': '科研伦理', '20222404': '卫生法规'}

Secondary_discipline_dic = {'202201': '基础形态', '202202': '基础机能', '202203': '临床内科学', '202204': '临床外科学', '202205': '妇产科学', '202206': '儿科学', '202207': '眼、耳鼻咽喉科学', '202208': '口腔医学', '202209': '影像医学', '202210': '急诊学', '202211': '医学检验', '202212': '公共卫生与预防医学', '202213': '药学', '202214': '护理学', '202215': '医学教育与卫生管理学', '202216': '康复医学', '202217': '全科医学', '202218': '麻醉学', '202219': '重症医学', '202220': '皮肤病学与性病学', '202221': '核医学', '202222': '医院感染（管理）学', '202223': '心理学', '202224': '卫生法规与医学伦理学'}




class Chrome_automation:
    def __init__(self,url,timeout):
        # self.driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe',desired_capabilities=dcap)
        self.driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe',desired_capabilities=dcap)
        self.driver.implicitly_wait(timeout)  # 隐式等待
        self.driver.get(url)  # 打开浏览器
        self.driver.maximize_window()  # 最大化窗口
        time.sleep(2)
        self.driver.find_element_by_xpath('//select[@id="year"]/option[@value="2022"]').click()
        self.driver.find_element_by_xpath('//input[@id="pageSize"]').clear()
        self.driver.find_element_by_xpath('//input[@id="pageSize"]').send_keys('990')   # 修改页面数据量

        key_li = [element.get_attribute('value') for element in
                  self.driver.find_elements_by_xpath('//select[@id="parentSubjectId"]/option')]
        value_li = [element.text for element in self.driver.find_elements_by_xpath('//select[@id="parentSubjectId"]/option')]
        self.Secondary_discipline_dic = dict(zip(key_li, value_li))
        key_li = [element.get_attribute('value') for element in
                  self.driver.find_elements_by_xpath('//select[@id="subjectId"]/option')]
        value_li = [element.text for element in self.driver.find_elements_by_xpath('//select[@id="subjectId"]/option')]
        self.Tertiary_discipline_dic = dict(zip(key_li, value_li))
        print(self.Secondary_discipline_dic)
        print(self.Tertiary_discipline_dic)

    def OCR_NUM(self,image):
        # 边缘保留滤波  去噪
        a = cv.pyrMeanShiftFiltering(image, sp=55, sr=25)
        cv.imshow('jiangzao', a)
        # 灰度图像
        a = cv.cvtColor(a, cv.COLOR_BGR2GRAY)
        cv.imshow('huidu', a)
        # # 二值化
        # # ret, a = cv.threshold(a, 200, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        # # print(f'二值化设置的阈值：{ret}')
        # # cv.imshow('erzhihua',a)
        # # 形态学操作   腐蚀  膨胀
        a = cv.erode(a, None, iterations=1)
        a = cv.dilate(a, None, iterations=0)
        cv.imshow('dilate', a)
        #
        # # 逻辑运算  让背景为白色  字体为黑  便于识别
        a = cv.bitwise_not(a, a)
        cv.imshow('binary-image', a)

        # # 二值化
        ret, a = cv.threshold(a, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        print(f'二值化设置的阈值：{ret}')
        cv.imshow('erzhihua', a)

        # 识别
        test_message = Image.fromarray(a)
        text = pytesseract.image_to_string(test_message, lang='chi_sim')
        print(f'----验证码识别结果：{text}')
        cv.waitKey(0)
        cv.destroyAllWindows()
        return text

    def pic_code_interaction(self,flag,code=None):
        if flag == 'Get_PIC':
            img = self.driver.find_element_by_tag_name('#codeImg')  #获得图片选择器
            img.screenshot('yzm/yzm.png')     #截图保存至指定路径
        if flag == 'Refresh_PIC':
            self.driver.find_element_by_tag_name('#codeImg').click()
        if flag == 'send_code':
            self.driver.find_element_by_xpath('//input[@id="J_VCode"]').send_keys(code)
            # if page == 1:
            #     self.driver.find_element_by_xpath('//input[@value="查询"]').click()
            # else:
            #     self.driver.find_element_by_xpath('//a[@title="Go to page %s"]'%page).click()
            #
            # content_title = self.driver.find_element_by_xpath('//div[@class="mmm"]')
            # print(content_title)

    def get_result(self):
        # 项目id
        projectId_elements_li = self.driver.find_elements_by_xpath('//tr[@class="odd" or @class="even"]/td[last()]/button[@name="teacherListButton"]')
        projectId_li = [projectId_elements.get_attribute("projectid") for projectId_elements in projectId_elements_li]
        print('projectId_li:',projectId_li)
        print(len(projectId_li))
        #项目编号
        project_num_elements_li = self.driver.find_elements_by_xpath('//tr[@class="odd" or @class="even"]/td[1]')
        project_num_li = [project_num_elements.text for project_num_elements in project_num_elements_li]
        print('project_num_li:',project_num_li)
        print(len(project_num_li))
        #学科
        discipline_li = [self.Secondary_discipline_dic[re.findall('\d{4}-\d{2}', project_num_elements.text)[0].replace('-', '')]+'-'+self.Tertiary_discipline_dic[re.findall('\d{4}-\d{2}-\d{2}', project_num_elements.text)[0].replace('-', '')] for project_num_elements in project_num_elements_li]
        print('discipline_li:', discipline_li)
        print(len(discipline_li))
        #项目名称
        project_name_elements_li = self.driver.find_elements_by_xpath('//tr[@class="odd" or @class="even"]/td[2]')
        project_name_li = [project_name_elements.text for project_name_elements in project_name_elements_li]
        print('project_name_li:', project_name_li)
        print(len(project_name_li))
        #申办单位
        company_elements_li = self.driver.find_elements_by_xpath('//tr[@class="odd" or @class="even"]/td[3]')
        company_li = [company_elements.text for company_elements in company_elements_li]
        print('company_li:', company_li)
        print(len(company_li))
        #项目负责人
        leading_name_elements_li = self.driver.find_elements_by_xpath('//tr[@class="odd" or @class="even"]/td[4]')
        leading_name_li = [leading_name_elements.text for leading_name_elements in leading_name_elements_li]
        print('leading_name_li:', leading_name_li)
        print(len(leading_name_li))
        #负责人电话
        tel_elements_li = self.driver.find_elements_by_xpath('//tr[@class="odd" or @class="even"]/td[5]')
        tel_li = [tel_elements.text for tel_elements in tel_elements_li]
        print('tel_li:', tel_li)
        print(len(tel_li))
        #日期
        date_elements_li = self.driver.find_elements_by_xpath('//tr[@class="odd" or @class="even"]/td[6]')
        startdate_li = [date_elements.text.split('\n')[0].replace('-','') for date_elements in date_elements_li]
        enddate_li = [date_elements.text.split('\n')[1] for date_elements in date_elements_li]
        date_num_li = [date_elements.text.split('\n')[2].split('天')[0] for date_elements in date_elements_li]
        print('startdate_li:', startdate_li)
        print('enddate_li:', enddate_li)
        print('date_num_li:', date_num_li)
        #举办地点(远程为教学网站)
        address_elements_li = self.driver.find_elements_by_xpath('//tr[@class="odd" or @class="even"]/td[7]')
        address_li = [address_elements.text for address_elements in address_elements_li]
        print('address_li:', address_li)
        print(len(address_li))
        #授予学员学分
        credit_elements_li = self.driver.find_elements_by_xpath('//tr[@class="odd" or @class="even"]/td[8]')
        credit_li = [credit_elements.text.split('分')[0] for credit_elements in credit_elements_li]
        print('credit_li:', credit_li)
        print(len(credit_li))
        #教学对象
        crowd_elements_li = self.driver.find_elements_by_xpath('//tr[@class="odd" or @class="even"]/td[9]')
        crowd_li = [crowd_elements.text for crowd_elements in crowd_elements_li]
        print('crowd_li:', crowd_li)
        print(len(crowd_li))
        # 招生人数
        person_num_elements_li = self.driver.find_elements_by_xpath('//tr[@class="odd" or @class="even"]/td[10]')
        person_num_li = [person_num_elements.text.split('/')[0] for person_num_elements in person_num_elements_li]
        print('person_num_li:', person_num_li)
        print(len(person_num_li))
        #备注
        remark_elements_li = self.driver.find_elements_by_xpath('//tr[@class="odd" or @class="even"]/td[11]')
        remark_li = [remark_elements.text for remark_elements in remark_elements_li]
        print('remark_li:', remark_li)
        print(len(remark_li))

        df = pd.DataFrame({'projectId':projectId_li,
                           'project_num':project_num_li,
                           'project_name':project_name_li,
                           'company':company_li,
                           'leading_name':leading_name_li,
                           'tel':tel_li,
                           'startdate':startdate_li,
                           'enddate':enddate_li,
                           'date_num':date_num_li,
                           'address':address_li,
                           'credit':credit_li,
                           'crowd':crowd_li,
                           'person_num':person_num_li,
                           'remark':remark_li,
                           'discipline':discipline_li
                           })
        print(df)
        return df

    def verification(self,page):
        while 1:

            print(page)
            if page>1 and page<14 :
                pass

            # self.pic_code_interaction('Get_PIC')
            # src = cv.imread(r'yzm/yzm.png')
            # cv.imshow('input image', src)
            # yzm_content = self.OCR_NUM(src)
            # num_li = re.findall('\d+', yzm_content)
            # operator = re.findall('\s(.+?)\s', yzm_content)
            # print(num_li, operator)
            # if len(num_li) != 2 or not operator:
            #     self.pic_code_interaction('Refresh_PIC')
            #     continue
            # operator = operator[0]
            # operator_dic = {'加、州、办、如': '+', '减、净、冼、凑、碧、班': '-', '乘、梢、渡、粲、椿、梁、弼': '*'}
            # result = '20'
            # for i in operator_dic:
            #     if operator in i:
            #         print(num_li[0] + operator_dic[i] + num_li[1])
            #         result = int(eval(num_li[0] + operator_dic[i] + num_li[1]))
            #         print(result)
            result = input('请输入验证码：')
            print('result:',result)
            self.pic_code_interaction('send_code',result)
            if page == 1:
                self.driver.find_element_by_xpath('//input[@value="查询"]').click()
                self.driver.switch_to.frame('resultIFrame')
                time.sleep(6)
                # self.driver.switch_to.default_content()
            else:
                self.driver.switch_to.frame('resultIFrame')
                self.driver.find_element_by_xpath('//a[@title="Go to page %s"]'%page).click()
            body = self.driver.find_elements_by_xpath('//body[text()="请输入正确的计算结果"]')
            print('body',body)
            if body:
                self.driver.switch_to.default_content()
                continue
            time.sleep(2)
            df = self.get_result()
            self.driver.switch_to.default_content()
            return df


            # content_title = self.driver.find_element_by_xpath('//div[@class="mmm"]')
            # print(content_title)
if __name__ == '__main__':
    df = pd.DataFrame()
    for i in range(1,15):
        df1 = pd.read_excel('result2022-%s.xlsx'%i)
        df = pd.concat([df, df1])
    print(df)
    df.to_excel('result2022.xlsx',index=False)





