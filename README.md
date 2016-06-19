hosts_replacer
===============================

version number: 0.0.1
author: Kensuke Kaieda

Overview
--------

hosts replace for concentrate, work and so on.

Attention For Mac users
----------------------------

Please cache clear.
`sudo dscacheutil -flushcache`

Attention For Chrome users
--------------------------------

If you use chrome, clear dns cache in chrome.
go to `chrome://net-internals/#dns` , and put 'clear host cache' button.

Then, go to `chrome://net-internals/#sockets`, and put 'close idle sockets' button.

Installation / Usage
--------------------

To install use pip:

    $ pip install hosts_replacer


Or clone the repo:

    $ git clone https://github.com/qooh0/hosts_replacer.git
    $ python setup.py install

Contributing
------------

TBD

Example
-------

TBD
