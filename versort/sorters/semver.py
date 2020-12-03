"""SemVer version sorting implementation."""
from semver import VersionInfo

from ..base import VersionSorterABC
from ..typing_extra import CallableThatReturnsSortable


class SemverSorter(VersionSorterABC):
    def _sorter(self) -> CallableThatReturnsSortable:
        return VersionInfo.parse
