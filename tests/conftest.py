import io
import os
import runpy
import sys
from collections import namedtuple
from pathlib import Path

import pytest

from versort.base import get_sorter
from versort.cli import VerSortApp

ROOT = Path(__file__).parent.parent
Case = namedtuple("Case", ("input", "output"), defaults=([], []))


@pytest.fixture
def case_tester(monkeypatch, capsys):
    """Test a case in all possible forms."""

    def _inner(sorter_name: str, case: Case):
        sorter = get_sorter(sorter_name)()
        # API call, direct order
        assert sorter.sort(*case.input) == case.output
        # API call, inverse order
        reverse_output = list(reversed(case.output))
        assert sorter.sort(*case.input, reverse=True) == reverse_output
        # CLI call, direct order, arguments
        VerSortApp.run(["versort", sorter_name, *case.input], exit=False)
        result = capsys.readouterr()
        assert result.out.rstrip() == os.linesep.join(case.output)
        assert not result.err
        # CLI call, inverse order, stdin, custom separator
        with monkeypatch.context() as patcher:
            patcher.setattr(sys, "stdin", io.StringIO(" ".join(case.input)))
            VerSortApp.run(["versort", "-ris|", sorter_name], exit=False)
        result = capsys.readouterr()
        assert result.out.rstrip() == "|".join(reverse_output)
        assert not result.err
        # CLI call, first element, stdin
        with monkeypatch.context() as patcher:
            patcher.setattr(sys, "stdin", io.StringIO(" ".join(case.input)))
            VerSortApp.run(["versort", "--stdin", "--first", sorter_name], exit=False)
        result = capsys.readouterr()
        assert result.out.rstrip() == case.output[0]
        assert not result.err
        # CLI call as python module, last element, arguments
        with monkeypatch.context() as patcher:
            patcher.setattr(sys, "argv", [sys.argv[0], "-fr", sorter_name, *case.input])
            with pytest.raises(SystemExit, match=r"^0$"):
                runpy.run_module("versort", alter_sys=True)
        result = capsys.readouterr()
        assert result.out.rstrip() == case.output[-1]
        assert not result.err

    return _inner
