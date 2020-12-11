import pytest
from pre_commit.main import main as pre_commit

from versort import get_sorter


def test_style():
    """Just run pre-commit and see what happens."""
    pre_commit(("run", "--all-files", "--show-diff-on-failure", "--color=always"))


def test_unknown_sorter():
    """See there's a valid error when a sorter is unknown."""
    with pytest.raises(ValueError):
        get_sorter("missing")
