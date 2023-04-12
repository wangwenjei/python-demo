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
        self.code = {'code': 200, 'msg': ''}

    def add_file(self, file_path='', email_header='邮件默认标题', email_body='邮件默认主体内容', *args, **kwargs):
        message = MIMEMultipart()  # 多个MIME对象
        message['From'] = self.from_user  # 发件人
        message['To'] = self.to_user  # 收件人
        message['Subject'] = Header(email_header, 'utf-8')  # 邮件标题
        message.attach(MIMEText(email_body, 'plain', 'utf-8'))  # 邮件正文内容

        # 附件
        if file_path:
            "有附件则邮件添加附件"
            file_name = file_path.split('/')[-1]  # 附件文件名
            file_base = MIMEApplication(open(file_path, 'rb').read())  # 读取文件
            file_base["Content-Type"] = 'application/octet-stream'  # 设置内容类型
            file_base.add_header('Content-Disposition', 'attachment', filename=file_name)  # 添加到header信息
            message.attach(file_base)

        try:
            smtpObj = smtplib.SMTP(self.mail_host)  # 使用SSL连接邮箱服务器
            smtpObj.login(self.mail_user, self.mail_pass)  # 登录服务器
            smtpObj.sendmail(self.from_user, self.to_user_list, message.as_string())  # 发送邮件

            self.code['msg'] = '邮件发送成功'
            return self.code
        except Exception as e:
            self.code['code'] = 404
            self.code['msg'] = e
            return self.code
