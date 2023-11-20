import json
import logging

from core.ResultBase import ResultResponse
from utils.log_util import logger


def process_response(resp):
    if resp.status_code in (200, 201):
        ResultResponse.success = True
        ResultResponse.body = resp.json()
    else:
        ResultResponse.success=False
        logger.info("接口状态码返回不是2开头，请检查传参")

    # json.dumps 将python的数据格式转换为字典格式，
    # 与json.dump的区别的是，dump是转为文件流，可用文件接收
    # ensure_ascii 表示转义为中文，indent = 2 表示缩进，数据增加换行符, 数据层级以2个空格为缩进.
    logger.info("接口返回的内容为>>>："+json.dumps(resp.json(),ensure_ascii=False,indent=2))
    return ResultResponse

if __name__ == '__main__':
    a = 30
    if a in (10,20):
        print(a)
    else:
        print("meicuo")