#coding:utf-8


from Respider.core.spider import Spider
from Respider.item import Item
from Respider.http.request import Request

class DoubanSpider(Spider):
    name = "douban"

    start_urls = ["https://movie.douban.com/top250?start=" + str(page) for page in range(0, 25, 25)]


    def parse(self, response):
        node_list = response.xpath("//div[@class='hd']")[:3]
        for node in node_list:
            item = Item()
            item = {}
            item['page_title'] = node.xpath("./a/span/text()")[0]
            item['page_link'] = node.xpath("./a/@href")[0]
            yield item
            yield Request(item['page_link'], callback="parse_page")


    def parse_page(self, response):
        item = Item()
        title = response.xpath("//head/title/text()")[0]
        item['title'] = title
        print('parse page type item', type(item))
        yield item

