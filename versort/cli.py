"""CLI application and utilities."""
import os
import sys
from io import StringIO
from unittest.mock import patch

from plumbum import cli

from . import __version__, get_sorter


class VerSortApp(cli.Application):
    """A simple version sorter CLI app.

    Supported algorithms: PEP440, SemVer.
    """

    VERSION = __version__

    first = cli.Flag(["-f", "--first"], help="Print only first match")
    reverse = cli.Flag(["-r", "--reverse"], help="Reverse order")
    separator = cli.SwitchAttr(
        ["-s", "--separator"],
        help="Separator used when printing sorted results; the default is a new line",
    )
    stdin = cli.Flag(["-i", "--stdin"], help="Read tags from STDIN")

    def main(self, algorithm: str, *versions: str):
        sorter = get_sorter(algorithm)()
        if self.stdin:
            versions = tuple(sys.stdin.read().split())
        sorted_versions = sorter.sort(*versions, reverse=self.reverse)
        if self.first:
            print(sorted_versions[0])
            return
        separator = os.linesep if self.separator is None else self.separator
        print(*sorted_versions, sep=separator)


# Add --help-all results to docs
if __doc__:
    help_io = StringIO()
    with patch("sys.stdout", help_io):
        VerSortApp.run(["versort", "--help-all"], exit=False)
    help_io.seek(0)
    __doc__ += f"\n\nCLI help generated from `versort --help-all`:\n\n```\n{help_io.read()}\n```"
