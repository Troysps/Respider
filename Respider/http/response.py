# -*- coding: utf-8 -*-


"""源码分析
    主要参数: (联想一下 requests 发送请求之后 会获得response response中有那些主>要的属性)
        headers: response headers
        status: response status
        body: response body
        url: response url
        request: 根据返回的地址 创建Request的对象
            特性:
                1. 将会应发重定向
                2. request.url != response.url
                3. 只作用与这个spider
    主要功能:
        标准化: url body headers
        flags: 包含响应标志的列表
        meta: 就是Request对象的原始标准化: headers url body
        提供接口访问body url : 设置属性只允许访问 不允许修改
        __repr__ = __str__
        提供复制功能: 新建一个一样的Response对象
        follw: 使用相对url重定向, 新建Request
"""
import json
import re
from lxml import etree


class Response(object):
    """
    Response 响应对象
    :param url -- Response url
    :param status_code -- Http status code
    :param body -- Http response body
    :param headers -- Http response headers

    """

    def __init__(self, url, status_code, body, headers):
        self.url = url
        self.status_code = status_code
        self.body = body
        self.headers = headers


    def xpath(self, rule):
        html_obj = etree.HTML(self.body)
        return html_obj.xpath(rule)


    def re_findall(self, rule, string=None):
        if string is None:
            return re.findall(rule, self.body)
        else:
            return re.findall(rule, string)

    @property
    def json(self):
        try:
            return json.loads(self.body)
        except Exception as e:
            raise e

# if __name__ == '__main__':
#     import requests
#     resp = requests.get('https://www.baidu.com/')
#
#     from lxml import etree
#     html = etree.HTML(resp.content)
#     print(html.xpath('/html/head/title/text()'))
