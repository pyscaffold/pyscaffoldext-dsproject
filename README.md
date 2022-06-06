[![Build Status](https://api.cirrus-ci.com/github/pyscaffold/pyscaffoldext-dsproject.svg?branch=master)](https://cirrus-ci.com/github/pyscaffold/pyscaffoldext-dsproject)
[![ReadTheDocs](https://readthedocs.org/projects/pyscaffold/badge/?version=latest)](https://pyscaffold.org/projects/dsproject/en/latest)
[![Coveralls](https://img.shields.io/coveralls/github/pyscaffold/pyscaffoldext-dsproject/master.svg)](https://coveralls.io/r/pyscaffold/pyscaffoldext-dsproject)
[![PyPI-Server](https://img.shields.io/pypi/v/pyscaffoldext-dsproject.svg)](https://pypi.org/project/pyscaffoldext-dsproject)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/pyscaffoldext-dsproject.svg)](https://anaconda.org/conda-forge/pyscaffoldext-dsproject)
[![Downloads](https://pepy.tech/badge/pyscaffoldext-dsproject/month)](https://pepy.tech/project/pyscaffoldext-dsproject)

# pyscaffoldext-dsproject

[PyScaffold] extension tailored for *Data Science* projects. This extension is inspired by
[cookiecutter-data-science] and enhanced in many ways. The main differences are that it
1. advocates a proper Python package structure that can be shipped and distributed,
2. uses a [conda] environment instead of something [virtualenv]-based and is thus more suitable
   for data science projects,
3. more default configurations for [Sphinx], [pytest], [pre-commit], etc. to foster
   clean coding and best practices.

Also consider using [dvc] to version control and share your data within your team.
Read [this blogpost] to learn how to work with JupyterLab notebooks efficiently by using a
data science project structure like this.

The final directory structure looks like:
```
├── AUTHORS.md              <- List of developers and maintainers.
├── CHANGELOG.md            <- Changelog to keep track of new features and fixes.
├── CONTRIBUTING.md         <- Guidelines for contributing to this project.
├── Dockerfile              <- Build a docker container with `docker build .`.
├── LICENSE.txt             <- License as chosen on the command-line.
├── README.md               <- The top-level README for developers.
├── configs                 <- Directory for configurations of model & application.
├── data
│   ├── external            <- Data from third party sources.
│   ├── interim             <- Intermediate data that has been transformed.
│   ├── processed           <- The final, canonical data sets for modeling.
│   └── raw                 <- The original, immutable data dump.
├── docs                    <- Directory for Sphinx documentation in rst or md.
├── environment.yml         <- The conda environment file for reproducibility.
├── models                  <- Trained and serialized models, model predictions,
│                              or model summaries.
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for
│                              ordering), the creator's initials and a description,
│                              e.g. `1.0-fw-initial-data-exploration`.
├── pyproject.toml          <- Build configuration. Don't change! Use `pip install -e .`
│                              to install for development or to build `tox -e build`.
├── references              <- Data dictionaries, manuals, and all other materials.
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures             <- Generated plots and figures for reports.
├── scripts                 <- Analysis and production scripts which import the
│                              actual PYTHON_PKG, e.g. train_model.
├── setup.cfg               <- Declarative configuration of your project.
├── setup.py                <- [DEPRECATED] Use `python setup.py develop` to install for
│                              development or `python setup.py bdist_wheel` to build.
├── src
│   └── PYTHON_PKG          <- Actual Python package where the main functionality goes.
├── tests                   <- Unit tests which can be run with `pytest`.
├── .coveragerc             <- Configuration for coverage reports of unit tests.
├── .isort.cfg              <- Configuration for git hook that sorts imports.
└── .pre-commit-config.yaml <- Configuration of pre-commit git hooks.
```

See a demonstration of the initial project structure under [dsproject-demo] and also check out
the documentation of [PyScaffold] for more information.


## Usage

Just install this package with `conda install -c conda-forge pyscaffoldext-dsproject`
and note that `putup -h` shows a new option `--dsproject`.
Creating a data science project is then as easy as:
```bash
putup --dsproject my_ds_project
```

The flag `--dsproject` comprises additionally the flags `--markdown`, `--pre-commit` and `--no-skeleton`
for convenience.

<!-- pyscaffold-notes -->

## Making Changes & Contributing

This project uses [pre-commit], please make sure to install it before making any
changes:

```bash
conda install pre-commit
cd pyscaffoldext-dsproject
pre-commit install
```

It is a good idea to update the hooks to the latest version:

```bash
pre-commit autoupdate
```

Please also check PyScaffold's [contribution guidelines].

[PyScaffold]: https://pyscaffold.org/
[cookiecutter-data-science]: https://github.com/drivendata/cookiecutter-data-science
[Miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Jupyter]: https://jupyter.org/
[dsproject-demo]: https://github.com/pyscaffold/dsproject-demo
[Sphinx]: https://www.sphinx-doc.org/
[pytest]: https://docs.pytest.org/
[conda]: https://docs.conda.io/
[Conda-Forge]: https://anaconda.org/conda-forge/pyscaffoldext-dsproject
[virtualenv]: https://virtualenv.pypa.io/
[pre-commit]: https://pre-commit.com/
[dvc]: https://dvc.org/
[this blogpost]: https://florianwilhelm.info/2018/11/working_efficiently_with_jupyter_lab/
[pre-commit]: https://pre-commit.com/
[contribution guidelines]: https://pyscaffold.org/en/latest/contributing.html
