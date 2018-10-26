# -*- coding: utf-8 -*-
from ..utils.log import logger

class DownloaderMiddleware(object):
    """
    Downloader Middleware 下载器中间件组件
    """

    def process_request(self, request):
        """
        处理request
        """
        logger.info("[DownloaderMiddleware] process request [{}] <{}>".format(request.method, request.url))
        return request

    def process_response(self, response):
        """
        处理response
        """
        logger.info("[DownloaderMiddleware] process response [{}] <{}>".format(response.status_code, response.url))

        return response