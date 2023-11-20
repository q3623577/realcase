# 获取短信验证码
import pytest

from utils.log_util import logger
from utils.mysql_util import db

public_data = {}


@pytest.fixture(scope='function')
def set_data():
    def _set_data(key, value):
        public_data[key] = value
    return _set_data


@pytest.fixture(scope='function')
def get_data():
    def _get_data(key):
        return public_data.get(key)
    return _get_data


def get_code(mobile):
    sql = "select code from users_verifycode where mobile = {} order by id desc ;".format(mobile)
    result = db.select_db(sql)
    logger.info("手机号 {0} 获取到的验证码为：{1}".format(mobile, result['code']))
    return result['code']


def delete_user(mobile):
    sql = "delete from users_userprofile where mobile = {};".format(mobile)
    result = db.execute_db(sql)
    logger.info("删除用户的结果为：{}".format(result))


# 删除用户验证码
def delete_code(mobile):
    sql = "delete from users_verifycode where mobile = {};".format(mobile)
    result = db.execute_db(sql)
    logger.info("重置验证码结果为：{}".format(result))


def get_user_id(mobile):
    sql = "select id from users_userprofile where mobile = {} ".format(mobile)
    result = db.select_db(sql)
    logger.info("获取的用户id为：{}".format(result))
    return result['id']


def get_goods_num(user_id, goods_id):
    sql = f"select goods_id,nums from trade_shoppingcart where user_id = {user_id} and goods_id = {goods_id} "
    result = db.select_db(sql)['nums']
    logger.info("用户：{} 的购物车中，货物id为：{} 的商品数量为：{} ".format(user_id, goods_id, result))
    return result
# get_code(13703490110)
