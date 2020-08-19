import requests
import unittest
class TestDepPostAll(unittest.TestCase):
#班级-查询所有
    def test_classesQuery_all(self):
        url=r'http://127.0.0.1:8000/api/departments/T01/classes/'
        res=requests.get(url)
        self.assertEqual(200,res.status_code)
#班级-查询指定
    def test_classesQuery_one(self):
        url=r'http://127.0.0.1:8000/api/departments/ghi/classes/A班5/'
        res=requests.get(url)
        self.assertEqual(200,res.status_code)
#班级-列表查询
    def test_classesQuery_list(self):
        url=r'http://127.0.0.1:8000/api/departments/ghi/classes/?$cls_id_list=A班1,A班2'
        res=requests.get(url)
        self.assertEqual(200,res.status_code)
#班级-列表查询-组合查询
    def test_classesQuery_listall(self):
        url=r'http://127.0.0.1:8000/api/departments/ghi/classes/?$cls_id_list=A班1,A班2&$master_name_list=C班1,C班2'
        res=requests.get(url)
        self.assertEqual(200,res.status_code)
#班级-条件查询
    def test_classesQuery_condition(self):
        url=r'http://127.0.0.1:8000/api/departments/ghi/classes/?cls_name=B班1'
        res=requests.get(url)
        self.assertEqual(200,res.status_code)
#班级-条件查询-组合查询
    def test_classesQuery_conditionall(self):
        url=r'http://127.0.0.1:8000/api/departments/ghi/classes/?cls_name=B班5&master_name=C班5&slogan=D班5'
        res=requests.get(url)
        self.assertEqual(200,res.status_code)
#班级-模糊查询
    def test_classesQuery_vague(self):
        url=r'http://127.0.0.1:8000/api/departments/ghi/classes/?blur=1&cls_name=A班'
        res=requests.get(url)
        self.assertEqual(200,res.status_code)
#班级-模糊查询-组合查询
    def test_classesQuery_vagueall(self):
        url=r'http://127.0.0.1:8000/api/departments/ghi/classes/?blur=1&cls_name=B班&master_name=C班'
        res=requests.get(url)
        self.assertEqual(200,res.status_code)
if __name__ == '__main__':
    unittest.main()