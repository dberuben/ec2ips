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


list ec2 ips 


* Free software: MIT license
* Documentation: https://ec2ips.readthedocs.io.


Installation
------------

Install with pip from github

:code: `$: pip install git+github.com:dberuben/ec2ips.git`
:code: `$: pip install boto3`


Quick examples
--------------
List all instance name tags and #instance

:code:`$: ec2ips list_names`

All ips

:code:`$: ec2ips all`

Instance name equals 'web'

:code:`$: ec2ips name web`

Instances name contains 'web'

`ec2ips name web --contains`

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

