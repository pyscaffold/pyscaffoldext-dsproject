# -*- coding: utf-8 -*-
from os.path import exists as path_exists

from pyscaffold.api import create_project
from pyscaffold.cli import parse_args, process_opts
from pyscaffold.utils import chdir

EXT_FLAG = "--dsproject"
FLAKE8 = "flake8 --max-line-length=88"


def test_add_custom_extension(tmpfolder):
    args = [EXT_FLAG, "my_project", "-p", "my_package"]
    opts = parse_args(args)
    opts = process_opts(opts)
    create_project(opts)

    assert path_exists("my_project/src/my_package/__init__.py")


def test_generated_extension_flake8(tmpfolder, venv_run):
    args = [EXT_FLAG, "my_project"]
    opts = parse_args(args)
    opts = process_opts(opts)
    create_project(opts)

    with chdir("my_project"):
        assert '' == venv_run(FLAKE8)
        venv_run("python setup.py install")

    venv_run("putup {ext_flag} the_actual_project".format(ext_flag=EXT_FLAG))
    assert path_exists("the_actual_project/setup.cfg")

    with chdir("the_actual_project"):
        assert '' == venv_run(FLAKE8)
