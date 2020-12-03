"""PEP440 version sorting implementation."""
from packaging.version import parse

from ..base import VersionSorterABC
from ..typing_extra import CallableThatReturnsSortable


class PEP440Sorter(VersionSorterABC):
    def _sorter(self) -> CallableThatReturnsSortable:
        return parse
