import os
from pathlib import Path
from subprocess import CalledProcessError

import pytest
from pyscaffold import cli
from pyscaffold.file_system import chdir

from pyscaffoldext.dsproject.extension import DSProject

from .helpers import run, run_common_tasks

EXT_FLAG = DSProject().flag

# If you need to check logs with caplog, have a look on
# pyscaffoldext-custom-extension's tests/conftest.py file and the
# `isolated_logger` fixture.

EXPECTED_DIRS = [
    "configs",
    "data/external",
    "data/interim",
    "data/preprocessed",
    "data/raw",
    "models",
    "reports/figures",
]

EXPECTED_FILES = [
    "README.md",
    "environment.yml",
    "notebooks/template.ipynb",
    "scripts/train_model.py",
    "src/my_package/__init__.py",
]


def test_add_custom_extension(tmpfolder):
    args = ["--no-config", "-vv", EXT_FLAG, "my_project", "-p", "my_package"]
    # --no-config: avoid extra config from dev's machine interference
    cli.main(args)

    with chdir("my_project"):
        assert not Path("README.rst").exists()
        for path in EXPECTED_DIRS:
            assert Path(path).is_dir()
        for path in EXPECTED_FILES:
            assert Path(path).is_file()


def test_add_custom_extension_and_pretend(tmpfolder):
    args = [
        "--no-config",
        "--pretend",
        "-vv",
        EXT_FLAG,
        "my_project",
        "-p",
        "my_package",
    ]
    # --no-config: avoid extra config from dev's machine interference
    cli.main(args)

    assert not Path("my_project").exists()


@pytest.mark.slow
@pytest.mark.system
def test_generated_extension(tmpfolder):
    args = ["--no-config", "-vv", "--venv", "--pre-commit", EXT_FLAG, "my_project"]
    # --no-config: avoid extra config from dev's machine interference
    # --venv: generate a venv so we can install the resulting project
    # --pre-commit: ensure generated files respect repository conventions
    cli.main(args)

    with chdir("my_project"):
        # Testing a project generated by the custom extension
        run_common_tasks(tests=False)


def test_new_project_does_not_fail_pre_commit(cwd, pre_commit, putup):
    # Given pyscaffold is installed,
    # when we call putup with extensions and pre-commit
    name = "my_project"
    run(f"{putup} --pre-commit --dsproject -p my_package {name}")
    with cwd.join(name).as_cwd():
        # then the newly generated files should not result in errors when
        # pre-commit runs...
        try:
            run(f"{pre_commit} install")
            run(f"{pre_commit} run --all")
        except CalledProcessError as ex:
            if os.name == "nt" and (
                "filename or extension is too long"
                in ((ex.stdout or "") + (ex.stderr or ""))
            ):
                pytest.skip("Sometimes Windows have problems with nested files")
                # Even if we try to change that by configuring the CI
                # environment
            else:
                raise
