from os import path
from codecs import open
from setuptools import setup, find_packages

# we're using a README.md, if you do not have this in your folder, simply
# replace this with a string.
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Here you specify the meta-data of your package. The `name` argument is
# needed in some other steps.
setup(
    name='triplestore-collaboration-descriptives',
    version="1.0.0",
    description='Vantage6 algorithm that retrieves the descriptive information of triplestores in a collaboration',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/STRONGAYA/triplestore-collaboration-descriptives',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[
        'vantage6-algorithm-tools',
        'pandas',
        'requests'
    ]
)
