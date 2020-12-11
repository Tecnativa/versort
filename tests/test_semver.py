import pytest

from .conftest import Case

CASES = (
    Case(["10.0.0", "5.0.0", "0.0.0"], ["0.0.0", "5.0.0", "10.0.0"]),
    Case(
        ["2020.1.1", "1900.0.99", "2020.1.1-alpha.99", "2020.1.1-alpha.1"],
        ["1900.0.99", "2020.1.1-alpha.1", "2020.1.1-alpha.99", "2020.1.1"],
    ),
)


@pytest.mark.parametrize("case", CASES)
def test_cases(case: Case, case_tester):
    case_tester("semver", case)
