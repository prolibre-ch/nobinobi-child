=====
Usage
=====

To use Nobinobi Child in a project, add it to your `INSTALLED_APPS`:

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
