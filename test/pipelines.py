#coding:utf-8

# from Respider.core.pipline import Pipeline
# class BaiduPipeline(Pipeline):
from test.spiders.baidu import BaiduSpider
from test.spiders.douban import DoubanSpider


class BaiduPipeline1(object):
    def process_item(self, item, spider):
        if isinstance(spider, BaiduSpider):
            print(u"[BaiduPipeline1] : item data {}".format(item.data))
        return item


class BaiduPipeline2(object):
    def process_item(self, item, spider):
        if isinstance(spider, BaiduSpider):
            print(u"[BaiduPipeline2] : item data {}".format(item.data))
        return item


class DoubanPipeline1(object):
    def process_item(self, item, spider):
        if isinstance(spider, DoubanSpider):
            print(u"[DoubanPipeline1] : item data {}".format(item.data))
        return item


class DoubanPipeline2(object):
    def process_item(self, item, spider):
        if isinstance(spider, DoubanSpider):
            print(u"[DoubanPipeline2] : item data {}".format(item.data))
        return item

