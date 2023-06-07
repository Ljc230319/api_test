import unittest
from commom.excel_handler import ExcelHandler
from config.setting import config
from commom.logger_handler import test_log
from commom.request_handler import RequestHandler
from middleware.helper import save_token
from commom.db_handler import DBHandler
from pymysql.cursors import DictCursor
import ddt
from config.setting import config
import json
from middleware.helper import Context,save_token

class TestRecharge(unittest.TestCase):
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('recharge')
    logger = test_log('test_rechargelog1')
    def setUp(self) -> None:
        self.res = RequestHandler()
        self.db = DBHandler(host='120.78.28.25', port=3306, user='future', password='123456',
                            charset='UTF-8', database='futureloan', cursorclass=DictCursor)
        save_token()

    def tearDown(self) -> None:
        self.res.close()
        self.db.close()
    @ddt.data(*data)
    def recharge(self,data_info):
        token = Context.token
        member_id = Context.member_id
        sql = 'select * from member where id=%s;'
        user = self.db.query(sql,args=[member_id,])      #查询充值之前数据库账户余额
        before_money = user['leave_mount']

        if "#member_id"  in  data_info['json']:
            data_info['json'] = data_info['json'].replace("#member_id",str(member_id))
        if "#wrong_member_id"  in data_info['json']:     #用户名不正确时；
            data_info['json'] = data_info['json'].replace("#wrong_member_id",str(member_id+2))
        headers = json.load(data_info['headers'])   #从excel中获取headers
        headers['Authorization'] = token     #添加Authorization信息
        res = self.res.visit(data_info['url'],data_info['method'],json=json.load(data_info['json']),headers=headers)
        money = json.load(data_info['json'])['amount']    #充值的钱
        self.assertEqual(res['code'],data_info['code'])     #断言1、判断实际结果和预期接结果
        if res['code'] == 0:      #判断是否成功用例，如果是成功用例，进行数据库校验
            #查看数据库，充值后的金额=充值前的+充值的金额
            sql = 'select * from member where id=%s;'
            user2 = self.new_db.query(sql, args=[member_id])
            after_money = user2['leave_amount']
            self.assertEqual(before_money+money,after_money)











