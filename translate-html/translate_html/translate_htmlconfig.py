#! /usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2011 David Planella <david.planella@ubuntu.com>
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

# THIS IS TranslateHtml CONFIGURATION FILE
# YOU CAN PUT THERE SOME GLOBAL VALUE
# Do not touch unless you know what you're doing.
# you're warned :)

__all__ = [
    'project_path_not_found',
    'get_data_file',
    'get_data_path',
    ]

# Where your project will look for your data (for instance, images and ui
# files). By default, this is ../data, relative your trunk layout
__translate_html_data_directory__ = '../data/'
__translate_html_sources_directory__ = '../../'
__license__ = 'GPL-3'
__version__ = 'VERSION'

import os
PO_FOLDER = 'po-html'
GETTEXT_DOMAIN = 'ubuntu-online-tour'
POTFILES = 'POTFILES.in'

class project_path_not_found(Exception):
    """Raised when we can't find the project directory."""


def get_data_file(*path_segments):
    """Get the full path to a data file.

    Returns the path to a file underneath the data directory (as defined by
    `get_data_path`). Equivalent to os.path.join(get_data_path(),
    *path_segments).
    """
    return os.path.join(get_data_path(), *path_segments)


def get_data_path():
    """Retrieve translate-html data path

    This path is by default <translate_html_lib_path>/../data/ in trunk
    and /usr/share/translate-html in an installed version but this path
    is specified at installation time.
    """

    # Get pathname absolute or relative.
    path = os.path.join(
        os.path.dirname(__file__), __translate_html_data_directory__)

    abs_data_path = os.path.abspath(path)
    if not os.path.exists(abs_data_path):
        raise project_path_not_found

    return abs_data_path


def get_source_file(*path_segments):
    """Get the full path to a source file.

    Returns the path to a file underneath the sources directory (as defined by
    `get_sources_path`). Equivalent to os.path.join(get_sources_path(),
    *path_segments).
    """
    return os.path.join(get_sources_path(), *path_segments)


def get_sources_path():
    """Retrieve translate-html sources path

    This path is by default <translate_html_lib_path>/../../ in trunk
    """

    # Get pathname absolute or relative.
    path = os.path.join(
        os.path.dirname(__file__), __translate_html_sources_directory__)

    abs_sources_path = os.path.abspath(path)
    if not os.path.exists(abs_sources_path):
        raise project_path_not_found

    return abs_sources_path
