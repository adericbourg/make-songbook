#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Songbook printing."""

import os
import string
import zipfile
from shutil import copyfile

import jinja2

from makesongbook.song_library import Library

_TEMPLATE_FILE = "songbook.template.html"
_TOX_TEMPLATE_FILE = "tox.template.ncx"

_SONGBOOK_HTML_FILE = "songbook.html"
_TOC_FILE = "tox.ncx"
_CSS_FILE = "default.css"
_OPF_FILE = "book.opf"

_TMP_ZIP_NAME = "songbook.zip"
_EBOOK_NAME = "Songbook.epub"

_EBOOK_FILES = [_SONGBOOK_HTML_FILE, _TOC_FILE, _CSS_FILE, _OPF_FILE]
_STATIC_FILES = [_CSS_FILE, _OPF_FILE]


def print_library(library: Library, target: str):
    """Print library into a songbook."""
    _cleanup_target(target)

    template_env = _build_template_engine()

    songbook_file = os.path.join(target, _SONGBOOK_HTML_FILE)
    toc_file = os.path.join(target, _TOC_FILE)

    _write_songbook(template_env, library, songbook_file)
    _write_tox(template_env, library, toc_file)
    _write_static_files(target)

    _make_epub(target)


def _cleanup_target(target: str):
    target_files = [os.path.join(target, f) for f in _EBOOK_FILES]
    for target_file in target_files:
        if os.path.exists(target_file):
            os.remove(target_file)

    ebook_path = os.path.join(target, _EBOOK_NAME)
    if os.path.exists(ebook_path):
        os.remove(ebook_path)


def _build_template_engine() -> jinja2.Environment:
    template_loader = jinja2.FileSystemLoader(searchpath="./template")

    template_env = jinja2.Environment(loader=template_loader)
    template_env.filters['artist_anchor'] = _artist_anchor
    template_env.filters['song_anchor'] = _song_anchor
    template_env.filters['song_content'] = _song_content

    return template_env


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


def _write_static_files(target: str):
    for f in _STATIC_FILES:
        src = "template/{}".format(f)
        dst = os.path.join(target, f)
        copyfile(src, dst)


def _make_epub(target):
    # Zip ebook content
    songbook_files = [os.path.join(target, f) for f in _EBOOK_FILES]
    zip_name = os.path.join(target, _TMP_ZIP_NAME)
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for f in songbook_files:
            zip_file.write(f, os.path.basename(f))

    # Create epub
    os.rename(
        os.path.join(target, _TMP_ZIP_NAME),
        os.path.join(target, _EBOOK_NAME)
    )

    # Cleanup
    for f in songbook_files:
        os.remove(os.path.join(target, f))


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
