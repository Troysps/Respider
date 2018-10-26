# -*- coding: utf-8 -*-
from Respider.http.request import Request


class Spider(object):
    """
    Spider 爬虫组件
        1. start_requests() 初始化start_urls, 传入Request请求对象
        2. parse() 解析Response返回对象数据, 传入Item对象中
    """
    name = 'baidu_spider'
    start_urls = ['http://www.baidu.com']


    def __init__(self, name=None, **kwargs):
        if name is not None:
            self.name = name
        elif not getattr(self, 'name', None):
            raise ValueError("{} class must have a name".format(self.__class__.__name__))
        if not hasattr(self, 'start_urls'):
            self.start_urls = []


    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url)

    def parse(self, response):
        """
        Must override method return Request or Item
        :return Request =====> Schedule
        :return Item    =====> Pipeline

        """
        raise NotImplementedError("{}.parse callback is not defined".format(self.__class__.__name__))

    def __str__(self):
        return "<%s %r at 0x%0x>" % (type(self).__name__, self.name, id(self))

    __repr__ = __str__


if __name__ == '__main__':
    test = Spider()
    parse = getattr(test, "parse", None)
    print(parse)
