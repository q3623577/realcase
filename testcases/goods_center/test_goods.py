import allure

from api.goods_api import get_banner
from testcases.goods_center.conftest import banner_num


class TestGoods:
    @allure.story("首页展示内容")
    @allure.title("banner")
    def test_banner(self):
        result = get_banner()
        assert result.success is True
        assert len(result.body) == banner_num()
