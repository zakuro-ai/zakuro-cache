import pytest

from zakuro_cache.zakuro_cache import ZakuroCache


@pytest.fixture
def cache():
    return ZakuroCache()


class TestSet:
    def test_stores_result_with_empty_logs(self, cache):
        cache.set("abc", 42)
        assert cache.cache["abc"] == {"result": 42, "logs": []}

    def test_overwrites_existing_entry(self, cache):
        cache.set("abc", 1)
        cache.set("abc", 2)
        assert cache.cache["abc"]["result"] == 2

    def test_handles_none(self, cache):
        cache.set("k", None)
        assert cache.cache["k"]["result"] is None

    def test_handles_dict(self, cache):
        cache.set("k", {"a": 1})
        assert cache.cache["k"]["result"] == {"a": 1}

    def test_handles_list(self, cache):
        cache.set("k", [1, 2, 3])
        assert cache.cache["k"]["result"] == [1, 2, 3]

    def test_handles_str(self, cache):
        cache.set("k", "hello")
        assert cache.cache["k"]["result"] == "hello"


class TestSetLogger:
    def test_attaches_logs_to_entry(self, cache):
        cache.set("abc", 42)
        cache.set_logger("abc", ["line1", "line2"])
        assert cache.cache["abc"]["logs"] == ["line1", "line2"]

    def test_raises_key_error_on_missing_key(self, cache):
        with pytest.raises(KeyError):
            cache.set_logger("missing", ["log"])


class TestGet:
    def test_returns_result_and_logs(self, cache):
        cache.set("abc", 42)
        cache.set_logger("abc", ["log1"])
        assert cache.get("abc") == [42, ["log1"]]

    def test_raises_key_error_on_missing_hash(self, cache):
        with pytest.raises(KeyError):
            cache.get("missing")
