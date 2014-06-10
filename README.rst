golang for virtualenvwrapper
============================

Very simple, effective go virtual environments that work directly with
python's virtualenv and virtualenvwrapper.

How does it work?
-----------------

It's just a virtualenvwrapper extension!

If you are already using that, just

  $ pip install govenv

And next time you make a virtualenv by using ``mkvirtualenv`` it will create
a ``gopath`` directory in your venv folder to hold all your golang source.
Now, whenever you activate that it will set your ``GOPATH`` and ``PATH``,
and return it to its previous setting when you deactive.

It's extremely simple, you should just look at the source:
`gopath.py <tree/master/govenv/gopath.py>`
