=============================
Nobinobi Child
=============================

.. image:: https://badge.fury.io/py/nobinobi-child.svg
    :target: https://badge.fury.io/py/nobinobi-child

.. image:: https://travis-ci.org/alu/nobinobi-child.svg?branch=master
    :target: https://travis-ci.org/alu/nobinobi-child

.. image:: https://codecov.io/gh/alu/nobinobi-child/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/alu/nobinobi-child

Application Child for Nobinobi

Documentation
-------------

The full documentation is at https://nobinobi-child.readthedocs.io.

Quickstart
----------

Install Nobinobi Child::

    pip install nobinobi-child

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'nobinobi_child.apps.NobinobiChildConfig',
        ...
    )

Add Nobinobi Child's URL patterns:

.. code-block:: python

    from nobinobi_child import urls as nobinobi_child_urls


    urlpatterns = [
        ...
        url(r'^', include(nobinobi_child_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
