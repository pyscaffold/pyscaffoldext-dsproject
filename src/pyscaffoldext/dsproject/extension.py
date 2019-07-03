# -*- coding: utf-8 -*-
import argparse

from pyscaffold.api import Extension, helpers
from pyscaffold.extensions.no_skeleton import NoSkeleton
from pyscaffold.extensions.pre_commit import PreCommit

from pyscaffoldext.markdown.extension import MarkDown

from . import templates


class IncludeExtensions(argparse.Action):
    """Activate other extensions
    """
    def __call__(self, parser, namespace, values, option_string=None):
        extensions = [
            NoSkeleton('no_skeleton'),
            PreCommit('pre_commit'),
            DSProject('dsproject')
        ]
        namespace.extensions.extend(extensions)


class DSProject(Extension):
    """Template for data-science projects
    """
    def augment_cli(self, parser):
        """Augments the command-line interface parser

        A command line argument ``--FLAG`` where FLAG=``self.name`` is added
        which appends ``self.activate`` to the list of extensions. As help
        text the docstring of the extension class is used.
        In most cases this method does not need to be overwritten.

        Args:
            parser: current parser object
        """
        help = self.__doc__[0].lower() + self.__doc__[1:]

        parser.add_argument(
            self.flag,
            help=help,
            nargs=0,
            dest="extensions",
            action=IncludeExtensions)
        return self

    def activate(self, actions):
        actions = self.register(
                actions,
                add_dsproject,
                after='define_structure'
        )
        actions = self.register(
                actions,
                replace_readme,
                after='add_dsproject'
        )
        return actions


def add_dsproject(struct, opts):
    """Adds basic module for custom extension

    Args:
        struct (dict): project representation as (possibly) nested
            :obj:`dict`.
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        struct, opts: updated project representation and options
    """
    gitignore_all = templates.gitignore_all(opts)

    for folder in ('external', 'interim', 'preprocessed', 'raw'):
        path = [opts["project"], "data", folder, ".gitignore"]
        struct = helpers.ensure(struct, path,
                                gitignore_all,
                                helpers.NO_OVERWRITE)

    path = [opts["project"], "notebooks", "template.ipynb"]
    template_ipynb = templates.template_ipynb(opts)
    struct = helpers.ensure(struct, path,
                            template_ipynb,
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "scripts", "train_model.py"]
    train_model_py = templates.train_model_py(opts)
    struct = helpers.ensure(struct, path,
                            train_model_py,
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "models", ".gitignore"]
    struct = helpers.ensure(struct, path,
                            gitignore_all,
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "references", ".gitignore"]
    struct = helpers.ensure(struct, path,
                            "",
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "reports", "figures", ".gitignore"]
    struct = helpers.ensure(struct, path,
                            "",
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "environment.yaml"]
    environment_yaml = templates.environment_yaml(opts)
    struct = helpers.ensure(struct, path,
                            environment_yaml,
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "requirements.txt"]
    struct = helpers.reject(struct, path)

    return struct, opts


def replace_readme(struct, opts):
    """Replace the readme.md of the markdown extension by our own

    Args:
        struct (dict): project representation as (possibly) nested
            :obj:`dict`.
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        struct, opts: updated project representation and options
    """
    # let the markdown extension do its job first
    struct, opts = MarkDown('markdown').markdown(struct, opts)

    file_path = [opts['project'], "README.md"]
    struct = helpers.reject(struct, file_path)
    readme = templates.readme_md(opts)
    struct = helpers.ensure(struct, file_path, readme, helpers.NO_OVERWRITE)
    return struct, opts
