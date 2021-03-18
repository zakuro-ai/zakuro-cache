class ZakuroCache:
    def __init__(self):
        super(ZakuroCache, self).__init__()
        self.cache = {}

    def set(self, hash, result):
        self.cache[hash] = {"result": result,  "logs": []}

    def set_logger(self, hash, logs):
        self.cache[hash]["logs"] = logs

    def get(self, hash):
        return list(self.cache[hash].values())

