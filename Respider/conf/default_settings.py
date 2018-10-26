#coding:utf-8

import logging

# 默认的配置
DEFAULT_LOG_LEVEL = logging.INFO    # 默认等级
DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'   # 默认日志格式
DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'  # 默认时间格式
DEFAULT_LOG_FILENAME = 'log.log'    # 默认日志文件名称



# 导入用户代码目录下的 settings文件，替换之前同名的变量值


SPIDERS = []
PIPELINES = []
SPIDER_MIDDLEWARES = []
DOWNLOADER_MIDDLEWARES = []
MAX_ASYNC_NUMBER = 3

# async type thread or coroutine
ASYNC_TYPE = 'coroutine'


# try:
#     # 导入用户代码目录下的 settings文件，替换之前同名的变量值
#     from settings import *
# except:
#     pass
