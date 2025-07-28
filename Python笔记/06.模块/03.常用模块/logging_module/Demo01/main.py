import traceback

import requests
from logging import config, getLogger
import time
import json

LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {'simple': {'format': '[%(asctime)s] - [%(filename)s:%(lineno)d] - [%(levelname)s]  %(message)s'}, },
    'filters': {},
    'handlers': {
        'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'simple'},
        'info_file_handler': {'class': 'logging.handlers.RotatingFileHandler', 'level': 'INFO',
                              'formatter': 'simple', "filename": "info.log", "maxBytes": 1024 * 1024 * 128, "backupCount": 5, "encoding": "utf8"},
    },
    'loggers': {
        'console_log': {'level': 'DEBUG', 'handlers': ['console', ], 'propagate': False, },
        "info_log": {"level": "INFO", "handlers": ['console', 'info_file_handler'], "propagate": False},
        '': {"level": "INFO", "handlers": ['console', 'info_file_handler'], "propagate": False}
    },
}

config.dictConfig(LOGGING_DIC)
# logger = getLogger('console_log')
logger = getLogger('info_log')


class YzbApiHealthMonitor:
    """医助宝模块监控拨测监控"""

    def __init__(self):
        # self.HOST = 'https://yzbapitest.wanyih.com'
        self.HOST = 'https://yzbapi.wanyih.com'
        self.API = [
            '/v1/user/open/heartbeat',
            '/v1/system/open/heartbeat',
            '/v1/message/open/heartbeat',
            '/v1/flowable/open/heartbeat',
            '/v1/platform/open/heartbeat',
            '/v1/schedule/open/heartbeat',
            '/v1/datastore/open/heartbeat',
            '/v1/file/open/heartbeat',
            '/v1/order/open/heartbeat',
            '/v1/payment/open/heartbeat',
            '/v1/sync/open/heartbeat',
            '/v1/coding/open/heartbeat',

        ]
        self.logger = logger
        self.qywxSecretKey = '56d6ab7f-a462-4e9c-b69b-12999a6ec639'
        self.warning_phone = ["18501635120"]

    def __wechat_warn(self, module_name, error_info):
        """
            企业微信错误提醒
            18501635120 魏
        """
        # 测试群
        url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={self.qywxSecretKey}&debug=1'
        headers = {'Content-Type': 'application/json'}

        msg = f"msg: {module_name}服务停止了,\ninfo: {error_info}".replace('\'', '')
        data = {
            "msgtype": "text",
            "text": {
                "content": msg,
                "mentioned_mobile_list": self.warning_phone
            }
        }

        data = str(data).replace("'", '"')
        r = requests.post(url=url, headers=headers, data=data.encode('utf-8'))
        self.logger.info(data)
        self.logger.info(r.text)

    def __error_action(self, health_info, url):
        """错误动作"""
        self.logger.error(health_info)

        module_name = url.split('v1')[1].split('/')[1]
        with open(r'./WeChat.json', mode="rt", encoding='utf-8') as f:
            data = json.load(f)

        # print(data.get(module_name))
        # 判断,连续五分钟内只触发一次错误报警动作
        old_time = data.get(module_name)['time']
        old_timestamp = time.mktime(time.strptime(old_time, "%Y-%m-%d %H:%M:%S")) + 60 * 5
        if old_timestamp > time.time():
            self.logger.info(f'{module_name}错误,五分钟内重复不触发报警动作')
        else:
            data[module_name]['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_input = json.dumps(data)
            with open(f'./WeChat.json', mode="wt", encoding='utf-8') as f:
                f.write(data_input)
                f.flush()
            self.logger.info('触发错误动作')
            self.__wechat_warn(module_name=module_name, error_info=str(health_info))

    def heartbeat(self):
        """心跳拨测"""
        url_list = []
        for api in self.API:
            url_list.append(self.HOST + api)

        for url in url_list:
            r = requests.post(url)
            health_info = r.json()

            if r.status_code == 200 and health_info.get('code') == 200:
                health_info['path'] = url.split('v1')[1]
                self.logger.info(health_info)

            if r.status_code != 200 or health_info.get('code') != 200:
                self.__error_action(health_info=health_info, url=url)


if __name__ == '__main__':
    y = YzbApiHealthMonitor()
    y.heartbeat()
