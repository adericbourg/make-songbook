#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Songbook printing."""

import os

from makesongbook.song_library import Library


def print_library(library: Library, target: str):
    """Print library into a songbook."""
    songbook_file = os.path.join(target, "songbook.txt")
    print("Printing library to:", target)
    if os.path.exists(songbook_file):
        os.remove(songbook_file)
    with open(songbook_file, 'a') as songbook:
        for artist in library.artists:
            songbook.write("===========\n".format(artist.name))
            songbook.write("==== {} ====\n".format(artist.name))
            songbook.write("===========\n".format(artist.name))
            for song in artist.songs:
                songbook.write("-- {}\n".format(song.title))
                songbook.write(song.content)
