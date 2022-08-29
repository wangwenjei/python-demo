import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication


class SendEmail:
    def __init__(self, mail_host, mail_user, mail_pass, from_user, to_user, *args, **kwargs):
        self.mail_host = mail_host  # 设置服务器
        self.mail_user = mail_user  # 用户名
        self.mail_pass = mail_pass  # 口令
        self.from_user = from_user  # 邮件发送者
        self.to_user_list = to_user.split(',')  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        self.to_user = to_user

    def message_config(self, email_header='邮件默认标题', email_body='邮件默认主体内容', *args, **kwargs):
        message = MIMEMultipart()  # 多个MIME对象
        message['From'] = self.from_user  # 发件人
        message['To'] = self.to_user  # 收件人
        message['Subject'] = Header(email_header, 'utf-8')  # 邮件标题
        message.attach(MIMEText(email_body, 'plain', 'utf-8'))  # 邮件正文内容

        try:
            smtpObj = smtplib.SMTP(self.mail_host)  # 使用SSL连接邮箱服务器
            smtpObj.login(self.mail_user, self.mail_pass)  # 登录服务器
            smtpObj.sendmail(self.from_user, self.to_user_list, message.as_string())  # 发送邮件
            print("邮件发送成功")
        except Exception as e:
            print(e)

    def add_txt(self, email_header='邮件默认标题', email_body='邮件默认主体内容', *args, **kwargs):
        message = MIMEMultipart()  # 多个MIME对象
        message['From'] = self.from_user  # 发件人
        message['To'] = self.to_user  # 收件人
        message['Subject'] = Header(email_header, 'utf-8')  # 邮件标题
        message.attach(MIMEText(email_body, 'plain', 'utf-8'))  # 邮件正文内容

        try:
            smtpObj = smtplib.SMTP(self.mail_host)  # 使用SSL连接邮箱服务器
            smtpObj.login(self.mail_user, self.mail_pass)  # 登录服务器
            smtpObj.sendmail(self.from_user, self.to_user_list, message.as_string())  # 发送邮件
            print("邮件发送成功")
        except Exception as e:
            print(e)

    def add_excel(self, file_path, email_header='邮件默认标题', email_body='邮件默认主体内容', *args, **kwargs):
        message = MIMEMultipart()  # 多个MIME对象
        message['From'] = self.from_user  # 发件人
        message['To'] = self.to_user  # 收件人
        message['Subject'] = Header(email_header, 'utf-8')  # 邮件标题
        message.attach(MIMEText(email_body, 'plain', 'utf-8'))  # 邮件正文内容

        file_name = file_path  # 文件名
        xlsx = MIMEApplication(open(file_path, 'rb').read())  # 打开Excel,读取Excel文件
        xlsx["Content-Type"] = 'application/octet-stream'  # 设置内容类型
        xlsx.add_header('Content-Disposition', 'attachment', filename=file_name)  # 添加到header信息
        message.attach(xlsx)

        try:
            smtpObj = smtplib.SMTP(self.mail_host)  # 使用SSL连接邮箱服务器
            smtpObj.login(self.mail_user, self.mail_pass)  # 登录服务器
            smtpObj.sendmail(self.from_user, self.to_user_list, message.as_string())  # 发送邮件
            print("邮件发送成功")
        except Exception as e:
            print(e)


class SendEmailAccessory(SendEmail):
    def __init__(self, mail_host, mail_user, mail_pass, from_user, to_user, *args, **kwargs):
        super().__init__(mail_host, mail_user, mail_pass, from_user, to_user, *args, **kwargs)
        self.ss = SendEmail(
            mail_host, mail_user, mail_pass, from_user, to_user, *args, **kwargs
        )

    def add_txt(self):
        self.ss.message_config()
        print(111)

    def add_excel(self):
        pass

    def sed_email(self):
        pass


a = SendEmail(
    mail_host="smtpdm.aliyun.com",
    mail_user="summer_wwj@email.wangwenjie520.com",
    mail_pass="0S03z1nzRVodB57qRY30",
    from_user='summer_wwj@email.wangwenjie520.com',
    to_user="wwj2254964433@163.com,2254964433@qq.com"
)

# a.message_config()
a.add_excel(file_path='2')