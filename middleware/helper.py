from commom.request_handler import RequestHandler
from jsonpath import jsonpath
from commom.db_handler import DBHandler
def login():
    req = RequestHandler()
    res = req.visit('http://120.78.128.25:8766/futureloan','post',headers="{'X-Lemoban-Media-Type':'Lemonban.v2'}",
              json="{'mobile_phone':'13621377750','pwd':'12345678'}")
    return res


def save_token():
    data = login()
    member_id = jsonpath(data,'$..member_id')[0]
    token = jsonpath(data,'$..token')[0]
    token_type = jsonpath(data,'$..token_type')[0]
    token = " ".join([token_type,token])
    return token,member_id
def load_id():
    data1 = login()


class Context:
    """将token作为类属性"""
    token = ''
    member_id = ''


if __name__ == '__main__':

    print(save_token())
