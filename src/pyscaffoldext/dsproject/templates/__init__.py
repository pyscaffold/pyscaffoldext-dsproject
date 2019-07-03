# -*- coding: utf-8 -*-
import string
from pkg_resources import resource_string


def get_template(name):
    """Retrieve the template by name

    Args:
        name: name of template

    Returns:
        :obj:`string.Template`: template
    """
    file_name = "{name}.template".format(name=name)
    data = resource_string("pyscaffoldext.dsproject.templates",
                           file_name)
    return string.Template(data.decode("UTF-8"))


def gitignore_all(opts):
    """gitignore file that ignores just everything

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("gitignore_all")
    return template.safe_substitute(opts)


def environment_yaml(opts):
    """Environment.yaml with some basic libraries

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("environment_yaml")
    return template.safe_substitute(opts)


def readme_md(opts):
    """Adds a basic README.md

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("readme_md")
    opts['pkg'] = opts['package'].ljust(19)
    return template.safe_substitute(opts)


def template_ipynb(opts):
    """Adds a template Jupyter notebook

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("template_ipynb")
    return template.safe_substitute(opts)


def train_model_py(opts):
    """Adds a template python experiment

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("train_model_py")
    return template.safe_substitute(opts)
