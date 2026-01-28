# Copyright (c) ZakuroAI. All rights reserved.
# Licensed under the ZakuroAI License. See LICENSE for details.
"""Pure function caching via content-addressable hashing."""

import hashlib
import json

from zakuro_cache import ZakuroCache
from zakuro_cache.loggers import Capturing

cache = ZakuroCache()


def exec(hash, func, args, kwargs):
    """Execute *func* and store its result and captured stdout in the cache.

    Parameters
    ----------
    hash : str
        MD5 hex digest used as the cache key.
    func : callable
        The function to execute.
    args : tuple
        Positional arguments forwarded to *func*.
    kwargs : dict
        Keyword arguments forwarded to *func*.
    """
    with Capturing() as logger:
        cache.set(hash, func(*args, **kwargs))
        cache.set_logger(hash, logger)


def pure(func):
    """Decorator that caches a function's return value based on its arguments.

    The decorated function's positional and keyword arguments are serialised
    to JSON together with the function's qualified name, then hashed with
    MD5 to produce a cache key.  Subsequent calls with the same arguments
    return the cached result and replay any captured stdout output.

    Parameters
    ----------
    func : callable
        The function to wrap with caching behaviour.

    Returns
    -------
    callable
        A wrapper that transparently caches *func*.
    """

    def wrapper(*args, **kwargs):
        global cache
        key = json.dumps(
            {
                "args": args,
                "kwargs": kwargs,
                "call": "@".join([func.__name__, func.__module__]),
            }
        )
        hash = hashlib.md5(key.encode()).hexdigest()
        try:
            cache.get(hash)
        except:
            exec(hash, func, args, kwargs)
        finally:
            result, logs = cache.get(hash)
            if len(logs) > 0:
                print("\n".join(logs))
            return result

    return wrapper
