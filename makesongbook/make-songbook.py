# -*- coding: utf-8 -*-
"""Startup module."""

from makesongbook import song_library
from makesongbook import songbook_printer
from makesongbook.song_library import Library


def main():
    """Start the program."""
    library: Library = song_library.build_library("/home/alban/tmp/Songbook/")
    songbook_printer.print_library(library)


if __name__ == '__main__':
    main()
