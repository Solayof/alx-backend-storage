#!/usr/bin/env python3
"""Redis Module"""
import redis
from typing import Union, Callable, Optional
from uuid import uuid4
UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    """Cache class redis"""
    def __init__(self):
        """initialize instance redis db"""
        self._redis = redis.Redis()
        self._redis.flushdb


    def store(self, data: UnionOfTypes):
        """
        method that takes a data argument and returns a string. The method
        should generate a random key (e.g. using uuid),
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
