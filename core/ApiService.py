import allure

from core.rest_client_new import RestClient
from utils.AssertUtil import AssertUtil
from utils.ExtractUtil import ExtractUtil


class ApiService:
    def __init__(self):
        self.session = RestClient()
        self.extract = ExtractUtil()

    def handle_case(self,test_data,login_token=None):
        # 获取url
        url = self.extract.extract_url(test_data['request_info']['url'])
        # 获取method
        method = test_data['request_info']['method']
        # 获取headers
        headers = test_data['request_info']['headers']
        if login_token:
            headers.update(login_token)
        # 获取title
        allure_tile = test_data['request_info']['case_title']
        # 给allure报告定义用例标题
        allure.dynamic.title(allure_tile)
        # 获取case_info
        case_info = test_data['case_info']
        # 获取validate
        validate = case_info.pop("validate", None)
        # 获取extract
        extract = case_info.pop("extract", None)
        case_info = self.extract.extract_case(case_info)
        res = self.session.do_request(url=url, method=method, headers=headers, **case_info)
        # 将extract写入yaml
        self.extract.extract_data(res, extract)
        # 断言逻辑
        AssertUtil().validate_response(res, validate)
        return res
