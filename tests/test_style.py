from pre_commit.main import main as pre_commit


def test_pre_commit():
    pre_commit(("run", "--all-files", "--show-diff-on-failure", "--color=always"))
