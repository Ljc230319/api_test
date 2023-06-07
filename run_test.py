import unittest
import  os
from commom.HTMLTestRunner import HTMLTestRunner
from config.setting import config
import time
from test_cases.test_diuban_login import TestDouban
#1、初始化testloader
testloader = unittest.TestLoader()
#2、查找测试用例
suite = testloader.discover(config.case_path)


#测试报告
ts = str(int(time.time()))
file_name = 'test_result_{}.html'.format(ts)
file_path = os.path.join(config.report_path,file_name)


with open(file_path,'wb') as f:
    #初始化运行器，是以普通文本生成测试报告
    runner = HTMLTestRunner(f,title='刘大帅')
    runner.run(suite)
