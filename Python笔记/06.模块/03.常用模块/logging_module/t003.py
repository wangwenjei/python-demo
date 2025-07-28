import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 控制台
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)

# 日志文件
handler = logging.FileHandler('logfile.log')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

try:
    print(1 + 'Hello World!')
except Exception as e:
    # logger.error(e)
    # logger.error(e, exc_info=True)
    logger.exception(e)
