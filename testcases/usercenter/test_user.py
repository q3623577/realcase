import allure
import pytest

from api.user_api import send_code, register, login, add_shopping_car
from testcases.usercenter.conftest import get_code, delete_user, delete_code, get_user_id, get_goods_num, set_data
from utils.read import base_data


@allure.feature("用户中心模块")
class TestUser:

    @allure.story("用户注册")
    @allure.title("使用手机号注册用例")
    @pytest.mark.skip
    def test_register(self):
        json_data = base_data.read_data()['test_register']
        # 清理最近的验证码
        delete_code(json_data["mobile"])
        # 发起获取验证码的请求
        result = send_code(json_data)
        assert result.success is True
        # 从数据库获取短信验证码
        mobile = result.body['mobile']
        code = get_code(mobile)
        # 注册用户
        register_result = register(code, mobile)
        assert register_result.success is True
        # 删除用户
        # delete_user(mobile)

    @pytest.mark.parametrize("username,password", base_data.read_data()['login_user'])
    @allure.story("用户登录")
    @allure.title("使用手机号登录")
    def test_login(self, username, password,set_data):
        # print(mobile,password)
        result = login(username, password)
        assert result.success is True
        set_data('token', result.body['token'])
        # assert result.body['token'] is True

    @allure.story("购物车")
    @allure.title("加购物车")
    def test_shopping_car(self,get_data):
        param = base_data.read_data()["shopping_car"]
        token=get_data('token')
        result = add_shopping_car(param, token)
        assert result.success is True
        user_id = get_user_id(base_data.read_data()["test_register"]["mobile"])
        goods_num = get_goods_num(user_id, result.body['goods'])
        assert result.body['nums'] == goods_num
