# Copyright (c) ZakuroAI. All rights reserved.
# Licensed under the ZakuroAI License. See LICENSE for details.
"""Stdout-capturing context manager."""

import sys
from io import StringIO


class Capturing(list):
    """Context manager that captures everything written to ``sys.stdout``.

    On exit the captured lines are appended to *self* (which is a plain
    ``list``), making them available for later inspection.
    """

    def __enter__(self):
        """Redirect ``sys.stdout`` to an in-memory buffer and return *self*."""
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        """Restore the original ``sys.stdout`` and store captured lines."""
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout
