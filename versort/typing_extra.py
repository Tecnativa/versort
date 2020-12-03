"""Extra types used in this project."""
from typing import TYPE_CHECKING, Any, Callable, Protocol, Type

if TYPE_CHECKING:
    from .base import VersionSorterABC


class Sortable(Protocol):
    def __lt__(self, __other: Any) -> bool:
        ...


CallableThatReturnsSortable = Callable[[str], Sortable]
VersionSorterClass = Type["VersionSorterABC"]
