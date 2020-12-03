import pytest

from versort.sorters.semver import SemverSorter

from .conftest import Case

test_cases = (
    Case(["10.0.0", "5.0.0", "0.0.0"], ["0.0.0", "5.0.0", "10.0.0"]),
    Case(
        ["2020.1.1", "1900.0.99", "2020.1.1-alpha.99", "2020.1.1-alpha.1"],
        ["1900.0.99", "2020.1.1-alpha.1", "2020.1.1-alpha.99", "2020.1.1"],
    ),
)


@pytest.mark.parametrize("case", test_cases)
def test_semver_normal(case: Case):
    sorter = SemverSorter()
    assert sorter.sort(*case.input) == case.output
    reverse_output = list(reversed(case.output))
    assert sorter.sort(*case.input, reverse=True) == reverse_output
