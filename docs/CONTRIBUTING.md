# VerSort contribution guidelines

Thank you for considering contributing to our project. 😊

There are a few ways to contribute:

1. [Discuss](https://github.com/Tecnativa/versort/discussions). Talk there about
   anything related to our project.
1. [Issues](https://github.com/Tecnativa/versort/issues). Publish one when there's a
   bug, problem or feature request for this project.
1. [Pull requests](https://github.com/Tecnativa/versort/pulls). Here you can propose
   code changes to our project.

Read [this good guide](https://opensource.guide/how-to-contribute/) about how to use
those features effectively.

Be respectful. Speak English if possible, to let most of the world understand most of
your words.

## Set up a development environment

If you want to code, to set up a working development environment, you should have these
things installed:

-   [Git](https://git-scm.com/).
-   A supported [Python](https://www.python.org/) version.
-   [Poetry](https://python-poetry.org/).
-   [pre-commit](https://pre-commit.com/).

Once all is installed, execute:

```sh
poetry install
pre-commit install
```

Then, write your changes, and add new tests for them. Try to avoid modifying existing
tests, always add new ones; this way you make sure everything that was working before,
is still working. Aim for 100% coverage. Run tests with:

```sh
poetry run pytest
```

Once you're satisfied with the changes, commit them with Git, and
[open a pull request](https://opensource.guide/how-to-contribute/#opening-a-pull-request).
