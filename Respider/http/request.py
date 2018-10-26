# -*- coding: utf-8 -*-

"""class Request 主要实现功能 -- 与requests 库联想起来
    分析主要参数
    1. url 去重的几个重要条件 实例化时需要创建
        encoding default 'utf8'
        method  'GET'   to bytes 
        url     url     to bytes
        body    request body to bytes
    2. callback errback 回调函数 以及处理回调函数报错
        callback 主要实现的方法为callable 判断该函数是否为可以调用的对象方法
        errback 必须要有callback 否则有没有errback都没有作用
        使用断言 满足该'充分不必要条件'
    3. meta 以字典形式传递一些参数 对外提供接口可以访问 但是无法修改
    4. headers 标准化 headers
    5. dont_filter url去重设置 默认为False 不进行去重
    6. flags : Flags sent to the request, can be used for logging or similar purposes
    7. copy 返回一个Request对象的复制信息
    8. proxy 代理
    9. formdata 表单数据
"""


class Request(object):
    """
    Request 请求对象
    :param method -- method for the new Request object.
    :param url -- URL for the new Request object.
    :param params -- (optional) Dictionary or bytes to be sent in the query string for the Request.
    :param data -- (optional) Dictionary or list of tuples [(key, value)] (will be form-encoded), bytes, or file-like object to send in the body of the Request.
    :param json -- (optional) json data to send in the body of the Request.
    :param headers -- (optional) Dictionary of HTTP Headers to send with the Request.
    :param cookies -- (optional) Dict or CookieJar object to send with the Request.
    :param timeout (float or tuple) -- (optional) How many seconds to wait for the server to send data before giving up, as a float, or a (connect timeout, read timeout) tuple.
    :param allow_redirects (bool) -- (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to True.
    :param proxies -- (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify -- (optional) Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to True.
    :param encoding -- default utf-8

    :param meta -- Used dict to pass additional data
    :dont_filter --  filter request base on method url body encoding

    **kwargs
    :param files -- (optional) Dictionary of 'name': file-like-objects (or {'name': file-tuple}) for multipart encoding upload. file-tuple can be a 2-tuple ('filename', fileobj), 3-tuple ('filename', fileobj, 'content_type') or a 4-tuple ('filename', fileobj, 'content_type', custom_headers), where 'content-type' is a string defining the content type of the given file and custom_headers a dict-like object containing additional headers to add for the file.
    :param auth -- (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param stream -- (optional) if False, the response content will be immediately downloaded.
    :param cert -- (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.


    """
    def __init__(self,
                 url, method = 'GET', params = None, data = None, json = None, headers = None,
                 cookies = None, timeout = None, allow_redirects = True, callback = 'parse',
                 proxies = None, meta = None, dont_filter  = False, encoding = 'UTF-8', verify = True
                 ):

        self.method = method.upper()
        self.url = url
        self.params = params
        self.data = data
        self.json = json
        self.headers = headers
        self.cookies = cookies
        self.timeout = timeout
        self.allow_redirects = allow_redirects
        self.proxies = proxies
        self.meta = dict(meta) if meta else None
        self.dont_filter = dont_filter
        self.encoding = encoding
        self.callback = callback
        self.verify = verify


# if __name__ == '__main__':
#     test = Request(url='xxx')