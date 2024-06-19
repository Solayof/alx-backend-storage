#!/usr/bin/env python3
"""Redis Module"""
import redis
from functools import wraps
from typing import Union, Callable, Optional
from uuid import uuid4
UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """count numbers of time calche methods are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        self._redis.incr(key)
        return method(self, *args,**kwargs)
    return wrapper


class Cache:
    """Cache class redis"""
    def __init__(self):
        """initialize instance redis db"""
        self._redis = redis.Redis()
        self._redis.flushdb

    @count_calls
    def store(self, data: UnionOfTypes):
        """
        method that takes a data argument and returns a string. The method
        should generate a random key (e.g. using uuid),
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> UnionOfTypes:
        """retrieves data with the given key"""
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """get a string"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """get an int"""
        return self.get(key, int)
