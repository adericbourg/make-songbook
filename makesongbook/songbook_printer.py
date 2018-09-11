#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Songbook printing."""

import os
import string

import jinja2

from makesongbook.song_library import Library

_TEMPLATE_FILE = "songbook.template.html"
_TOX_TEMPLATE_FILE = "tox.template.ncx"


def print_library(library: Library, target: str):
    """Print library into a songbook."""
    songbook_file = os.path.join(target, "songbook.html")
    if os.path.exists(songbook_file):
        os.remove(songbook_file)
    tox_file = os.path.join(target, "tox.ncx")
    if os.path.exists(tox_file):
        os.remove(tox_file)

    template_loader = jinja2.FileSystemLoader(searchpath="./template")

    template_env = jinja2.Environment(loader=template_loader)
    template_env.filters['artist_anchor'] = _artist_anchor
    template_env.filters['song_anchor'] = _song_anchor
    template_env.filters['song_content'] = _song_content

    _write_songbook(template_env, library, songbook_file)
    _write_tox(template_env, library, tox_file)


def _write_songbook(env, library: Library, songbook_file):
    template = env.get_template(_TEMPLATE_FILE)
    output = template.render({"library": library})

    with open(songbook_file, 'a') as songbook:
        songbook.write(output)


def _write_tox(env, library: Library, tox_file):
    template = env.get_template(_TOX_TEMPLATE_FILE)
    output = template.render({"library": library})

    with open(tox_file, 'a') as songbook:
        songbook.write(output)


def _artist_anchor(value: str) -> str:
    return "art-{}".format(_sanitize(value))


def _song_anchor(value: str, artist: str) -> str:
    return "sng-{}-{}".format(_sanitize(artist), _sanitize(value))


def _sanitize(s: str) -> str:
    lower = s.lower().replace(" ", "_")
    printable = set(string.printable)
    return ''.join(c for c in lower if c in printable)


def _song_content(value: str) -> str:
    return value.replace(" ", "&nbsp;").replace("\n", "<br />\n")
