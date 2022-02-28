import time
import unittest

from HtmlTestRunner import HTMLTestRunner

from emails.email_manage import EmailManage


class TestEcshop(unittest.TestCase):

    def test_01(self):
        print('success')

if __name__ == '__main__':
    suite=unittest.defaultTestLoader.discover('./','*.py')
    files=open('./report.html','wb')
    runner=HTMLTestRunner(stream=files,title='一网通自动化测试报告',description='报告描述')
    runner.run(suite)
    files.close()   #在发送前一定要把文件流关闭
    #发送邮件
    time.sleep(3)
    EmailManage().send_email(files.name)
