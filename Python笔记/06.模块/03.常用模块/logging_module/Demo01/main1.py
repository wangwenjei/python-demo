import traceback

import requests
from logging import config, getLogger
import os
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
        self.HOST = 'https://yzbapitest.wanyih.com'
        self.API = [
            '/v1/user/open/heartbeat',
            '/v1/system/open/heartbeat',
            '/v1/message/open/heartbeat',
            '/v1/flowable/open/heartbeat',
            '/v1/platform/open/heartbeat',
            '/v1/schedule/open/heartbeat',
            '/v1/datastore/open/heartbeat',
            # '/v1/file/open/heartbeat',
            # '/v1/order/open/heartbeat',
            # '/v1/payment/open/heartbeat',
            # '/v1/sync/open/heartbeat',
            # '/v1/coding/open/heartbeat',

        ]
        self.logger = logger

    def __error_action(self, module_name, error_info):
        """
        错误动作
        18501635120 魏
        """
        # 医助宝企微群
        url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b7eb066b-e169-46f5-917b-f3ae0a3f636f&debug=1'

        # 测试群
        url_3 = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=56d6ab7f-a462-4e9c-b69b-12999a6ec639&debug=1'
        headers = {'Content-Type': 'application/json'}

        msg = f"msg: {module_name}服务停止了,\ninfo: {error_info}".replace('\'', '')
        data = {
            "msgtype": "text",
            "text": {
                "content": msg,
                "mentioned_mobile_list": ["18501635120"]
            }
        }

        data = str(data).replace("'", '"').encode('utf-8')
        r = requests.post(url=url, headers=headers, data=data)
        self.logger.info(data)
        self.logger.info(r.text)

    def heartbeat(self):
        """心跳拨测"""
        url_list = []
        for api in self.API:
            url_list.append(self.HOST + api)

        for url in url_list:
            r = requests.post(url)
            health_info = r.json()

            if r.status_code == 200:
                health_info['path'] = url.split('v1')[1]
                self.logger.info(health_info)

            else:
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
                    self.__error_action(module_name=module_name, error_info=str(health_info))


if __name__ == '__main__':
    y = YzbApiHealthMonitor()
    y.heartbeat()
