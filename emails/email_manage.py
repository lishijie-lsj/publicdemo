import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailManage:
    #封装的发送邮件的方法
    def send_email(self,report_name):
        # 定义SMTP服务器
        smtpserver = 'smtp.163.com'
        # 发送邮件的用户名和客户端密码
        username = 'a672813112@163.com'
        password = 'VGXMYFEXVMTPQKYO'  # 授权密码
        # 接收邮件的邮箱
        receiver = '672813112@qq.com'
        # 创建邮件对象
        message = MIMEMultipart('related')
        subject = '自动化测试报告'  # 邮件的主题
        fujian = MIMEText(open(report_name, 'rb').read(), 'html', 'utf-8')  # 附件
        # 把邮件的信息组装到邮件对象里面
        message['form'] = username
        message['to'] = receiver
        message['subject'] = subject
        message.attach(fujian)
        # 登录smtp服务器并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(username, receiver, message.as_string())
        smtp.quit()
