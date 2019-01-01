example_service
===============

**example_service** is .....

The :file:`settings.ini` file contains options
for running the Flask app, like the DEBUG flag:

.. literalinclude:: ../../example_service/settings.ini
   :language: ini

Blueprint are imported from :mod:`example_service.endpoints` and one
Blueprint and view example was provided in :file:`example_service/endpoints/main.py`:

.. literalinclude:: ../../example_service/endpoints/main.py
   :name: main.py
   :emphasize-lines: 15