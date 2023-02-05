ClashofClans-API
================

ClashofClans-API is an easy to use API for the mobile game ClashofClans

Installing
----------

Install and update using `pip`_:

.. code-block:: text

    $ pip install clashofclans-api

.. _pip: https://pip.pypa.io/en/stable/getting-started/

Create an API token
-------------------
An API token is required to execute the script. You can create one `here`_.

A Simple Example
----------------

.. _here: https://developer.clashofclans.com/#/new-key
.. code-block:: python

    from ClashofClans import ClashofClans

    coc = ClashofClans("your API token")

    response = coc.players.get_player_info("e.g. #9Q8QYQ20Q or 9Q8QYQ20Q")

    print(response)

.. code-block:: text

    $ python3 file.py
        (200, <Response [200]>, {'tag': '#9Q8QYQ20Q', 'name': 'Orange', 'townHallLevel': 15, 'townHallWeaponLevel': 4, 'expLevel': 244, ...
.. _Supercell’s Fan Content Policy: https://supercell.com/en/fan-content-policy/.

Disclaimer
----------
This content is not affiliated with, endorsed, sponsored, or specifically approved by Supercell and Supercell is not responsible for it.
For more information see `Supercell’s Fan Content Policy`_.
