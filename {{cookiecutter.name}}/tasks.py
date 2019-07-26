from invoke import task
from pathlib import Path


@task
def venv(c, force=False):
    """Create a virtual environment for Python."""
    if Path("venv").exists() and not force:
        return None

    c.run("python3 -m venv venv --clear")
    c.run("venv/bin/pip install --requirement requirements.txt")
    c.run("venv/bin/jupyter nbextension install rise --user --py")
    c.run("venv/bin/jupyter nbextension enable rise --user --py")


@task(venv)
def work(c):
    """Run an instance of jupyter notebook."""
    c.run("venv/bin/jupyter notebook")


@task(venv)
def html(c):
    """Convert the slide deck to HTML."""
    c.run('venv/bin/jupyter nbconvert --to slides "deck.ipynb"')


@task(venv)
def open(c):
    """Open the presentation."""
    c.run('venv/bin/jupyter nbconvert --to slides "deck.ipynb" --post serve')
