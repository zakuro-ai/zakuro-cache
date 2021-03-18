class ZakuroCache:
    def __init__(self):
        super(ZakuroCache, self).__init__()
        self.cache = {}
        self._forbids = set()

    def set(self, hash, result):
        self.cache[hash] = {"result": result,  "logs": [], "time": -1}

    def set_logger(self, hash, logs):
        self.cache[hash]["logs"] = logs

    def get(self, hash):
        return self.cache[hash]["result"], self.cache[hash]["time"]

    def set_exec_time(self, hash, t):
        self.cache[hash]["time"] = t

    def unset(self, hash):
        del self.cache[hash]
        self._forbids.add(hash)

    def forbids(self, hash):
        return hash in self._forbids

cache = ZakuroCache()
