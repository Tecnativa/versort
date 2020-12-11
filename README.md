# VerSort

![License](https://img.shields.io/github/license/Tecnativa/versort)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/versort)
![PyPI](https://img.shields.io/pypi/v/versort)
![CI](https://github.com/Tecnativa/versort/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/Tecnativa/versort/branch/master/graph/badge.svg?token=1gDyBgOuPr)](https://codecov.io/gh/Tecnativa/versort)

Sort versions according to different versioning schemas.

## Install

To use as a CLI app:

```sh
pipx install versort
```

To use as a library:

```sh
pip install versort
```

## Usage

### Supported version algorithms

-   [PEP440](https://www.python.org/dev/peps/pep-0440/)
-   [SemVer](https://semver.org/)

### As a library

```python
from versort import get_sorter

sorter = get_sorter("pep440")()
print(sorter.sort("v1", "2a1", "2"))
```

### CLI

You can call `versort` directly, or as a Python module with `python -m versort`.

```sh
➤ echo 2 2a1 v1 | versort --stdin pep440
v1
2a1
2

➤ versort --reverse pep440 2 2a1 v1
2
2a1
v1

➤ versort --first pep440 2 2a1 v1
v1

➤ python -m versort --reverse --first pep440 2 2a1 v1
2
```
