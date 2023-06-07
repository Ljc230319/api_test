import  requests
import  json
class RequestHandler:
    def  __init__(self):
        self.session = requests.Session()
    def visit(self,method,url,params=None,data=None,json=None,headers=None,**kwargs):
        res = self.session.request(method,url,params=params,data=data,json=json,headers=headers,**kwargs)
        try:
            return res.json()
        except ValueError:
            print('not except')
    def close_session(self):
        self.session.close()


if __name__ == '__main__':
    req = RequestHandler()
    res = req.visit('post','https://vacations.ctrip.com/restapi/gateway/14422/genericDestRecommend')
    print(res)
