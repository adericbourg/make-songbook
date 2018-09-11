#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Local library related."""
import os
from typing import List


class Song(object):
    """Define a song."""

    def __init__(self, title: str, content: str):
        """Create a new song."""
        self.title = title
        self.content = content


class LibraryArtist:
    """Artist from library."""

    def __init__(self, name: str, songs: List[Song]):
        """Init LibraryArtist."""
        self.name = name
        self.songs = songs


class Library:
    """Representation of the local library."""

    def __init__(self, artists: List[LibraryArtist]):
        """Init Library."""
        self.artists = artists


def build_library(library_directory: str) -> Library:
    """Build library from provided path."""
    library_artists: List[LibraryArtist] = []
    for root, dir_names, _ in os.walk(library_directory):
        for artist_directory in dir_names:
            songs = _list_songs(os.path.join(root, artist_directory))
            library_artists.append(LibraryArtist(artist_directory, songs))
    return Library(library_artists)


def _list_songs(artist_directory: str) -> List[Song]:
    result: List[Song] = list()
    for _, _, file_names in os.walk(artist_directory):
        for name in file_names:
            file_full_name = os.path.join(artist_directory, name)
            song_name = _strip_extension(name)
            with open(file_full_name, 'r') as song_file:
                content = song_file.read()
                result.append(Song(song_name, content))
    return result


def _strip_extension(file_name) -> str:
    base_name = os.path.basename(file_name)
    short_name = os.path.splitext(base_name)[0]
    return short_name
