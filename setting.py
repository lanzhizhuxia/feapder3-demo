# -*- coding: utf-8 -*-
"""爬虫配置文件"""
import os


# MYSQL
MYSQL_IP = "192.168.132.123"
MYSQL_PORT = 3306
MYSQL_DB = "feapder"
MYSQL_USER_NAME = "feapder"
MYSQL_USER_PASS = "feapder123"

# REDIS
# IP:PORT
REDISDB_IP_PORTS = "192.168.132.123:32768"
REDISDB_USER_PASS = ""
REDISDB_DB = 0

# # 爬虫相关
# # COLLECTOR
COLLECTOR_SLEEP_TIME = 1 # 从任务队列中获取任务到内存队列的间隔
COLLECTOR_TASK_COUNT = 100 # 每次获取任务数量
#
# # SPIDER
SPIDER_THREAD_COUNT = 1 # 爬虫并发数
# SPIDER_SLEEP_TIME = 0 # 下载时间间隔（解析完一个response后休眠时间）
SPIDER_MAX_RETRY_TIMES = 0 # 每个请求最大重试次数

# # 重新尝试失败的requests 当requests重试次数超过允许的最大重试次数算失败
# RETRY_FAILED_REQUESTS = False
# # request 超时时间，超过这个时间重新做（不是网络请求的超时时间）单位秒
# REQUEST_LOST_TIMEOUT = 600  # 10分钟
# # 保存失败的request
# SAVE_FAILED_REQUEST = True
#
# # 下载缓存 利用redis缓存，由于内存小，所以仅供测试时使用
# RESPONSE_CACHED_ENABLE = False  # 是否启用下载缓存 成本高的数据或容易变需求的数据，建议设置为True
# RESPONSE_CACHED_EXPIRE_TIME = 3600  # 缓存时间 秒
# RESPONSE_CACHED_USED = False  # 是否使用缓存 补采数据时可设置为True
#
# WARNING_FAILED_COUNT = 1000  # 任务失败数 超过WARNING_FAILED_COUNT则报警
#
# # 爬虫初始化工作
# # 爬虫是否常驻
# KEEP_ALIVE = True
#
# # 设置代理
# PROXY_EXTRACT_API = None  # 代理提取API ，返回的代理分割符为\r\n
# PROXY_ENABLE = True
#
# # 随机headers
# RANDOM_HEADERS = True
# # requests 使用session
# USE_SESSION = False
#
# # 去重
# ITEM_FILTER_ENABLE = False # item 去重
# REQUEST_FILTER_ENABLE = False # request 去重
#
# # 报警
# DINGDING_WARNING_URL = "" # 钉钉机器人api
# DINGDING_WARNING_PHONE = "" # 报警人
# LINGXI_TOKEN = "" # 灵犀报警token
#
#LOG_NAME = os.path.basename(os.getcwd())
#LOG_PATH = "log/%s.log" % LOG_NAME  # log存储路径
LOG_LEVEL = "INFO"
LOG_IS_WRITE_TO_FILE = True  # 是否写文件
LOG_MODE = "w"  # 写文件的模式
LOG_MAX_BYTES = 10 * 1024 * 1024  # 每个日志文件的最大字节数
LOG_BACKUP_COUNT = 20  # 日志文件保留数量
LOG_ENCODING = "utf8"  # 日志文件编码
# LOG_IS_WRITE_TO_FILE = False
# OTHERS_LOG_LEVAL = "ERROR"  # 第三方库的log等级
