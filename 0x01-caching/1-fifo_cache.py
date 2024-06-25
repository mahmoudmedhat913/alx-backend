#!/usr/bin/env python3

"""task 1 FIFO Cache"""


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class fifo cache"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """return value"""
        return self.cache_data.get(key, None)
