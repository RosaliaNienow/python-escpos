# -*- coding: utf-8 -*-
"""python-escpos enables you to manipulate escpos-printers."""

__all__ = ["constants", "escpos", "exceptions", "printer"]

try:
    from .version import version as __version__  # noqa
except ImportError:  # pragma: no cover
    raise ImportError(
        "Failed to find (autogenerated) version.py. "
        "This might be because you are installing from GitHub's tarballs, "
        "use the PyPI ones."
    )
