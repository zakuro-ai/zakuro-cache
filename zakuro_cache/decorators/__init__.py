import json
import hashlib
from zakuro_cache.loggers import Capturing
from zakuro_cache import cache
import time

def main(hash, func, args, kwargs, cache):
    with Capturing() as logs:
        t0=time.time()
        result = func(*args, **kwargs)
        if not cache.forbids(hash):
            cache.set(hash, result)
            cache.set_logger(hash, logs)
            cache.set_exec_time(hash, time.time() - t0)
        if len(logs) > 0:
            print("\n".join(logs))
    return result

def zakuro_cache(func):
    """

    :param fcn:
    :return:
    """

    def wrapper(*args, **kwargs):
        # global cache
        # key = json.dumps({"args": args, "kwargs":kwargs, "call": "@".join([func.__name__,  func.__module__])})
        # hash = hashlib.md5(key.encode()).hexdigest()
        # result = None, None
        try:
            t0 = time.time()
            result, _t_put = cache.get(hash)
            _t_get = time.time() - t0
            if _t_get>_t_put:
                print("Cache too slow...")
                cache.unset(hash)
        except:
            result = main(hash, func, args, kwargs, cache)
            # commands = [
            #     "with Capturing() as logs: " \
            #     f"    t0=time.time();" \
            #     f"    result = func(*args, **kwargs);" \
            #     f"    cache.set(hash, result);" \
            #     f"    cache.set_logger(hash, logs);" \
            #     f"    cache.set_exec_time(hash, time.time() - t0)"
            # ]
            # for command in commands:
            #     exec(command)
            

        return result

    return wrapper