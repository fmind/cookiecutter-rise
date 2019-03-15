from invoke import task

@task
def init(c):
	c.run("jupyter nbextension install rise --user --py")
	c.run("jupyter nbextension enable rise --user --py")


@task
def edit(c):
	c.run("jupyter notebook")


@task
def serve(c):
	c.run("jupyter nbconvert --to slides 'deck.ipynb' --post serve")


@task
def export(c):
	c.run("jupyter nbconvert --to slides 'deck.ipynb'")
