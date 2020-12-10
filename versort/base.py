"""Common stuff for working with versort."""
from abc import ABC, abstractmethod
from typing import List

from .typing_extra import CallableThatReturnsSortable, VersionSorterClass


class VersionSorterABC(ABC):
    """Abstract base class for sorters.

    All sorters must implement at least abstract methods defined here to be valid.

    Examples:

        ```python
        class MySorter(VersionSorterABC)
            def sorter(self) -> CallableThatReturnsSortable:
                return my_parser
        ```
    """

    @abstractmethod
    def sorter(self) -> CallableThatReturnsSortable:
        """Return custom sorter callable.

        The callable must accept a `str` as input and return anything that
        allows being sorted by comparing it using `<`.

        You **must** override this method in subclasses.
        """

    def sort(self, *versions: str, reverse: bool = False) -> List[str]:
        """Sort the versions.

        Args:
            *versions:
                Version strings to be sorted.

            reverse:
                Whether the order must be reversed.
        """
        return sorted(versions, key=self.sorter(), reverse=reverse)


def get_sorter(algorithm: str) -> VersionSorterClass:
    """Get the proper sorter class according to the specified algorithm.

    Args:
        algorithm:
            One of these. It's case-insensitive:

            - `"PEP440"`
            - `"SemVer"`

    Raises:
        ValueError: If the sorter you want does not exist.

    Returns:
        The corresponding sorter class.
    """
    algorithm = algorithm.lower()
    if algorithm == "pep440":
        from .sorters.pep440 import PEP440Sorter

        return PEP440Sorter
    if algorithm == "semver":
        from .sorters.semver import SemverSorter

        return SemverSorter
    raise ValueError(f"Unknown sorter {algorithm}")
