[![Build Status](https://travis-ci.org/pyscaffold/pyscaffoldext-dsproject.svg?branch=master)](https://travis-ci.org/pyscaffold/pyscaffoldext-dsproject)
[![Coveralls](https://img.shields.io/coveralls/github/pyscaffold/pyscaffoldext-dsproject/master.svg)](https://coveralls.io/r/pyscaffold/pyscaffoldext-dsproject)
[![PyPI-Server](https://img.shields.io/pypi/v/pyscaffoldext-dsproject.svg)](https://pypi.org/project/pyscaffoldext-dsproject)

# pyscaffoldext-dsproject

PyScaffold extension tailored for *Data Science* projects. This extension is inspired by
[cookiecutter-data-science] and enhanced in many ways.

Besides the typical [PyScaffold] layout, the extensions provides:

* `data` folder to keep your data,
* `experiments` folder for the actual scripts, e.g. `train_model.py`,
* `notebooks` for data exploration with [Jupyter] notebooks,
* `notebooks/template.ipynb` for starting with the most important imports and plugins,
* `models` for trained and serialized models, model predictions, or model summaries,
* `references` for data dictionaries, manuals, and all other explanatory materials.
* `reports` for generated analysis as HTML, PDF, LaTeX, etc. and a `figures` subdirectory
  for generated graphics and figures to be used in reporting,
* `environment.yaml` to create an [conda][Miniconda] environment with the most
  needed data science libraries and tools,
* `README.md` with lots of information about how to install your package and development advices.

Check out the initial project structure under [dsproject-demo].

## Usage

Just install this package with `pip install pyscaffoldext-dsproject`
and note that `putup -h` shows a new option `--dsproject`.

## Note

This project has been set up using PyScaffold 3.2. For details and usage
information on PyScaffold see https://pyscaffold.org/.

[PyScaffold]: https://pyscaffold.org/
[cookiecutter-data-science]: https://github.com/drivendata/cookiecutter-data-science
[Miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Jupyter]: https://jupyter.org/
[dsproject-demo]: https://github.com/pyscaffold/dsproject-demo
