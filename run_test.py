import requests
import unittest
import time
import common.HTMLTestRunnerNew as HT
#设置装这些用例的容器
suite=unittest.TestSuite()
#发现这些用例的工具
load=unittest.defaultTestLoader
#load发现用例
testcases=load.discover('test_cases',pattern='test*.py',top_level_dir=None)
#发现的用例放在容器中
suite.addTests(testcases)
#设置测试报告的文档名字——固定的名字reporter+当前系统时间+.html
#currenttime=time.strftime("%Y-%m-%d %H-%M-%S")
filename=r'report/reporter.html'
#生成测试报告
with open(filename,'wb+') as fp:
    runner=HT.HTMLTestRunner(stream=fp,
                             title='学生管理系统接口测试报告',
                             description='测试',
                             tester="张三")
    runner.run(suite)