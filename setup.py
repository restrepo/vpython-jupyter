from __future__ import print_function

try:
    from setuptools import setup  # try first in case it's already there.
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

from Cython.Build import cythonize

import versioneer

setup(
    name='vpython',
    packages=['vpython'],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='VPython for Jupyter Notebook',
    long_description=open('README.md').read(),
    author='John Coady / Ruth Chabay / Bruce Sherwood / Steve Spicklemire',
    author_email='bruce.sherwood@gmail.com',
    url='http://pypi.python.org/pypi/vpython/',
    license='LICENSE.txt',
    keywords='vpython',
    classifiers=[
          'Framework :: IPython',
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Topic :: Multimedia :: Graphics :: 3D Modeling',
          'Topic :: Multimedia :: Graphics :: 3D Rendering',
          'Topic :: Scientific/Engineering :: Visualization',
    ],
    ext_modules = cythonize("vpython/cyvector.pyx"),
    install_requires=['jupyter', 'vpnotebook'],
    package_data={'vpython': ['data/*']},
)
