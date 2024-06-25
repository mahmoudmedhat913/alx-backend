#!/usr/bin/env python3
"""basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class basic cache"""
    def put(self, key, item):
        """assign to dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return value"""
        return self.cache_data.get(key, None)
