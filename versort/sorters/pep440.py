"""PEP440 version sorting implementation.

It is based on [`packaging`](https://packaging.pypa.io/en/stable/version.html).

See the [PEP440 spec](https://www.python.org/dev/peps/pep-0440/).
"""

from packaging.version import parse

from ..base import VersionSorterABC
from ..typing_extra import CallableThatReturnsSortable


class PEP440Sorter(VersionSorterABC):
    """PEP440 sorter class."""

    def sorter(self) -> CallableThatReturnsSortable:
        """Return version parsing function, suitable for PEP440."""
        return parse
