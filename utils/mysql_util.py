import pymysql

from utils.log_util import logger
from utils.read import base_data

data = base_data.read_ini()['mysql']
DB_CONF = {
    'host': data["MYSQL_HOST"],
    'port': int(data["MYSQL_PORT"]),
    'user': data["MYSQL_USER"],
    'password': data["MYSQL_PASSWD"],
    'db': data["MYSQL_DB"]
}


class MysqlDb:
    def __init__(self):
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)

        # cursor=pymysql.cursors.DictCursor
        # DictCursor是pymysql库中的一个游标类型。它与其他游标类型不同之处在于，
        # 它返回的查询结果是一个字典的列表，其中字典的键是列名，值是对应列的值
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def select_db(self, sql):
        logger.info("执行的查询语句为：{}".format(sql))
        self.cur.execute(sql)
        # 获取一条查询数据
        result = self.cur.fetchone()
        logger.info("单条查询的结果为：{}".format(result))
        return result

    def select_db_all(self, sql):
        logger.info("执行的查询语句为：{}".format(sql))
        self.cur.execute(sql)
        # 获取一条查询数据
        result = self.cur.fetchone()
        logger.info("查询的全部结果为：{}".format(result))
        return result

    def execute_db(self, sql):
        try:
            logger.info("执行的sql为：{}".format(sql))
            self.cur.execute(sql)
            self.conn.commit()
            return "success"
        except Exception as e:
            logger.info("执行出错的sql：{}".format(sql))


db = MysqlDb()

if __name__ == '__main__':
    db = MysqlDb()
    result = db.select_db(
        "select code from users_verifycode where mobile = '13703490110' order by id desc ;")
    print(result['code'])