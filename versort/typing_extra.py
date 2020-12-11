"""Extra types used in this project.

Objects here are only meant to be used for static typing.
"""

from typing import TYPE_CHECKING, Any, Callable, Protocol, Type

if TYPE_CHECKING:  # pragma: no cover
    from .base import VersionSorterABC


class VersionObject(Protocol):
    """Anything that can be sorted."""

    major: Any

    def __lt__(self, __other: Any) -> bool:  # pragma: no cover
        ...


CallableThatReturnsVersionObject = Callable[[str], VersionObject]
"""Anything that, returns a [VersionObject][versort.typing_extra.VersionObject] when called with a `str`."""

VersionSorterClass = Type["VersionSorterABC"]
"""A class that inherits from [VersionSorterABC][versort.base.VersionSorterABC]."""
