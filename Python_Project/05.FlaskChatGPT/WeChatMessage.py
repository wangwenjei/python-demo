import json
import requests
from auth.callback.WXBizMsgCrypt import WXBizMsgCrypt
from auth.config import settings
import sys
import requests
from _sha1 import sha1
import hashlib


class WeChatMes:
    CORP_ID = settings.CORP_ID
    SECRET = settings.SECRET
    Verify_URL = settings.Verify_URL
    Verify_Token = settings.Verify_Token
    Verify_EncodingAESKey = settings.Verify_EncodingAESKey

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

    def dataVerify(self, msg_signature, timestamp, nonce, echostr):
        """
            验证URL有效性
            官方文档: https://developer.work.weixin.qq.com/document/10514
        :return:
        """
        # 第一步: 验证回调URL
        wxcpt = WXBizMsgCrypt(sToken=self.Verify_Token, sReceiveId=self.CORP_ID,
                              sEncodingAESKey=self.Verify_EncodingAESKey)
        ret, sEchoStr = wxcpt.VerifyURL(sMsgSignature=msg_signature, sTimeStamp=timestamp, sNonce=nonce,
                                        sEchoStr=echostr)

        print('**********')
        print(ret)
        print(sEchoStr)
        print('**********')

        if (ret != 0):
            print("ERR: VerifyURL ret: " + str(ret))
            # sys.exit(1)
            return str(ret)

        print('===========')
        print(ret)
        print(sEchoStr)
        print('===========')

        # # 对用户回复的消息解密
        # sReqData = "<xml>" \
        #            "<ToUserName> <![CDATA[ww1436e0e65a779aee]]> </ToUserName>" \
        #            "\n<Encrypt><![CDATA[Kl7kjoSf6DMD1zh7rtrHjFaDapSCkaOnwu3bqLc5tAybhhMl9pFeK8NslNPVdMwmBQTNoW4mY7AIjeLvEl3NyeTkAgGzBhzTtRLNshw2AEew+kkYcD+Fq72Kt00fT0WnN87hGrW8SqGc+NcT3mu87Ha3dz1pSDi6GaUA6A0sqfde0VJPQbZ9U+3JWcoD4Z5jaU0y9GSh010wsHF8KZD24YhmZH4ch4Ka7ilEbjbfvhKkNL65HHL0J6EYJIZUC2pFrdkJ7MhmEbU2qARR4iQHE7wy24qy0cRX3Mfp6iELcDNfSsPGjUQVDGxQDCWjayJOpcwocugux082f49HKYg84EpHSGXAyh+/oxwaWbvL6aSDPOYuPDGOCI8jmnKiypE+]]> </Encrypt>" \
        #            "\n<AgentID> <![CDATA[1000002]]> </AgentID>" \
        #            "\n</xml>"
        #
        # ret, sMsg = wxcpt.DecryptMsg(sPostData=sReqData,
        #                              sMsgSignature=msg_signature,
        #                              sTimeStamp=timestamp,
        #                              sNonce=nonce)
        # print(ret, sMsg)
        # if (ret != 0):
        #     print("ERR: DecryptMsg ret: " + str(ret))
        #     sys.exit(1)

        # # 企业回复用户消息的加密
        # sRespData = "<xml><ToUserName>ww1436e0e65a779aee</ToUserName><FromUserName>ChenJiaShun</FromUserName><CreateTime>1476422779</CreateTime><MsgType>text</MsgType><Content>你好</Content><MsgId>1456453720</MsgId><AgentID>1000002</AgentID></xml>"
        # ret, sEncryptMsg = wxcpt.EncryptMsg(sReplyMsg=sRespData,
        #                                     sNonce=nonce,
        #                                     timestamp=timestamp)
        # if (ret != 0):
        #     print("ERR: EncryptMsg ret: " + str(ret))
        #     sys.exit(1)
        # # ret == 0 加密成功，企业需要将sEncryptMsg返回给企业号
        # # TODO:
        # # HttpUitls.SetResponse(sEncryptMsg)

        return 'ok'

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
