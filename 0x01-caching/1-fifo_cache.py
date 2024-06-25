#!/usr/bin/env python3
"""FIFOCache"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class fifo cache"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to dictionary"""
        if key is not None and item is not None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")
        self.cache_data[key] = item

    def get(self, key):
        """return value"""
        return self.cache_data.get(key, None)
