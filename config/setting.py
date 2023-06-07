import os
class Config:
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(root_path,'data/case.xlsx  ') #测试数据地址
    case_path = os.path.join(root_path,'test_cases')  #测试用例地址
    report_path = os.path.join(root_path,'outputs/report')
    if not os.path.exists(report_path):
        os.makedirs(report_path)
    log_path = os.path.join(root_path,'outputs/log')
    host = 'http://120.78.128.25:8766/futureloan'

config =  Config()
print(config.root_path)

