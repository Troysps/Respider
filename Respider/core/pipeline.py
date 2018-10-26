# -*- coding: utf-8 -*-

class Pipeline(object):

    def process_item(self, item, spider):
        """
        process item data
        """
        return item.data
