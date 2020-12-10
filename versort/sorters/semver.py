"""SemVer version sorting implementation."""
from semver import VersionInfo

from ..base import VersionSorterABC
from ..typing_extra import CallableThatReturnsSortable


class SemverSorter(VersionSorterABC):
    """SemVer sorter class."""

    def sorter(self) -> CallableThatReturnsSortable:
        """Return version object, sortable for SemVer."""
        return VersionInfo.parse
