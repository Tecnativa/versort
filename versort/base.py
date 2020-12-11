"""Common stuff for working with versort."""
from abc import ABC, abstractmethod
from contextlib import suppress
from typing import List, Set

from .typing_extra import CallableThatReturnsVersionObject, VersionSorterClass


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
    def parser(self) -> CallableThatReturnsVersionObject:
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
        return sorted(versions, key=self.parser(), reverse=reverse)


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


def lazy_git():
    """Import [GitPython](https://gitpython.readthedocs.io/) lazily."""
    import git

    return git


def git_tag_matches(
    sorter: VersionSorterABC,
    repo_root: str = ".",
    *,
    branch: bool = False,
    latest: str = "",
    major: bool = False,
    pattern: str = "%s",
) -> Set[str]:
    """Get smart matches of git tags.

    This method is quite simple, but the name is a bit misleading. I didn't find
    a better name, sorry for that. 🤷‍♂️

    It will get git repo's `HEAD` and try to obtain as much information of its
    tags as possible. Then, it will return a `set` of matching tags according to
    the criteria, formatted with the pattern.

    To use this method, [Git](https://git-scm.com/) must be installed.

    Args:
        sorter:
            An instance of a sorter class.

        repo_root:
            A path to an existing Git repo root folder.

        branch:
            Set to `True` if you want to consider `HEAD`'s ref (the branch)
            a valid match.

        latest:
            Set to any `str` value to add this raw tag to the list of results,
            if `HEAD` happens to be the latest commit, sorted with the given
            sorter.

        major:
            Set to `True` if you want to add to the list of matches a tag with
            just the major part of the version object.

        pattern:
            Any `str` which contains a single `%s`, which will be used to
            format the results in the list.

    Returns: List of formatted matching tags. The order is not relevant.

    Examples:

        This is all too complex to understand, right? OK, let's put a practical
        example: when you want to map tags from a Git repo to a container image.

        So, let's say you have a git repository in `/tmp/test` that contains
        a `Containerfile` meant to build a container image called
        `ghcr.io/tecnativa/versort`. The git repository is checked out in the
        `master` branch, and tagged as `1.2.3`, following SemVer.

        You want to tag your container images automatically, like this:

        -   `ghcr.io/tecnativa/versort:master` points to the latest commit in
            the git `master` branch.
        -   `ghcr.io/tecnativa/versort:latest` points to the latest tagged
            release in git, sorted using SemVer.
        -   `ghcr.io/tecnativa/versort:1.2.3` points to that exact same git tag.
        -   `ghcr.io/tecnativa/versort:1` points to the latest git tag, sorted
            with SemVer, that belongs to the major release `1`.

        Well, you can use this method like this:

        ```python
        from versort.base import get_sorter, git_tag_matches
        from pathlib import Path
        from pprint import pprint

        sorter = get_sorter("semver")()
        repo_root = Path("/tmp/test")
        matches = git_tag_matches(sorter, repo_root, branch=True, latest="latest", major=True, pattern="ghcr.io/tecnativa/versort:%s")

        pprint(matches)
        # {'ghcr.io/tecnativa/versort:1.2.3',
        #  'ghcr.io/tecnativa/versort:latest',
        #  'ghcr.io/tecnativa/versort:1',
        #  'ghcr.io/tecnativa/versort:master'}
        ```
    """
    git = lazy_git()
    repo = git.Repo(repo_root)
    result = set()
    latest_tag = None
    with suppress(IndexError):
        latest_tag = sorter.sort(*map(str, repo.tags))[-1]
    for tag in repo.tags:
        if repo.head.commit != tag.commit:
            continue
        # Add tag match
        result.add(pattern % tag)
        # Add latest match
        if latest and tag.name == latest_tag:
            result.add(pattern % latest)
        # Add major tag match
        if major:
            parse = sorter.parser()
            tag_parsed = parse(tag.name)
            tags_sharing_major = filter(
                lambda _tag: parse(str(_tag)).major == tag_parsed.major,
                repo.tags,
            )
            latest_of_major = sorter.sort(*map(str, tags_sharing_major))[-1]
            if tag.name == latest_of_major:
                result.add(pattern % tag_parsed.major)
    # Add branch match
    if branch:
        with suppress(TypeError):
            result.add(pattern % repo.head.ref)
    return result
