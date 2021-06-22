'''
工具类
公共方法
'''
import yaml
from jsonpath import jsonpath


class Utils:
    # 类方法，不需要类的实例化，可直接通过类名调用
    @classmethod
    def get_yamal_data(cls,file_path):
        '''
        封装yaml文件读取的方法
        :param file_path: yaml文件的路径
        :return: 字典格式的yaml 文件内容
        '''
        with open(file_path) as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def base_jsonpath(cls,obj,json_expr):
        '''
        封装jsonpath断言
        :param obj: 要断言的响应内容
        :param json_expr: jsonpath表达式
        :return: 提取内容的列表
        '''

        return jsonpath(obj,json_expr)