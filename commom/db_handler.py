import pymysql
from pymysql.cursors import DictCursor

class DBHandler:
    def __init__(self,host='120.78.28.25',port=3306,user='future',password='123456',
                               charset='UTF-8',database='futureloan',cursorclass=DictCursor):
        self.conn = pymysql.connect(host=host,port=port,user=user,password=password,
                               charset=charset,database=database,cursorclass=cursorclass)       #链接数据库
        self.cursor = self.conn.cursor()     #创建游标

    def query(self,sql,args=None,one=True):
        self.cursor.execute(sql,args)      #执行sql语句
        self.conn.commit()     #提交事务
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
