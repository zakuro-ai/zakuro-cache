import json
import hashlib
from zakuro_cache.loggers import Capturing
from zakuro_cache import ZakuroCache
cache = ZakuroCache()


def exec(hash, func, args, kwargs):
    with Capturing() as logger:
        cache.set(hash, func(*args, **kwargs))
        cache.set_logger(hash, logger)


def deterministic(func):
    """

    :param fcn:
    :return:
    """

    def wrapper(*args, **kwargs):
        global cache
        key = json.dumps({"args": args, "kwargs":kwargs, "call": "@".join([func.__name__,  func.__module__])})
        hash = hashlib.md5(key.encode()).hexdigest()
        try:
            cache.get(hash)
        except:
            exec(hash, func, args, kwargs)
        finally:
            result, logs = cache.get(hash)
            if len(logs)>0:
                print("\n".join(logs))
            return result

    return wrapper