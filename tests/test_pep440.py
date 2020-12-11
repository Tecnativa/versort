import pytest

from .conftest import Case

CASES = (
    Case(["v10", "v5", "v0"], ["v0", "v5", "v10"]),
    Case(
        ["2020.01.01", "v1900.00.99", "2020.01.01.alpha.99", "2020.01.01.alpha.001"],
        ["v1900.00.99", "2020.01.01.alpha.001", "2020.01.01.alpha.99", "2020.01.01"],
    ),
)


@pytest.mark.parametrize("case", CASES)
def test_cases(case: Case, case_tester):
    case_tester("pep440", case)
