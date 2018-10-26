#coding:utf-8


from Respider.core.spider import Spider
from Respider.item import Item

class BaiduSpider(Spider):
    name = "baidu"

    start_urls = [
        "http://www.baidu.com",
        "http://news.baidu.com/",
        "http://www.baidu.com"
    ]

    def parse(self, response):
        item = Item()
        title = response.xpath("//head/title/text()")[0]
        item['title'] = title
        print('parse page type item', type(item))

        yield item
