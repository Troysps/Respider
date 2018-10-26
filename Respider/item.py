# -*- coding: utf-8 -*-


class Item(object):
    """
    Item 数据对象
        以字典形式保存数据
        提供对外访问的接口
    """

    def __init__(self):
        self._values = {}

    def __getitem__(self, key):
        """
        item[key] return value
        :param key: dict key
        :return: value
        """
        return self._values[key]

    def __setitem__(self, key, value):
        if key not in self._values:
            self._values[key] = value
        else:
            raise KeyError("%s does not support field: %s" %
                (self.__class__.__name__, key))

    def get_value(self, key):
        """
        item.get_value(key) return value {key : value}
        :param key:
        :return:
        """
        return self.__getitem__(key)

    def get_key(self, value):
        """
        item.get_key(value) return key {key : value}
        :param value:
        :return:
        """
        return list(self._values.keys())[list(self._values.values()).index(value)]

    @property
    def data(self):
        """
        return dict data
        :return: self._values
        """
        return self._values

    def __str__(self):
        return "<%s at 0x%0x>" % (type(self).__name__, id(self))

    __repr__ = __str__

