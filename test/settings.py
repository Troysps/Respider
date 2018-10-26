#coding:utf-8


DEFAULT_LOG_FILENAME = 'baidu.log'    # 默认日志文件名称


# 表示启用的SPIDER
SPIDERS = [
    "test.spiders.douban.DoubanSpider",
    "test.spiders.baidu.BaiduSpider",

]


PIPELINES = [
    "pipelines.BaiduPipeline1",
    "pipelines.BaiduPipeline2",
    "pipelines.DoubanPipeline1",
    "pipelines.DoubanPipeline2",
]


SPIDER_MIDDLEWARES = [
    "middlewares.SpiderMiddleware1",
    "middlewares.SpiderMiddleware2",
]


DOWNLOADER_MIDDLEWARES = [
    "middlewares.DownloaderMiddleware1",
    "middlewares.DownloaderMiddleware2",
]

# if __name__ == '__main__':
#     from gevent.pool import Pool
#
#     import gevent.monkey
#     gevent.monkey.patch_all()
#
#     class test(Pool):
#         pass