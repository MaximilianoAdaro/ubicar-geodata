Pipenv: Python Development Workflow
==============================================

**Pipenv** is a tool that aims to bring the best of all packaging worlds
(bundler, composer, npm, cargo, yarn, etc.) to the Python world.
*Windows is a first-class citizen, in our world.*

It automatically creates and manages a virtualenv for your projects, as
well as adds/removes packages from your `Pipfile` as you
install/uninstall packages. It also generates the ever-important
`Pipfile.lock`, which is used to produce deterministic builds.

Installation
------------

If you\'re using Debian Buster+:

    $ sudo apt install pipenv

Or, if you\'re using Fedora:

    $ sudo dnf install pipenv

Or, if you\'re using FreeBSD:

    # pkg install py36-pipenv

When none of the above is an option, it is recommended to use [Pipx](https://pypi.org/p/pipx):

    $ pipx install pipenv

Otherwise, refer to the [documentation](https://pipenv.pypa.io/en/latest/#install-pipenv-today) for instructions.

✨🍰✨


☤ Usage
-------

    $ pipenv
    Usage: pipenv [OPTIONS] COMMAND [ARGS]...

    Options:
      --where          Output project home information.
      --venv           Output virtualenv information.
      --py             Output Python interpreter information.
      --envs           Output Environment Variable options.
      --rm             Remove the virtualenv.
      --bare           Minimal output.
      --completion     Output completion (to be eval'd).
      --man            Display manpage.
      --three / --two  Use Python 3/2 when creating virtualenv.
      --python TEXT    Specify which version of Python virtualenv should use.
      --site-packages  Enable site-packages for the virtualenv.
      --version        Show the version and exit.
      -h, --help       Show this message and exit.


    Usage Examples:
       Create a new project using Python 3.7, specifically:
       $ pipenv --python 3.7

       Remove project virtualenv (inferred from current directory):
       $ pipenv --rm

       Install all dependencies for a project (including dev):
       $ pipenv install --dev

       Create a lockfile containing pre-releases:
       $ pipenv lock --pre

       Show a graph of your installed dependencies:
       $ pipenv graph

       Check your installed dependencies for security vulnerabilities:
       $ pipenv check

       Install a local setup.py into your virtual environment/Pipfile:
       $ pipenv install -e .

       Use a lower-level pip command:
       $ pipenv run pip freeze

    Commands:
      check      Checks for security vulnerabilities and against PEP 508 markers
                 provided in Pipfile.
      clean      Uninstalls all packages not specified in Pipfile.lock.
      graph      Displays currently–installed dependency graph information.
      install    Installs provided packages and adds them to Pipfile, or (if no
                 packages are given), installs all packages from Pipfile.
      lock       Generates Pipfile.lock.
      open       View a given module in your editor.
      run        Spawns a command installed into the virtualenv.
      scripts    Displays the shortcuts in the (optional) [scripts] section of 
                 Pipfile. 
      shell      Spawns a shell within the virtualenv.
      sync       Installs all packages specified in Pipfile.lock.
      uninstall  Un-installs a provided package and removes it from Pipfile.

Locate the project:

    $ pipenv --where
    /Users/kennethreitz/Library/Mobile Documents/com~apple~CloudDocs/repos/kr/pipenv/test

Locate the virtualenv:

    $ pipenv --venv
    /Users/kennethreitz/.local/share/virtualenvs/test-Skyy4vre

Locate the Python interpreter:

    $ pipenv --py
    /Users/kennethreitz/.local/share/virtualenvs/test-Skyy4vre/bin/python

Install packages:

    $ pipenv install
    Creating a virtualenv for this project...
    ...
    No package provided, installing all dependencies.
    Virtualenv location: /Users/kennethreitz/.local/share/virtualenvs/test-EJkjoYts
    Installing dependencies from Pipfile.lock...
    ...

    To activate this project's virtualenv, run the following:
    $ pipenv shell

Install a dev dependency:

    $ pipenv install pytest --dev
    Installing pytest...
    ...
    Adding pytest to Pipfile's [dev-packages]...

Show a dependency graph:

    $ pipenv graph
    requests==2.18.4
      - certifi [required: >=2017.4.17, installed: 2017.7.27.1]
      - chardet [required: >=3.0.2,<3.1.0, installed: 3.0.4]
      - idna [required: >=2.5,<2.7, installed: 2.6]
      - urllib3 [required: <1.23,>=1.21.1, installed: 1.22]

Generate a lockfile:

    $ pipenv lock
    Assuring all dependencies from Pipfile are installed...
    Locking [dev-packages] dependencies...
    Locking [packages] dependencies...
    Note: your project now has only default [packages] installed.
    To install [dev-packages], run: $ pipenv install --dev

Install all dev dependencies:

    $ pipenv install --dev
    Pipfile found at /Users/kennethreitz/repos/kr/pip2/test/Pipfile. Considering this to be the project home.
    Pipfile.lock out of date, updating...
    Assuring all dependencies from Pipfile are installed...
    Locking [dev-packages] dependencies...
    Locking [packages] dependencies...

Uninstall everything:

    $ pipenv uninstall --all
    No package provided, un-installing all dependencies.
    Found 25 installed package(s), purging...
    ...
    Environment now purged and fresh!

Use the shell:

    $ pipenv shell
    Loading .env environment variables...
    Launching subshell in virtual environment. Type 'exit' or 'Ctrl+D' to return.
    $ ▯

☤ Documentation
---------------

Documentation resides over at [pipenv.pypa.io](https://pipenv.pypa.io/en/latest/).
