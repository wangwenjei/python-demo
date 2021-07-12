import logging

# 定义日志输出相关信息
logging.basicConfig(
    # 日志输出位置: 不指定默认打印到终端
    filename='access.log',

    # 日志输出格式
    format='%(asctime)s - %(name)s - %(levelname)s -%(python_modules)s:  %(message)s',

    # 时间格式
    datefmt='%Y-%m-%d %H:%M:%S %p',

    # 4、设置日志输出级别
    # critical => 50
    # error => 40
    # warning => 30
    # info => 20
    # debug => 10
    level=10,
)

logging.debug("调试日志内容 DEBUG")
logging.info("消息日志内容 INFO")
logging.warning("警告日志内容 WARNING")
logging.error("错误日志内容 ERROR")
logging.critical("严重错误内容 CRITICAL")
