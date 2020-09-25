import json
import sys
import os
import cx_Oracle

# sys.path.append('../')
sys.path.append('C:/Users/huangfeipeng/PycharmProjects/demo')
curPath = os.path.abspath(os.path.dirname(__file__))
from util.handle_init import handle_ini
from util.handle_log import run_log as logger


class Handledb:
    __db = None

    def __init__(self):
        self.connectiondatabase()

    def __del__(self):
        if (self.__db is not None):
            self.__db.close()

    def connectiondatabase(self):
        dbconfig = handle_ini.get_value('oracle_config', 'oracleconfig')
        db_config = json.loads(dbconfig)
        try:
            tns = cx_Oracle.makedsn(db_config['host'],1521,db_config['port'])
            self.conn = cx_Oracle.connect(db_config['username'],db_config['password'],tns)
        except:
            logger.error("connectDatabase failed")
            return False
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def closedatabase(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self, sql, params=()):
        self.connectiondatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql, params)
                rs = self.cur.fetchall()
                print(rs)

                self.conn.commit()
        except:
            logger.error("execute failed: " + sql)
            logger.error("params: " + params)
            self.closedatabase()
            return False
        return True

    # 用来查询表数据
    def select(self, sql, params=()):
        try:
            self.connectiondatabase()
            self.cur.execute(sql, params)
            result = self.cur.fetchall()
            logger.info("select success：" + sql + params)
            return result
        except Exception as e:
            logger.error("execute failed：" + sql + params)
            logger.error(e)
            return (e)


handle_db = Handledb()
if __name__ == "__main__":
    handledb = Handledb()
    sql = "select * from s_sale_order where xsqd=-2 order by xdsj desc "
    result = handledb.execute(sql)
