from distutils.core import setup
from setuptools import find_packages

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(name='parallel-ssh',
      version='0.3',
      description='Wrapper library over paramiko to allow remote execution of tasks. Supports parallel execution on multiple hosts',
      author='Panos Kittenis',
      author_email='pkittenis@gmail.com',
      url = "https://github.com/pkittenis/parallel-ssh",
      py_modules = ['pssh'],
      install_requires = ['paramiko', 'gevent'],
      cmdclass = {'build_py': build_py},
      classifiers = [
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Unix',
        'Operating System :: POSIX :: BSD',
        'Operating System :: Windows',
        ],
      )
