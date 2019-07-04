init:
	pip3 install --user -r requirements.txt

rise: init
	jupyter nbextension install rise --user --py
	jupyter nbextension enable rise --user --py

work:
	jupyter notebook

html:
	jupyter nbconvert --to slides 'deck.ipynb'

open:
	jupyter nbconvert --to slides 'deck.ipynb' --post serve
