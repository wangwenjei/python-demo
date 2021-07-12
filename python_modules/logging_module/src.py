# 导入模块获取 LOGGING_DIC 变量
import settings
from logging import config,getLogger

# 加载配置
config.dictConfig(settings.LOGGING_DIC)

# logger1 = getLogger('kkk')
# logger1.info("消息日志内容 INFO")

logger2 = getLogger('终端提示')
logger2.info("消息日志内容 INFO")

# 当找不到相应的loggers名,则使用 '' 该logger
logger3 = getLogger('用户日志')
logger3.debug("消息日志内容 DEBUG")

# 拿到日志的产生者,即loggers