# -*- coding: utf-8 -*-
import six
from six.moves.queue import Queue
from Respider.conf.default_settings import *

if ROLE == None:
    from six.moves.queue import Queue
    from ..queue.set import NoramlFilterContainer as Set

elif ROLE in ["master", "slave"]:
    from Respider.queue.queue import Queue as RedisQueue
    from Respider.queue.set import NoramlFilterContainer, RedisFilterContainer

else:
    raise Exception("Not Support ROLE:{}".format(ROLE))

from Respider.utils.log import logger


class Schedule(object):
    """
    Schedule 调度器组件
    """
    def __init__(self):
        self.queue = Queue()
        self.__filter_set = Set()
        self.total_request_num = 0
        self.total_repeat_num = 0

    def add_to_queue(self, request):
        """
        add request to queue if request not in __filter_set
        """
        fp = self.__get_fingerprint(request)

        if self._filter_request(fp, request):
            self.__filter_set.add_fp(fp)
            self.queue.put(request)
            self.total_request_num += 1
        else:
            self.total_repeat_num += 1

    def get(self):
        """
        get request from Schedule.queue
        :return request
        """
        try:
            request = self.queue.get_nowait()
        except:
            return None
        else:
            return request

    def _filter_request(self, fp, request):
        """
        Use set filter request
        """
        if fp in self.__filter_set:
            logger.info("Filter Request [{}] <{}>".format(request.method, request.url))
            return False
        else:
            # 如果不是重复请求，允许添加到请求队列
            return True


    def __get_fingerprint(self, request):
        """
        指纹去重
        根据url method params data  给出指纹
        """
        import w3lib.url
        url = w3lib.url.canonicalize_url(request.url)

        method = request.method.upper()
        params = request.params if request.params else {}
        params = str(sorted(params.items(), key=lambda x : x[0]))

        data = request.data if request.data else {}
        data = str(sorted(data.items(), key=lambda x: x[0]))

        from hashlib import sha1

        sha1_data = sha1()
        sha1_data.update(self.get_utf8_str(url))
        sha1_data.update(self.get_utf8_str(method))
        sha1_data.update(self.get_utf8_str(params))
        sha1_data.update(self.get_utf8_str(data))

        fp = sha1_data.hexdigest()
        return fp


    def get_utf8_str(self, string):
        """
            判断字符串类型，并将Unicode字符串编码为utf-8
        """
        if six.PY2:
            if isinstance(string, str):
                return string
            else:
                return string.encode("utf-8")
        else:
            if isinstance(string, bytes):
                return string
            else:
                return string.encode("utf-8")
