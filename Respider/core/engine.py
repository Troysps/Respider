# -*- coding: utf-8 -*-
from ..conf.default_settings import *
from ..utils.log import logger


if ASYNC_TYPE == "thread":
    from multiprocessing.dummy import Pool
    logger.info("[Async type] : <{}>".format(ASYNC_TYPE))
elif ASYNC_TYPE == "coroutine":
    from ..async.coroutine import Pool
    logger.info("[Async type] : <{}>".format(ASYNC_TYPE))
else:
    raise ImportError("Not Support async type : {}".format(ASYNC_TYPE))

import time

from ..core.downloader import Downloader
from ..core.pipeline import Pipeline
from ..core.schedule import Schedule
from ..core.spider import Spider
from ..http.request import Request
from ..item import Item
from ..middlewares.downloaderMiddlewares import DownloaderMiddleware
from ..middlewares.spiderMiddlewares import SpiderMiddleware




class Engine(object):
    """
    Engine 引擎组件
    """
    def __init__(self):
        self.spiders = self.__auto_import_instances(SPIDERS, True)
        # print('init spiders:', self.spiders)
        self.downloader = Downloader()
        self.scheduler = Schedule()
        self.pipelines = self.__auto_import_instances(PIPELINES)
        # print('init pipelines:', self.pipelines)
        self.spider_mids = self.__auto_import_instances(SPIDER_MIDDLEWARES)
        # print('init spider_mids:', self.spider_mids)

        self.downloader_mids = self.__auto_import_instances(DOWNLOADER_MIDDLEWARES)
        print('init downloader_mids:', self.downloader_mids)

        self.total_response_num = 0
        self.pool = Pool()


    def __auto_import_instances(self, path_list, is_spider=False):
        if is_spider is True:
            instances = dict()
        else:
            instances = list()

        import importlib
        for path in path_list:
            module_name = path[:path.rfind(".")]
            class_name = path[path.rfind(".")+1:]

            result = importlib.import_module(module_name)


            cls = getattr(result, class_name)

            if is_spider is True:
                instances[cls.name] = cls()
            else:
                instances.append(cls())
            # print('module name:', module_name)
            # print('class_name:', class_name)
            # print('instances:', instances)
        return instances

    def start(self):
        """
            引擎提供start() 方法做为接口供外部调用，执行整个框架代码
        """
        start = time.time()
        logger.info("Start time : {}".format(start))

        self.__start_engine()
        end = time.time()
        logger.info("End time : {}".format(end))

        logger.info("Used time : {} seconds".format((end - start)))

    def __start_engine(self):
        self.running = True
        self.pool.apply_async(func=self.__start_request)
        # self.__start_request()
        for _ in range(MAX_ASYNC_NUMBER):
            self.pool.apply_async(func=self.__execute_request_response_item, callback=self.__callback, error_callback=self.__error_callback)

        while 1:
            time.sleep(0.0001)
            if (self.total_response_num >= self.scheduler.total_request_num) and (self.scheduler.total_request_num != 0):
                self.running = False
                break

        self.pool.close()
        self.pool.join()


        # for request in self.spider.start_requests():
        #     request = self.spider_mid.process_request(request)
        #     self.schedule.add_to_queue(request)
        #
        # while 1:
        #     try:
        #         request = self.schedule.get()
        #     except Exception:
        #         return
        #
        #     request = self.downloader_mid.process_request(request)
        #     response = self.downloader.download(request)
        #     response = self.downloader_mid.process_response(response)
        #
        #     callable_parse = getattr(self.spider, request.callback, None)
        #     if callable_parse:
        #         result = callable_parse(response)
        #         if isinstance(result, Item):
        #             result = self.spider_mid.process_item(result)
        #             self.pipeline.process_item(result)
        #         elif isinstance(result, Request):
        #             result = self.spider_mid.process_request(result)
        #             result = self.spider_mid.process_request(result)
        #             self.schedule.add_to_queue(result)
        #         else:
        #             raise Exception("{} type is not support".format(type(result)))

    def __start_request(self):
        print('SPIDERS:', SPIDERS)
        print('spiders:', self.spiders)
        for spider_name, spider in self.spiders.items():
            for request in spider.start_requests():
                for spider_mid in self.spider_mids:
                    request = spider_mid.process_request(request, spider)
                request.spider_name = spider_name
                self.scheduler.add_to_queue(request)

    def __execute_request_response_item(self):
        request = self.scheduler.get()
        if request is None:
            return
        spider = self.spiders[request.spider_name]

        for downloader_mid in self.downloader_mids:
            request = downloader_mid.process_request(request, spider)
        response = self.downloader.download(request)
        for downloader_mid in self.downloader_mids:
            response = downloader_mid.process_response(response, spider)

        callable_parse = getattr(spider, request.callback, None)
        # print('[callable parse]:', callable_parse)

        if callable_parse:
            for result in callable_parse(response):
                # print('[type result]', type(result))
                if isinstance(result, Item):
                    for spider_mid in self.spider_mids:
                        result = spider_mid.process_item(result, spider)
                    for pipeline in self.pipelines:
                        pipeline.process_item(result, spider)
                elif isinstance(result, Request):
                    for spider_mid in self.spider_mids:
                        result = spider_mid.process_request(result, spider)
                    result.spider_name = request.spider_name
                    self.scheduler.add_to_queue(result)
            # else:
            #     raise Exception("{} type is not support".format(type(result)))
        else:
            logger.error("[Engine] function<execute request response item> {} spider has no parse function <{}> to callable".format(self.spider.__class__.__name__, request.callback))
        self.total_response_num += 1

    def __callback(self, _):
        if self.running:
            self.pool.apply_async(self.__execute_request_response_item, callback=self.__callback)

    def __error_callback(self, exception):
        '''异常回调函数'''
        try:
            raise exception  # 抛出异常后，才能被日志进行完整记录下来
        except Exception as e:
            logger.exception(e)

