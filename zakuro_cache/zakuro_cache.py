# Copyright (c) ZakuroAI. All rights reserved.
# Licensed under the ZakuroAI License. See LICENSE for details.
"""Core in-memory cache for function results and captured logs."""


class ZakuroCache:
    """In-memory cache that associates a hash key with a result and log lines.

    Each entry stores the return value of a cached function together with
    any stdout output captured during its execution.
    """

    def __init__(self):
        super(ZakuroCache, self).__init__()
        self.cache = {}

    def set(self, hash, result):
        """Store *result* under the given *hash*, initialising an empty log.

        Parameters
        ----------
        hash : str
            Cache key (typically an MD5 hex digest).
        result : object
            The value to cache.
        """
        self.cache[hash] = {"result": result, "logs": []}

    def set_logger(self, hash, logs):
        """Attach captured log lines to an existing cache entry.

        Parameters
        ----------
        hash : str
            Cache key whose entry should be updated.
        logs : list[str]
            Captured stdout lines to store alongside the result.
        """
        self.cache[hash]["logs"] = logs

    def get(self, hash):
        """Retrieve the cached result and logs for *hash*.

        Parameters
        ----------
        hash : str
            Cache key to look up.

        Returns
        -------
        list
            A two-element list ``[result, logs]``.

        Raises
        ------
        KeyError
            If *hash* is not present in the cache.
        """
        return list(self.cache[hash].values())
