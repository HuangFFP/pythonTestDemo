# coding=utf-8
import configparser
import os

curPath = os.path.abspath(os.path.dirname(__file__))
BasePath = os.path.abspath(os.path.join(os.getcwd().replace('\\','/'),'..'))
from util.handle_log import run_log as logger


class HandleInit:
    # 读取配置文件
    def load_ini(self):
        file_path = BasePath + "\config\config.ini"
        logger.info('file_Path{}'.format(file_path))
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding='UTF-8')
        return cf

    # 获取ini里面对应key的value
    def get_value(self, key, node=None):
        if node == None:
            node = 'Test'
        cf = self.load_ini()
        try:
            data = cf.get(node, key)
            logger.info('获取配置文件的值，node：{},key：{}, data：{}'.format(node, key, data))
        except Exception:
            logger.exception('没有获取到对应的值，node：{},key：{}'.format(node, key))
            data = None
        return data


handle_ini = HandleInit()
# if __name__ == "__main__":
#     he =  HandleInit()
#     print(he.get_value('apiurl','imooc'))
