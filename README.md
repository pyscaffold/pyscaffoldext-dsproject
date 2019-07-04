[![Build Status](https://travis-ci.org/pyscaffold/pyscaffoldext-dsproject.svg?branch=master)](https://travis-ci.org/pyscaffold/pyscaffoldext-dsproject)
[![Coveralls](https://img.shields.io/coveralls/github/pyscaffold/pyscaffoldext-dsproject/master.svg)](https://coveralls.io/r/pyscaffold/pyscaffoldext-dsproject)
[![PyPI-Server](https://img.shields.io/pypi/v/pyscaffoldext-dsproject.svg)](https://pypi.org/project/pyscaffoldext-dsproject)

# pyscaffoldext-dsproject

[PyScaffold] extension tailored for *Data Science* projects. This extension is inspired by
[cookiecutter-data-science] and enhanced in many ways. The main differences are that it
1. advocates a proper Python package structure that can be shipped and distributed,
2. uses a [conda] environment instead of something [virtualenv]-based and is thus more suitable
   for data science projects,
3. more default configurations for [Sphinx], [py.test], [pre-commit], etc. to foster
   clean coding and best practices.

Also consider using [dvc] to version control and share your data within your team.

The final directory structure looks like:
```
├── AUTHORS.rst             <- List of developers and maintainers.
├── CHANGELOG.rst           <- Changelog to keep track of new features and fixes.
├── LICENSE.txt             <- License as chosen on the command-line.
├── README.md               <- The top-level README for developers.
├── data
│   ├── external            <- Data from third party sources.
│   ├── interim             <- Intermediate data that has been transformed.
│   ├── processed           <- The final, canonical data sets for modeling.
│   └── raw                 <- The original, immutable data dump.
├── docs                    <- Directory for Sphinx documentation in rst or md.
├── environment.yaml        <- The conda environment file for reproducibility.
├── models                  <- Trained and serialized models, model predictions,
│                              or model summaries.
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for
│                              ordering), the creator's initials and a description,
│                              e.g. `1.0-fw-initial-data-exploration`.
├── references              <- Data dictionaries, manuals, and all other materials.
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures             <- Generated plots and figures for reports.
├── scripts                 <- Analysis and production scripts which import the
│                              actual PYTHON_PKG, e.g. train_model.
├── setup.cfg               <- Declarative configuration of your project.
├── setup.py                <- Make this project pip installable with `pip install -e`
│                              or `python setup.py develop`.
├── src
│   └── PYTHON_PKG          <- Actual Python package where the main functionality goes.
├── tests                   <- Unit tests which can be run with `py.test` or
│                              `python setup.py test`.
├── .coveragerc             <- Configuration for coverage reports of unit tests.
├── .isort.cfg              <- Configuration for git hook that sorts imports.
└── .pre-commit-config.yaml <- Configuration of pre-commit git hooks.
```

See a demonstration of the initial project structure under [dsproject-demo] and also check out
the the documentation of [PyScaffold] for more information.


## Usage

Just install this package with `pip install pyscaffoldext-dsproject`
and note that `putup -h` shows a new option `--dsproject`.
Creating a data science project is then as easy as:
```
putup --dsproject my_ds_project
```

## Note

This project has been set up using PyScaffold 3.2. For details and usage
information on PyScaffold see https://pyscaffold.org/.

[PyScaffold]: https://pyscaffold.org/
[cookiecutter-data-science]: https://github.com/drivendata/cookiecutter-data-science
[Miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Jupyter]: https://jupyter.org/
[dsproject-demo]: https://github.com/pyscaffold/dsproject-demo
[Sphinx]: http://www.sphinx-doc.org/
[py.test]: https://docs.pytest.org/
[conda]: https://docs.conda.io/
[virtualenv]: https://virtualenv.pypa.io/
[pre-commit]: https://pre-commit.com/
[dvc]: https://dvc.org/
