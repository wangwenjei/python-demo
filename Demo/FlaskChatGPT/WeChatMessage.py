import json
import requests

'''
本文件主要实现通过企业微信应用给企业成员发消息
'''

class WeChatMes:
    CORP_ID = "xxx"
    SECRET = "xxxx"
    s = requests.session()  # 添加session缓存,避免因频繁调用接口导致被拦截

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        """
            获取access_token
            官方文档:  https://developer.work.weixin.qq.com/document/10013#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96access_token
            :return: access_token
        """
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}'.format(ID=self.CORP_ID,
                                                                                                    SECRET=self.SECRET)
        rep = self.s.get(url)
        if rep.status_code != 200:
            print('request failed!!!')
            return
        return json.loads(rep.content)['access_token']

    def send_message(self, content):
        """
            调用企业微信应用发生消息
            官方文档: https://developer.work.weixin.qq.com/document/path/94677#%E8%8F%9C%E5%8D%95%E6%B6%88%E6%81%AF
            :return:
        """
        url = 'https://qyapi.weixin.qq.com/cgi-bin/kf/send_msg?access_token={ACCESS_TOKEN}'.format(
            ACCESS_TOKEN=self.token)
        header = {
            "Content-Type": "application/json"
        }
        form_data = {
            "touser": "WangWenJie",  # 接收人
            "toparty": "chatapi",
            "msgtype": "text",  # 消息类型
            "agentid": 1000004,  # 应用ID
            "text": {
                "content": content
            },
            "safe": 0
        }
        rep = self.s.post(url, data=json.dumps(form_data).encode('utf-8'), headers=header)
        if rep.status_code != 200:
            print("request failed!!!")
            return
        print(rep.__dict__)
        return json.loads(rep.content)

    def send_message_robot(self):
        """
            调用企业微信机器人发送消息
            :return:
        """
        pass
