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
class TestDouban(unittest.TestCase):
    #从Excel中读取测试数据
    excel_handler = ExcelHandler('/Users/apple/Desktop/case.xlsx')
    data = excel_handler.read('Sheet3')
    logger = test_log("test.log")
    def setUp(self) -> None:
        self.req = RequestHandler()
    def tearDown(self) -> None:
        self.req.close_session()

    @ddt.data(*data)
    def test_register(self,test_data):
          res = self.req.visit(test_data['url'],
                       test_data['method'],
                       json=json.loads(test_data['json']))

          try:
             self.assertEqual(test_data['expected'], res['code'])


          except AssertionError as e:
             self.logger.error('测试用例执行失败{}'.format(e))
             raise e











