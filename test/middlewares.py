#coding:utf-8

# 爬虫中间件
class SpiderMiddleware1(object):
    def process_request(self, request, spider):
        print("[SpiderMiddleware1] process request [{}] <{}>".format(request.method, request.url))
        return request


    def process_item(self, item, spider):
        print("[SpiderMiddleware1] process item <{}>".format(type(item)))
        return item

class SpiderMiddleware2(object):
    def process_request(self, request, spider):
        print("[SpiderMiddleware2] process request [{}] <{}>".format(request.method, request.url))
        return request


    def process_item(self, item, spider):
        print("[SpiderMiddleware2] process item <{}>".format(type(item)))
        return item




# 下载中间件
class DownloaderMiddleware1(object):
    def process_request(self, request, spider):
        print("[DownloaderMiddleware1] process request [{}] <{}>".format(request.method, request.url))

        return request

    def process_response(self, response, spider):
        print("[DownloaderMiddleware1] process response [{}] <{}>".format(response.status_code, response.url))

        return response



class DownloaderMiddleware2(object):
    def process_request(self, request, spider):
        print("[DownloaderMiddleware2] process request [{}] <{}>".format(request.method, request.url))

        return request

    def process_response(self, response, spider):
        print("[DownloaderMiddleware2] process response [{}] <{}>".format(response.status_code, response.url))

        return response
