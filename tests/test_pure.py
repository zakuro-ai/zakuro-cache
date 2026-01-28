import pytest

import zakuro_cache.function.pure as pure_mod
from zakuro_cache import ZakuroCache
from zakuro_cache.function.pure import pure


@pytest.fixture(autouse=True)
def reset_cache():
    """Reset the module-level cache before each test."""
    pure_mod.cache = ZakuroCache()


class TestPure:
    def test_returns_correct_result(self):
        @pure
        def add(a, b):
            return a + b

        assert add(1, 2) == 3

    def test_caches_on_second_call(self):
        call_count = 0

        @pure
        def inc(x):
            nonlocal call_count
            call_count += 1
            return x + 1

        assert inc(5) == 6
        assert inc(5) == 6
        assert call_count == 1

    def test_different_args_produce_different_entries(self):
        @pure
        def double(x):
            return x * 2

        assert double(2) == 4
        assert double(3) == 6

    def test_captures_stdout(self, capsys):
        @pure
        def greet(name):
            print(f"hello {name}")
            return name

        result = greet("world")
        assert result == "world"
        captured = capsys.readouterr()
        assert "hello world" in captured.out

    def test_replays_stdout_on_cache_hit(self, capsys):
        @pure
        def say():
            print("cached line")
            return 1

        say()
        capsys.readouterr()  # discard first call output

        say()
        captured = capsys.readouterr()
        assert "cached line" in captured.out

    def test_handles_kwargs(self):
        @pure
        def kw_func(a, b=10):
            return a + b

        assert kw_func(1, b=20) == 21
