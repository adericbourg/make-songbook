#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Startup module."""

from makesongbook import song_library
from makesongbook import songbook_printer
from makesongbook.song_library import Library
import sys


def main():
    """Start the program."""
    if len(sys.argv) != 2:
        print("Usage:")
        print("  make-songbook.py /path/to/library/root")
        sys.exit(1)

    target = sys.argv[1]
    library: Library = song_library.build_library(target)
    songbook_printer.print_library(library, target)


if __name__ == '__main__':
    main()
