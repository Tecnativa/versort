"""Extra types used in this project.

Objects here are only meant to be used for static typing.
"""

from typing import TYPE_CHECKING, Any, Callable, Protocol, Type

if TYPE_CHECKING:  # pragma: no cover
    from .base import VersionSorterABC


class Sortable(Protocol):
    """Anything that can be sorted."""

    def __lt__(self, __other: Any) -> bool:  # pragma: no cover
        ...


CallableThatReturnsSortable = Callable[[str], Sortable]
"""Anything that, returns a [Sortable][versort.typing_extra.Sortable] when called with a `str`."""

VersionSorterClass = Type["VersionSorterABC"]
"""A class that inherits from [VersionSorterABC][versort.base.VersionSorterABC]."""
