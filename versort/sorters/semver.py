"""SemVer version sorting implementation.

It is based on [`python-semver`](https://python-semver.readthedocs.io/en/stable/usage.html#parsing-a-version-string).

See the [SemVer spec](https://semver.org/).
"""

from semver import VersionInfo

from ..base import VersionSorterABC
from ..typing_extra import CallableThatReturnsVersionObject


class SemverSorter(VersionSorterABC):
    """SemVer sorter class."""

    def parser(self) -> CallableThatReturnsVersionObject:
        """Return version parsing function, suitable for SemVer."""
        return VersionInfo.parse
