import logging
from config.setting import config
loger_path = config.log_path
import os
from logging.handlers import RotatingFileHandler
def test_log(log_name):
    # 1、创建日志器
    logger = logging.getLogger(log_name)
    # 默认级别是warning  显示出来， 设置日志级别,默认的warning,显示在控制台.
    logger.setLevel('INFO')
    # 设置格式.
    formater = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s')
    #日志写入的路径.
    file_name = os.path.join(loger_path,log_name)
    # 设置日志信息显示在文本 file_hanlder.
    file_handler = RotatingFileHandler(file_name,maxBytes=20*1024*1024,backupCount=10,encoding='UTF-8')
    #控制台输出日志.
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel('INFO')   #日志输出级别.
    stream_handler.setFormatter(formater)
    file_handler.setLevel('INFO')
    file_handler.setFormatter(formater)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger



log = test_log('log1')
print(log)












