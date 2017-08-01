=============
EC2 IP Lister
=============


.. image:: https://img.shields.io/pypi/v/ec2ips.svg
        :target: https://pypi.python.org/pypi/ec2ips

.. image:: https://img.shields.io/travis/ibejohn818/ec2ips.svg
        :target: https://travis-ci.org/ibejohn818/ec2ips

.. image:: https://readthedocs.org/projects/ec2ips/badge/?version=latest
        :target: https://ec2ips.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/ibejohn818/ec2ips/shield.svg
     :target: https://pyup.io/repos/github/ibejohn818/ec2ips/
     :alt: Updates


list ec2 ips for mussh


* Free software: MIT license
* Documentation: https://ec2ips.readthedocs.io.


Features
--------
List public IP's for ec2 instance formatted to use in mussh

Get mussh here: https://sourceforge.net/projects/mussh/

This is a quick and dirty version that just works that I needed to do some troubleshooting


Quick examples
--------------
Uptime on all instances

`mussh -h \`ec2ips all\` -m 0 -l 'ec2-user' -c 'uptime'`

PHP Procs on instances containing 'web'

`mussh -h \`ec2ips name web --contains\` -m 0 -l 'ec2-user' -c 'ps aux | grep php'`

List all instance name tags and #instance

`ec2ips list_names`

* TODO
- Create Tests
- CI/CD intergration
- Add more features
Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

