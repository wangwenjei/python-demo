"""
日志配置字典LOGGING_DIC
"""
# 日志格式 其中的%(name)s为 getlogger 时指定的名字
standard_format = '%(asctime)s - %(threadName)s:%(thread)d - 日志名字:%(name)s - %(filename)s:%(lineno)d -' \
                  '%(levelname)s - %(message)s'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

# 3、日志配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    # 设置多个日志格式,以后需要使用那个格式就调用那种
    'formatters': {
        'simple': {'format': simple_format},
        'standard': {'format': standard_format},
    },
    'filters': {},
    # handlers是日志的接收者，不同的handler会将日志输出到不同的位置
    'handlers': {
        # 控制台输出
        'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'simple'},
        # 普通日志保存到文件,切割日志
        'info_file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'standard',
            "filename": "info.log",  # os.path.join(os.path.dirname(os.path.dirname(__file__)),'log','a2.log')
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "encoding": "utf8"
        },
        # 错误日志保存到文件,切割日志
        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": 'standard',
            "filename": "errors.log",
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "encoding": "utf8"
        },
    },
    # loggers是日志的产生者,产生的日志会传递给handler然后控制输出;通过logging.getLogger(__name__)拿到的对应logger配置
    'loggers': {
        'console_log': {
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'handlers': ['console', ],  # 内配置上述定义的handler可配置多个
            'propagate': False,  # 默认为True; 向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        "info_log": {"level": "INFO", "handlers": ['info_file_handler', 'error_file_handler'], "propagate": False},
        "error_log": {"level": "ERROR", "handlers": ['error_file_handler'], "propagate": False},
        # 上面都匹配上时,默认配置
        '': {"level": "INFO", "handlers": ['console', 'info_file_handler'], "propagate": False}
    },
    # "root": {"level": "INFO", "handlers": ["console", "info_file_handler", "error_file_handler"]}
}
