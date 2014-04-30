from distutils.core import setup

setup(
    name='scriptsearch',
    version='0.0.1',
    author='Jose Ricardo',
    author_email='root@josericardo.eti.br',
    packages=['scriptsearch'],
    scripts=['bin/scriptsearch'],
    url='http://pypi.python.org/pypi/bubbledoro/',
    license='LICENSE.txt',
    description='Searches for runnable scripts in a given dir.',
    long_description=open('README.md').read(),
    install_requires=[
    ],
)
