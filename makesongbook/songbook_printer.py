#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Songbook printing."""

from makesongbook.song_library import Library


def print_library(library: Library, target: str):
    """Print library into a songbook."""
    print("Printing library from:", target)
