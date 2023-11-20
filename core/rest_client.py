import json
import requests

from utils.read import base_data
from utils.log_util import logger

api_root_url = base_data.read_ini()['host']['api_sit_url']


class RestClient:
    def __init__(self):
        self.api_root_url = api_root_url
        self.session = requests.Session()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, **kwargs):
        return self.request(url, "POST", **kwargs)

    def put(self, url, **kwargs):
        return self.request(url, "PUT", **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def request(self, url, method, **kwargs):
        # 每次接口请求时，打印对应请求的相关信息
        self.request_log(url, method, **kwargs)
        # 使用requests.request()替代方法判断
        return self.session.request(method=method, url=api_root_url+url, **kwargs)

        # if method == "GET":
        #     return self.session.get(self.api_root_url + url, **kwargs)
        # if method == "POST":
        #     return self.session.post(self.api_root_url + url, **kwargs)
        # if method == "PUT":
        #     return self.session.put(self.api_root_url + url, **kwargs)
        # if method == "DELETE":
        #     return self.session.delete(self.api_root_url + url, **kwargs)

    def request_log(self, url, method, **kwargs):
        '''for循环优化一下？'''
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")

        logger.info("接口请求的地址>>>{}".format(self.api_root_url + url))
        logger.info("接口请求的方法>>>{}".format(method))

        # 判断传参数据是否为空，不为空的打印输出到日志
        if data is not None:
            logger.info("接口请求的data参数>>>\n{}".format(json.dumps(data, ensure_ascii=False, indent=2)))
        if json_data is not None:
            logger.info("接口请求的json参数>>>\n{}".format(json.dumps(json_data, ensure_ascii=False, indent=2)))
        if params is not None:
            logger.info("接口请求的params参数>>>\n{}".format(json.dumps(params, ensure_ascii=False, indent=2)))
        if headers is not None:
            logger.info("接口请求的headers参数>>>\n{}".format(json.dumps(headers, ensure_ascii=False, indent=2)))



