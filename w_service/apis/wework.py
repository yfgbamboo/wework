'''
企业微信的特有逻辑：完成access_token获取
'''
# import requests
from w_service.apis.base_api import BaseApi


class WeWork(BaseApi):
    def __init__(self,corp_id,corp_secret):
        self.token = self.get_access_token(corp_id,corp_secret)

    def get_access_token(self,corp_id,corp_secret):
        '''
        获取access_token
        :return: access_token值
        '''
        # 定义凭证
        # corp_id = "ww4d2958ea70041241"
        # corp_secret = "IUV6L5SzRwi8RqaciYGEpTBsJTiwA0PN8cDK_qeizQE"

        # url = f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        req = {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{
                "corpid":corp_id,
                "corpsecret":corp_secret
            }
        }
        # r = requests.request("GET", url)
        r = self.send_api(req)
        token = r.json()["access_token"]
        return token