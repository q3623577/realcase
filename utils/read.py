import configparser
import os
import yaml

# 使用os.path.join 拼接获取各配置文件的路径

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "settings.ini")
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "file", "upload.jpeg")

"""
新建文件读取类，包括读取data，ini配置和上传的文件
"""


class FileRead:

    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path
        self.file_path = file_path

    """
    读取data中的yaml数据并返回
    """

    def read_data(self):
        f = open(self.data_path, encoding="UTF-8")
        data = yaml.safe_load(f)
        return data
        # print(data_path)

    """
    读取ini配置并返回
    """

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding="UTF-8")
        return config

    """
    读取文件内容并返回
    """

    def read_file(self):
        file = open(self.file_path, 'rb')
        return {'file': ('upload.jpeg', file, "image/jpeg")}


base_data = FileRead()
