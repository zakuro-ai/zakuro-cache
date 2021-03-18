import json
import hashlib
from zakuro_cache.loggers import Capturing
from zakuro_cache import cache
def zakuro_cache(func):
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
            commands = [
                "with Capturing() as logger: " \
                f"    cache.set(hash, func(*args, **kwargs));" \
                f"    cache.set_logger(hash, logger)"
            ]
            for command in commands:
                exec(command)

        finally:
            result, logs = cache.get(hash)
            if len(logs)>0:
                print("\n".join(logs))
            return result

    return wrapper