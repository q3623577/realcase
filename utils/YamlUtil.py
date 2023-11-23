import os

import yaml

class YamlUtil:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"data/")

    def read_extract_yaml(self):
        with open(self.data_path+"extract.yaml",mode='r',encoding="utf-8") as f:
            value = yaml.safe_load(f)
            return value

    def read_testcases_yaml(self,yaml_name,key_name=None):
        """
        读取幽暗密林内容，支持传入文件名和key值
        :param yaml_name:
        :param key_name:
        :return:
        """
        with open(self.data_path+yaml_name,mode='r',encoding='UTF-8') as f:
            value = yaml.safe_load(f)
            if key_name:
                return value[key_name]
            return value

    def extract_case(self,yaml_name,key_name):
        """转换yaml内容格式，用于测试用例"""
        case_value = self.read_testcases_yaml(yaml_name,key_name)[0]
        new_case=[]
        for value in case_value['case_info']:
            new_case.append({"request_info":case_value['request_info'],'case_info':value})
        return new_case

    def write_extra_yaml(self,data:dict):
        """写入数据到yaml中，data为字典"""
        with open(self.data_path+"extract.yaml",mode='a',encoding='utf-8') as f:
            old_value = self.read_extract_yaml()
            if old_value:
                for key,value in data.items():
                    old_value[key] = value
                self.clear_extract_yaml()
                yaml.dump(data=old_value, stream=f, allow_unicode=True, sort_keys=False)
            else:
                yaml.dump(data= data,stream=f,allow_unicode=True,sort_keys=False)

    def clear_extract_yaml(self):
        """清理yaml"""
        with open(self.data_path+'extract.yaml',mode='w',encoding='utf-8') as f:
            f.truncate()

if __name__ == '__main__':
    data = {'code':200,'data':{"id":3386,'adress':"123421"}}
    YamlUtil().write_extra_yaml(data)