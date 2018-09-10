#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Local library related."""
import os
from typing import List


class LibraryArtist:
    """Artist from library."""

    def __init__(self, name: str, songs: List[str]):
        """Init LibraryArtist."""
        self.name = name
        self.songs = songs


class Library:
    """Representation of the local library."""

    def __init__(self, root: str, artists: List[LibraryArtist]):
        """Init Library."""
        self.root = root
        self.artists = artists


def build_library(library_directory: str) -> Library:
    """Build library from provided path."""
    library_artists: List[LibraryArtist] = []
    for root, dir_names, _ in os.walk(library_directory):
        for artist_directory in dir_names:
            songs = _list_song_files(os.path.join(root, artist_directory))
            library_artists.append(LibraryArtist(artist_directory, songs))
    return Library(library_directory, library_artists)


def _list_song_files(artist_directory: str) -> List[str]:
    result: List[str] = list()
    for _, _, file_names in os.walk(artist_directory):
        result.extend(file_names)
    return result
