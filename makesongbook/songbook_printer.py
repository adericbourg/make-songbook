#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Songbook printing."""

import os

import jinja2

from makesongbook.song_library import Library

_TEMPLATE_FILE = "songbook.template.txt"


def print_library(library: Library, target: str):
    """Print library into a songbook."""
    songbook_file = os.path.join(target, "songbook.txt")
    print("Printing library to:", target)
    if os.path.exists(songbook_file):
        os.remove(songbook_file)

    template_loader = jinja2.FileSystemLoader(searchpath="./template")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(_TEMPLATE_FILE)

    output = template.render({"library": library})

    with open(songbook_file, 'a') as songbook:
        songbook.write(output)
