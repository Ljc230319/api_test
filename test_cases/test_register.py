# 注册的测试用例
import unittest
import ddt
from commom.excel_handler import ExcelHandler
from config.setting import config
from commom.request_handler import RequestHandler
from commom.helper import generate_phone
import json
from commom.logger_handler import test_log
from commom.db_handler import DBHandler
import pymysql
from pymysql.cursors import DictCursor

@ddt.ddt
class TestRegister(unittest.TestCase):
    #从Excel中读取测试数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')
    logger = test_log("test.log")
    def setUp(self) -> None:
        self.req = RequestHandler()
        self.db = DBHandler(host='120.78.28.25',port=3306,user='future',password='123456',
                               charset='UTF-8',database='futureloan',cursorclass=DictCursor)
    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()
    @ddt.data(*data)
    def test_register(self,test_data):

     # 需要判断如果#exist_phone出现在了test['json']中 就生成一个随机手机号,验证手机号已经存在登陆失败的情况
          if '#exist_phone#' in test_data['json']:
            # phone = generate_phone()
             #查询数据库，找到一个手机号，直接用该号码替换
             phone = self.db.query('select * from member limit 1;')
             test_data['json'] = test_data['json'].replace('#exist_phone#',phone['phone'])    #替换

          if '#new_phone#' in test_data['json']:
             while True:         #判断 test_data['json']中是否有已经注册的手机号，如果有我们就在生成一次直到没有
                 gen_phone = generate_phone()
                 phone = self.db.query('select * from member where mobile_phone=%s;',args=[gen_phone])
                 if not phone:
                     break
             test_data['json'] = test_data['json'].replace('#new_phone#', gen_phone)

    #访问接口,得到实际结果
          res = self.req.visit(test_data['url'],
                       test_data['method'],
                       json=json.load(test_data['json']),
                       headers=json.load(test_data['headers']))

    #获取预期结果 test_data['expected']与实际结果res[code]比对
          try:
             self.assertEqual(test_data['expected'],res['code']) #断言

    #出现断言失败，要将失败的用例记录到log中
          except AssertionError as e:
             self.logger.error('测试用例执行失败{}'.format(e))
             raise e











