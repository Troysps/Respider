#coding:utf-8

from Respider.core.engine import Engine

# from settings import *

# from spiders.baidu import BaiduSpider
# from spiders.douban import DoubanSpider

# from pipelines import BaiduPipeline1, BaiduPipeline2, DoubanPipeline1, DoubanPipeline2
# from middlewares import SpiderMiddleware1, SpiderMiddleware2, DownloaderMiddleware1, DownloaderMiddleware2


# import importlib

def main():
    engine = Engine()
    engine.start()

#     print(SPIDERS)
#     print("--" * 20)
#     for path in SPIDERS:
#         module_name = path[:path.rfind(".")]
#         class_name = path[path.rfind(".")+1:]
#         print(module_name)
#         print(class_name)
#         result = importlib.import_module(module_name)
#         print(result)

# #类对象
# #类实例化对象
#         # 获取指定的类对象
#         cls = getattr(result, class_name)
#         print(cls())
#         print(BaiduSpider())
#         #1. 获取对象的指定数据
#         #2. 获取指定文件中的类

#         print("---" * 20)

    # baidu_spider = BaiduSpider()
    # douban_spider = DoubanSpider()

    # spiders = {
    #     BaiduSpider.name : baidu_spider,
    #     DoubanSpider.name : douban_spider
    # }

    # pipelines = [
    #     BaiduPipeline1(),
    #     BaiduPipeline2(),
    #     DoubanPipeline1(),
    #     DoubanPipeline2()
    # ]

    # spider_mids = [
    #     SpiderMiddleware1(),
    #     SpiderMiddleware2(),
    # ]

    # downloader_mids = [
    #     DownloaderMiddleware1(),
    #     DownloaderMiddleware2(),
    # ]


    # engine = Engine(
    #     spiders = spiders,
    #     pipelines = pipelines,
    #     spider_mids=spider_mids,
    #     downloader_mids=downloader_mids
    # )



if __name__ == "__main__":
    main()
