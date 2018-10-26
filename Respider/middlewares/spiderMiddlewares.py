# -*- coding: utf-8 -*-
from ..utils.log import logger

class SpiderMiddleware(object):
    """
    Spider Middleware 爬虫中间件
    """

    def process_request(self, request):
        """
        处理request
        """
        logger.info("[SpiderMiddleware] process request [{}] <{}>".format(request.method, request.url))

        return request

    def process_item(self, item):
        """
        处理item
        """
        logger.info("[SpiderMiddleware] process item <{}>".format(type(item)))

        return item
