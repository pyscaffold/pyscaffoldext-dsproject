import stat
from typing import List

from pyscaffold.actions import Action, ActionParams, ScaffoldOpts, Structure
from pyscaffold.extensions import Extension, include
from pyscaffold.extensions.no_skeleton import NoSkeleton
from pyscaffold.extensions.pre_commit import PreCommit
from pyscaffold.identification import get_id
from pyscaffold.operations import add_permissions, no_overwrite
from pyscaffold.structure import ensure, merge

from pyscaffoldext.markdown.extension import Markdown, replace_files

from .templates import readme_md, template

NO_OVERWRITE = no_overwrite()


class DSProject(Extension):
    """Template for data-science projects"""

    name = "dsproject"

    def augment_cli(self, parser):
        """Augments the command-line interface parser

        A command line argument ``--FLAG`` where FLAG=``self.name`` is added
        which appends ``self.activate`` to the list of extensions. As help
        text the docstring of the extension class is used.
        In most cases this method does not need to be overwritten.

        Args:
            parser: current parser object
        """

        parser.add_argument(
            self.flag,
            help=self.help_text,
            nargs=0,
            dest="extensions",
            action=include(NoSkeleton(), PreCommit(), self),
        )
        return self

    def activate(self, actions: List[Action]) -> List[Action]:
        actions = Markdown().activate(actions)
        # ^  Wrapping the Markdown extension is more reliable then including it via CLI.
        #    This way we can trust the activation order for registering actions,
        #    and the Python API is guaranteed to work, even if the user does not include
        #    Markdown in the list of extensions.
        actions = self.register(actions, add_dsproject, after="define_structure")
        actions = self.register(actions, replace_readme, after=get_id(replace_files))
        return actions


def add_dsproject(struct: Structure, opts: ScaffoldOpts) -> ActionParams:
    """Adds basic module for custom extension
    See :obj:`pyscaffold.actions.Action`
    """
    gitignore_all = (template("gitignore_all"), NO_OVERWRITE)

    files: Structure = {
        "configs": {".gitignore": ("", NO_OVERWRITE)},
        "data": {
            ".gitignore": (template("gitignore_data"), NO_OVERWRITE),
            **{
                folder: {".gitignore": gitignore_all}
                for folder in ("external", "interim", "preprocessed", "raw")
            },
        },
        "environment.yml": (template("environment_yml"), NO_OVERWRITE),
        "models": {".gitignore": gitignore_all},
        "notebooks": {"template.ipynb": (template("template_ipynb"), NO_OVERWRITE)},
        "references": {".gitignore": ("", NO_OVERWRITE)},
        "reports": {"figures": {".gitignore": ("", NO_OVERWRITE)}},
        "scripts": {
            "train_model.py": (
                template("train_model_py"),
                add_permissions(stat.S_IXUSR, NO_OVERWRITE),
            )
        },
    }

    return merge(struct, files), opts


def replace_readme(struct: Structure, opts: ScaffoldOpts) -> ActionParams:
    """Replace the readme.md of the markdown extension by our own
    See :obj:`pyscaffold.actions.Action`
    """
    return ensure(struct, "README.md", readme_md, NO_OVERWRITE), opts
