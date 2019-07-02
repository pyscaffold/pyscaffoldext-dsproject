#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for custom_extension.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""
from __future__ import absolute_import, division, print_function

import os
import shlex
import stat
from shutil import rmtree

import pytest


def set_writable(func, path, exc_info):
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise RuntimeError


@pytest.fixture
def tmpfolder(tmpdir):
    old_path = os.getcwd()
    newpath = str(tmpdir)
    os.chdir(newpath)
    try:
        yield tmpdir
    finally:
        os.chdir(old_path)
        rmtree(newpath, onerror=set_writable)


@pytest.fixture
def venv(virtualenv):
    """Create a virtualenv for each test"""
    return virtualenv


@pytest.fixture
def venv_run(venv):
    """Run a command inside the venv"""

    def _run(*args, **kwargs):
        # pytest-virtualenv doesn't play nicely with external os.chdir
        # so let's be explicit about it...
        kwargs['cd'] = os.getcwd()
        kwargs['capture'] = True
        if len(args) == 1 and isinstance(args[0], str):
            args = shlex.split(args[0])
        return venv.run(args, **kwargs).strip()

    return _run
