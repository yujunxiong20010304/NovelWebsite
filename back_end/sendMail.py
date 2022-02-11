import smtplib
from email.mime.text import MIMEText
import random

class sendMail(object):
    # content 邮件的内容
    def __init__(self, receivingEmailAddress, content):
        # 发件人的邮件地址
        self.e_mail_address = '2140585762@qq.com'
        # 发件人的授权码
        self.e_mail_grant_authorization = 'vsplybazxxbycide'
        # 收件人的邮件地址
        self.receivingEmailAddress = receivingEmailAddress
        # 邮件主题
        self.theme = '黄金屋注册验证码'
        self.msg = MIMEText(content, 'plain', 'utf-8')
        self.msg['Subject'] = self.theme
        self.msg['From'] = self.e_mail_address
        self.msg['To'] = self.receivingEmailAddress
        self.client = None

    def send_out_email(self):
        try:
            self.client = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
            print("连接到邮件服务器成功")
            self.client.login(self.e_mail_address, self.e_mail_grant_authorization)
            print("登录成功")
            self.client.sendmail(self.e_mail_address, self.receivingEmailAddress, self.msg.as_string())
            print('发送成功')
        except smtplib.SMTPException as e:
            print('发送邮件异常')
        finally:
            self.client.quit()


if __name__ == '__main__':
    test = sendMail('2713670062@qq.com', 'huhuhu')
    test.send_out_email()

