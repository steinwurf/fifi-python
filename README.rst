License
-------

A valid Steinwurf license is required if you wish to use this project.

Please request a license by **filling out the license request** form_.

Kodo is available under a research- and education-friendly license,
you can see the details here_.

If you try to configure without a valid license, then you will get an error!

.. _form: http://steinwurf.com/license/
.. _here: http://steinwurf.com/research-license/

About
-----

fifi-python contains a set of high-level Python bindings for the `Fifi
<https://github.com/steinwurf/fifi>`_ finite field C++ library. The
bindings provide access to the arithmetic operations provided by Fifi. The
examples folder provides sample applications showing the usage of the
Python API.

.. image:: http://buildbot.steinwurf.dk/svgstatus?project=fifi-python
    :target: http://buildbot.steinwurf.dk/stats?projects=fifi-python
    :alt: Buildbot status

If you have any questions or suggestions about this library, please contact
us at our developer mailing list (hosted at Google Groups):

* http://groups.google.com/group/steinwurf-dev

.. contents:: Table of Contents:
   :local:

Requirements
------------

First of all, follow `this Getting Started guide
<http://docs.steinwurf.com/getting_started.html>`_ to install
the basic tools required for the compilation (C++11 compiler, Git, Python).

The compilers used by Steinwurf are listed at the bottom of the
`buildbot page <http://buildbot.steinwurf.com>`_.

Linux
.....

These steps may not work with your specific Linux distribution, but they may
guide you in the right direction.

First, acquire the required packages from your package management system::

  sudo apt-get update
  sudo apt-get install python build-essential libpython-dev python-dev

If you are using Python 3, you'll need to install ``libpython3-dev`` instead.

Mac OSX
.......

Install the latest XCode and Command Line Tools from the Mac Store.

Python 2.7 is pre-installed on OSX, and the required Python headers should
also be available. If you are having trouble with the pre-installed Python
version, then you can install a more recent Python version with MacPorts or
Homebrew.

Windows
.......

Install Python 2.7 (32-bit) and Visual Studio Express 2015 for Windows Desktop.
Then set the ``VS90COMNTOOLS`` environment variable to::

  C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools\

so that Python distutils can detect your new compiler.


Building From Source
--------------------

It is recommended to build the Python bindings from source.

First, clone the project::

  git clone git@github.com:steinwurf/fifi-python.git

Configure and build the project::

  cd fifi-python
  python waf configure
  python waf build

Now the project is built and you should be able to find the resulting
``fifi.so`` or ``fifi.pyd`` file here (the actual path and extension is
dependent on your OS and Python version)::

  build/linux/src/fifi_python/fifi.so
  build/darwin/src/fifi_python/fifi.dylib
  build/win32/src/fifi_python/fifi.pyd

To use the bindings in your Python project you can do the following:

Using `PYTHONPATH`
..................

You can add the ``build/platform/src/fifi_python/`` path to your ``PYTHONPATH``
and import the module in your Python script::

  >>> import fifi

Copy the bindings to your project
.................................

Another option is to copy the built bindings e.g.
``build/linux/src/fifi_python/fifi.so``(for Linux) to your project directory.
As an example if your script is stored in ``/path/to/hello.py``, then copy
the bindings to ``/path/to/fifi.so`` and you should be able to ``import fifi``
from within the ``hello.py`` script.
