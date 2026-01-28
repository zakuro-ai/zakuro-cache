import sys

from zakuro_cache.loggers.capturing import Capturing


class TestCapturing:
    def test_captures_single_print(self):
        with Capturing() as output:
            print("hello")
        assert output == ["hello"]

    def test_captures_multiple_prints(self):
        with Capturing() as output:
            print("one")
            print("two")
            print("three")
        assert output == ["one", "two", "three"]

    def test_empty_when_nothing_printed(self):
        with Capturing() as output:
            pass
        assert output == []

    def test_restores_stdout_after_exit(self):
        original = sys.stdout
        with Capturing():
            pass
        assert sys.stdout is original

    def test_restores_stdout_on_exception(self):
        original = sys.stdout
        try:
            with Capturing():
                raise RuntimeError("boom")
        except RuntimeError:
            pass
        assert sys.stdout is original

    def test_output_is_list_instance(self):
        with Capturing() as output:
            print("test")
        assert isinstance(output, list)
