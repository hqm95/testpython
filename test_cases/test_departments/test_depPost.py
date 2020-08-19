import requests
import unittest
class TestDepPostAll(unittest.TestCase):
    def setUp(self) -> None:
        self.url=r'http://127.0.0.1:8000/api/departments/'
        self.req_head = {"Content-Type": "application/json"}
    def tearDown(self) -> None:
         pass
#新增学院信息-覆盖所有参数
    def test_depPost_all(self):
        req_data = r'{"data":[{"dep_id":"B11","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201,res.status_code)
#覆盖所有必填参数
    def test_depPost_notall(self):
        req_data = r'{"data":[{"dep_id":"B12","dep_name":"Test学院","master_name":"Test-Master","slogan":""}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201, res.status_code)
#depid必填为空
    def test_depPost_depidnull(self):
        req_data = r'{"data":[{"dep_id":"","dep_name":"Test学院","master_name":"Test-Master","slogan":"123"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(400, res.status_code)
        self.assertIn("为空",res.text,"该字段为空")
#depname必填为空
    def test_depPost_depnamenull(self):
        req_data = r'{"data":[{"dep_id":"B13","dep_name":"","master_name":"Test-Master","slogan":"123"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201, res.status_code)
#mastername必填为空
    def test_depPost_Depmasternamenull(self):
        req_data = r'{"data":[{"dep_id":"B14","dep_name":"Test","master_name":"","slogan":"123"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201, res.status_code)
#depid必填参数缺失
    def test_depPost_Depidlack(self):
        req_data = r'{"data":[{"dep_name":"Test","master_name":"master","slogan":"123"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201, res.status_code)
#depname必填参数缺失
    def test_depPost_Depnamelack(self):
        req_data = r'{"data":[{"dep_id":"B15","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201,res.status_code)
#masternmae必填参数缺失
    def test_depPost_Masternamelack(self):
        req_data = r'{"data":[{"dep_id":"B16","dep_name":"Test学院","slogan":"Here is Slogan"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201,res.status_code)
#depid必填参数冗余
    def test_depPost_depidAdd1(self):
        req_data = r'{"data":[{"dep_id":"B17","dep_name":"Test学院","master_name":"Test-Master","slogan":"123","dep_id":"T17"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201,res.status_code)
#depid必填参数冗余
    def test_depPost_depidAdd2(self):
        req_data = r'{"data":[{"dep_id":"B18","dep_name":"Test学院","master_name":"Test-Master","slogan":"123","dep_id":"不知道"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201,res.status_code)
#depid参数类型错误
    def test_depPost_depidParameterWrong(self):
        req_data = r'{"data":[{"dep_id":True,"dep_name":"Test学院","master_name":"Test-Master","slogan":"Slogan"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201,res.status_code)
#depname参数类型错误
    def test_depPost_depnameParameterWrong(self):
        req_data = r'{"data":[{"dep_id":"B19","dep_name":12.1,"master_name":"Test-Master","slogan":"Slogan"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201,res.status_code)
#mastername参数类型错误
    def test_depPost_MasternameParameterWrong(self):
        req_data = r'{"data":[{"dep_id":"B20","dep_name":"Test","master_name":False,"slogan":"Slogan"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201,res.status_code)
# slogan参数类型错误
    def test_depPost_SloganParameterWrong(self):
        req_data = r'{"data":[{"dep_id":"B21","dep_name":"Test","master_name":False,"slogan":12.1}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201,res.status_code)
#所有参数取最大值
    def test_depPost_Max(self):
        req_data = r'{"data":[{"dep_id":"乌鲁木齐123456","dep_name":"乌鲁木齐美美美美美美美美美美美美美美美美","master_name":"乌鲁木齐美美美美美美美美美美美美美美美美","slogan":"乌鲁木齐美美美美美美美美美美美美美美美美乌鲁木齐美美美美美美美美美美美美美美美美乌鲁木齐美美美美美美美美美美美美美美美美乌鲁木齐美美美美美美美美美美美美美美美美乌鲁木齐美美美美美美美美美美美美美美美美"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201,res.status_code)
#所有参数取最小值
    def test_depPost_Min(self):
        req_data = r'{"data":[{"dep_id":"好","dep_name":"鲁","master_name":"木","slogan":"齐"}]}'
        res = requests.post(self.url, data=req_data.encode('utf-8'), headers=self.req_head)
        self.assertEqual(201,res.status_code)
if __name__ == '__main__':
    unittest.main()