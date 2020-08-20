from functools import partial

from pyscaffold.templates import ScaffoldOpts, get_template

from .. import __version__ as dsproject_version

template = partial(get_template, relative_to=__name__)


def readme_md(opts: ScaffoldOpts) -> str:
    """Adds a basic README.md

    Args:
        opts: given options, see :obj:`create_project` for an extensive list.

    Returns:
        file content as string
    """
    opts["pkg"] = opts["package"].ljust(19)
    opts["dsproject_version"] = dsproject_version
    return template("readme_md").safe_substitute(opts)
