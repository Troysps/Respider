# -*- coding: utf-8 -*-

import requests

from ..http.request import Request
from ..http.response import Response


class Downloader(object):
    """
    Downloader 下载器组件
    """

    def download(self, request):
        """
        download to call __download_request
        :param request:
        :return:
        """
        return self.__download_request(request)

    def __download_request(self, request):
        """
        download request
        """

        if request.method == 'POST':
            response = requests.post(
                url=request.url,
                headers=request.headers,
                data=request.data,
                params=request.params,
                proxies=request.proxies,
                cookies=request.cookies,

            )
        elif request.method == 'GET':
            response = requests.post(
                url=request.url,
                headers=request.headers,
                params=request.params,
                proxies=request.proxies,
                cookies=request.cookies,
                timeout=request.timeout,
                allow_redirects=request.allow_redirects,
                verify=request.verify

            )
        else:
            raise ValueError("Request method is not support")

        return Response(response.url, response.status_code, response.content, response.headers)
