import logging

import requests


class BaseApi:
    # 设置Loging
    ## 定义log日志存放地址
    fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    ## 设置log日志级别
    logging.getLogger().setLevel(0)
    ## 确定日志的显示格式
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    ## 日志格式添加到fileHandler中
    fileHandler.setFormatter(formatter)
    ## 传入Logging
    logging.getLogger().addHandler(fileHandler)

    def log_info(self,msg):
        '''
        添加日志信息方法
        :return: info级别的日志
        '''
        return logging.info(msg)


    def send_api(self,req):
        '''
        对requests进行二次封装
        :return: 接口响应结果
        '''
        # req = {
        #     "method":"get",
        #     "url":"xxxx",
        #     "params":{},
        #     "json":{}
        # }
        # **req 等同于requests.request(method="get",url="xxx",params={},json={})
        self.log_info("----request data-----")
        self.log_info(req)
        r = requests.request(**req)
        self.log_info(("----response data----"))
        self.log_info(r.json())
        return r