"""PEP440 version sorting implementation."""
from packaging.version import parse

from ..base import VersionSorterABC
from ..typing_extra import CallableThatReturnsSortable


class PEP440Sorter(VersionSorterABC):
    """PEP440 sorter class."""

    def sorter(self) -> CallableThatReturnsSortable:
        """Return version object, sortable for SemVer."""
        return parse
